
# basic data analysis libraries
from statsmodels.formula.api import logit
import statsmodels.api as sm
from IPython.display import HTML
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import pylab as plt
import seaborn as sns
sns.set_style("whitegrid")


def lag_indicator(df, min_=1, max_=7):
    for i in range(min_, max_):
        df['IU'+str(i)] = df['BILL_AMT'+str(i)] / df['LIMIT_BAL']
        df['PER_PAYED'+str(i)] = df['PAY_AMT'+str(i)] / df['BILL_AMT'+str(i)]
        df['PER_PAYED'+str(i)] = df['PER_PAYED'+str(i)
                                    ].replace([np.inf, -np.inf], np.nan).fillna(0)

    months = (6 - np.arange(6)).reshape(1, -1)
    # see if the IU and percent payed is increasing or decreasing with time, a.k.a, has correlation

    fields_per_payed = ['PER_PAYED'+str(i) for i in range(min_, max_)]
    df['TREND_PER_PAYED'] = 1 - \
        pairwise_distances(df[fields_per_payed], months, metric='correlation')
    df['TREND_PER_PAYED'] = df['TREND_PER_PAYED'].replace(
        [np.inf, -np.inf], np.nan).fillna(0)

    fields_IU = ['IU'+str(i) for i in range(min_, max_)]
    df['TREND_PER_IU'] = 1 - \
        pairwise_distances(df[fields_IU], months, metric='correlation')
    df['TREND_PER_IU'] = df['TREND_PER_IU'].replace(
        [np.inf, -np.inf], np.nan).fillna(0)
    return df


def EDA_continuous_v1(df, var, target='target', datetime='dt_ref', preprocess=None, hist_bins=100, figsize=(10, 5)):
    display(HTML("EDA %s" % var))
    display(df[var].to_frame().describe(
        percentiles=np.linspace(0, 1, 11)).round(2).T)

    plt.figure(figsize=figsize)

    # plot 1
    plt.subplot(121)
    plt.title(" Histogram - %s" % var)
    df[var].hist(bins=hist_bins, density=True)
    plt.xlabel(var)

    # plot 2
    plt.subplot(122)
    temp = pd.DataFrame({
        'rank': KBinsDiscretizer(n_bins=hist_bins, encode='ordinal').fit_transform(df[[var]]).flatten(),
        'rank_cluster': KBinsDiscretizer(n_bins=5, strategy='kmeans', encode='ordinal').fit_transform(df[[var]]).flatten(),
        var: preprocess(df[var].values) if preprocess is not None else df[var],
        target: df[target],
        datetime: df[datetime]
    })
    sns.regplot(x=var, y=target, ax=plt.gca(),
                data=temp.groupby('rank').mean())

    plt.title("Correlation %0.4f" % temp.groupby(
        'rank').mean().corr().values[0, 1])
    plt.tight_layout()
    plt.show()

    # plot 3
    plt.figure(figsize=(figsize[0], 3))
    ax = plt.gca()
    temp.pivot_table(index=datetime, columns='rank_cluster',
                     values=target).plot(ax=ax)
    ax.legend(loc='upper center', bbox_to_anchor=(
        0.5, -0.10), fancybox=True, shadow=True, ncol=10)
    ax.set_xlabel(datetime)
    ax.set_ylabel(f"Mean {target}")
    ax.set_title(f"{target} per cluster of {var} over time")
    plt.tight_layout()
    plt.show()

    display(
        temp
        .drop(columns=['rank_cluster'])
        .groupby('rank').mean()
        .style.background_gradient(axis=0)
        .format(precision=3)
    )


def income2Range(x):
    # income are generaly exponential.
    x = x/1000

    return str(int(np.log(x)))


# Assuming the limit gave to the client has to something to do with his income.
# in the practice the risk + income defines the limit. So in the real world using the limit as input would break your model.
df['PROXY_INCOME'] = df['LIMIT_BAL'].apply(income2Range)
(
    df
    .pivot_table(index='dt_ref', columns='PROXY_INCOME', values='target')
    .round(2)
    .plot(figsize=(15, 4), title='Risk by Income Range')
)

display(HTML("We can see that different limits/incomes has different risks"))


# suggested variables - feel free to change
vars = [
    'PROXY_INCOME',
    'TREND2_IU',
    'TREND_PER_PAYED',
    'SEX',
    'MARRIED',
    'IU1',
    'AGE_NORM'
]

df2 = df.copy().replace([np.inf, -np.inf], np.nan).fillna(0)

logit_mod = logit('target ~ ' + (' + '.join(vars)), df2.query('sample_id < 7'))
logit_res = logit_mod.fit(disp=0)
display(logit_res.summary())

df = (
    df.assign(
        prob=logit_res.predict(df2),
        score=lambda x: createCluster(x, n_bins=7)
    )
)


# trying to understand the behaviour of sensible variables.
(
    df
    .copy()
    .assign(isMale=lambda x: x['SEX'] == 1)
    .groupby('score')
    .agg(
        mean_age=('AGE', 'mean'),
        max_age=('AGE', 'max'),
        per_male=('isMale', 'mean'),
        per_MARRIED=('MARRIED', 'mean'),
        target=('target', 'mean'),
    )
    .astype({'mean_age': 'int'})
    .round(2)
    .style.background_gradient(axis=0)
)

# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_2.py
# 🔹 Analysis Result:
#   1. Standard => Credit Information Business Act B.E.2545
#   ⦿ Section: 3
#    ⁃ Count of standard compliance in the code block:
#      ◦ income2Range: 2
#      ◦ PROXY_INCOME: 3
#      ◦ Income: 1
#      ◦ incomes: 1
#      ◦ AGE_NORM: 1
#      ◦ mean_age: 2
#      ◦ AGE: 2
#      ◦ max_age: 1
#      Total: 13
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ Credit Information Business Act B.E.2545 at section 10
# 🔹 Reference Number: c4e86aab4b49a92289a89df13dfceea57a5d22b8ce8e4176c4a385271022a67b
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_2.py
# 🔹 Analysis Result:
#   1. Standard => ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Credit Scoring Development
#    ⁃ Count of standard compliance in the code block:
#      ◦ data: 2
#      ◦ df: 34
#      ◦ df2: 3
#      Total: 39
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.6
#    ⁃ Count of standard compliance in the code block:
#      ◦ sample_id: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.1
#    ⁃ Count of standard compliance in the code block:
#      ◦ sample_id: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System I
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.2
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System II
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Verification of the Applicant’s Information
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.3
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Overrides in Credit Approval
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Construction of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Definition of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
# 🔹 Reference Number: 292be6495cdd00a5fcc3083a5ed88a0fbc14ad6f698665df47bee11ec5b5fa32
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_2.py
# 🔹 Analysis Result:
#   1. Standard => ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Credit Scoring Development
#    ⁃ Count of standard compliance in the code block:
#      ◦ data: 2
#      ◦ df: 34
#      ◦ df2: 3
#      Total: 39
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.6
#    ⁃ Count of standard compliance in the code block:
#      ◦ sample_id: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.1
#    ⁃ Count of standard compliance in the code block:
#      ◦ sample_id: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System I
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.2
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System II
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Verification of the Applicant’s Information
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.3
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Overrides in Credit Approval
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Construction of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Definition of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
# 🔹 Reference Number: 7632e37f40a9fec074c2d19f34e10b289d909094bf4225d1c23cab37d2657a13
