import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import model_selection, linear_model, metrics


def credit_log_modelling(cr_data):
    # we will shorten the last 2 feature names and address the null values
    cr_data = cr_data.rename(columns={
                             "cb_person_default_on_file": "default_hist", "cb_person_cred_hist_length": "cr_hist_len"})
    cr_data.isnull().sum()
    # percentage of null values from loan int rate col
    cr_data.loan_int_rate.isnull().sum() / cr_data.shape[0]

    plt.hist(cr_data['person_emp_length'])
    plt.xlabel("Employment Length")
    plt.ylabel("Frequency")
    plt.title("Freq vs Employment Length")
    plt.show()

    plt.hist(cr_data['loan_int_rate'])
    plt.xlabel("Interest Rate")
    plt.ylabel("Frequency")
    plt.title("Freq vs Interest Rate")

    colors = ["blue", "red"]
    plt.scatter(cr_data['person_age'], cr_data['loan_int_rate'],
                c=cr_data['loan_status'],
                cmap=mpl.colors.ListedColormap(colors), alpha=0.5)
    plt.xlabel("Person Age")
    plt.ylabel("Loan Interest Rate")
    plt.title("Interest Rate vs Age")

    cr_clean1 = cr_data[cr_data['person_age'] <= 100]
    cr_data[cr_data['person_age'] > 100]
    pd.crosstab(cr_clean1['default_hist'], cr_clean1['loan_grade'])

    # note 0 is non default and 1 is default
    default_hist_status_tab = pd.crosstab(
        cr_clean1['default_hist'], cr_clean1['loan_status'])
    default_hist_status_tab

    total1 = default_hist_status_tab.iloc[0].sum()

    defaulted1 = default_hist_status_tab.iloc[0, 1]

    total2 = default_hist_status_tab.iloc[1].sum()
    defaulted2 = default_hist_status_tab.iloc[1, 1]

    first_default = round(defaulted1 / total1 * 100, 2)
    second_default = round(defaulted2 / total2 * 100, 2)

    print("Despite the measures taken, {}% of clients defaulted for the first time.".format(
        first_default))
    print("And {}% of clients who had previously defaulted, defaulted again.".format(
        second_default))

    pd.crosstab(cr_clean1['default_hist'], cr_clean1['loan_intent'],
                values=cr_clean1['loan_int_rate'], aggfunc='median')

    # one hot encoding categorical variables
    num_col = cr_clean1.select_dtypes(exclude='object')
    char_col = cr_clean1.select_dtypes(include='object')

    encoded_char_col = pd.get_dummies(char_col)

    cr_clean2 = pd.concat([num_col, encoded_char_col], axis=1)

    # Split Train and Test Sets
    Y = cr_clean2['loan_status']
    X = cr_clean2.drop('loan_status', axis=1)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(
        X, Y, random_state=2020, test_size=.30)

    # Start of Classification Logistics Regression
    log_clf = linear_model.LogisticRegression()
    log_clf.fit(x_train, np.ravel(y_train))
    col_effect = pd.DataFrame()
    col_effect['col_names'] = X.columns
    col_effect['col_coef'] = log_clf.coef_[0]

    predict_log = pd.DataFrame(log_clf.predict_proba(x_test)[
                               :, 1], columns=['prob_default'])
    pred_df = pd.concat([y_test.reset_index(drop=True), predict_log], axis=1)

    return pred_df
