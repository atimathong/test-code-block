import ipywidgets as widgets
from IPython.display import display
from ipywidgets import *
from collections import Counter
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from pandas import DataFrame


data = pd.read_csv('cs-training.csv', sep=';').drop('Unnamed: 0', axis=1)
collections = 2
# min = pd.Series.min()
Cols = []
for i in range(len(data.columns)):
    Cols.append(data.columns[i].replace('-', ''))
data.columns = Cols
plt.figure(1)
df_data = {"age": 15, "NumberOfTime3059DaysPastDueNotWorse": 20}
df_data.age.plot.box()
Counter(df_data.age)
ind = np.where(df_data.age < 21)
df_data.age[ind[0]] = 21.
ind = np.where(df_data.age > 94)
df_data.age[ind[0]] = 94.
Counter(df_data.NumberOfTime3059DaysPastDueNotWorse)
# Set outlier values to median , that is 0.
ind = np.where(df_data.NumberOfTime3059DaysPastDueNotWorse > 95)
df_data.NumberOfTime3059DaysPastDueNotWorse[ind[0]] = 0.


plt.figure(figsize=(20, 15))
ax = plt.subplot(211)
# ax.set_ylim(0,20)
plt.plot(df_data.DebtRatio, 'bo', df_data.DebtRatio, 'k')
print('Median: %.7f \nMean: %.7f' %
      (np.median(df_data.DebtRatio), np.mean(df_data.DebtRatio)))
# ruoelLt2=len(df_data[df_data.RevolvingUtilizationOfUnsecuredLines < 2])
# ruoelACt=len(df_data.RevolvingUtilizationOfUnsecuredLines)
# print('Values less than 2 : %d in %d. Ratio: %.5f%%' %(ruoelLt2,ruoelACt,100*ruoelLt2/ruoelACt))
ax = sns.countplot(mad_based_outlier(df_data.DebtRatio))
plot_freq(l=len(df_data.DebtRatio))

minUpperBound = min([val for (val, out) in zip(
    df_data.DebtRatio, mad_based_outlier(df_data.DebtRatio)) if out == True])
# Set outlier values to upperbound, that is minUpperBound.
ind = np.where(df_data.DebtRatio > minUpperBound)
df_data.DebtRatio[ind[0]] = minUpperBound

plt.figure(figsize=(20, 15))
ax = plt.subplot(211)
plt.plot(df_data.DebtRatio, 'o')

df_data.DebtRatio.describe()

plt.figure(figsize=(20, 15))
ax = plt.subplot(211)
# ax.set_ylim(0,20)
plt.plot(df_data.MonthlyIncome, 'bo', df_data.MonthlyIncome, 'k')
print('Median: %.7f \nMean: %.7f' %
      (np.median(df_data.MonthlyIncome), np.mean(df_data.MonthlyIncome)))
maxUpperBound = min([val for (val, out) in zip(
    df_data.MonthlyIncome, mad_based_outlier(df_data.MonthlyIncome)) if out == True])
ind = np.where(df_data.MonthlyIncome > maxUpperBound)
df_data.MonthlyIncome[ind[0]] = maxUpperBound
ind = np.where(df_data.MonthlyIncome < 1500)
df_data.MonthlyIncome[ind[0]] = 1500
df_data.MonthlyIncome.describe()
Counter(df_data.NumberRealEstateLoansOrLines)
# Set outlier values to 16.
ind = np.where(df_data.NumberRealEstateLoansOrLines > 16)
df_data.NumberRealEstateLoansOrLines[ind[0]] = 16
Counter(df_data.NumberOfTime6089DaysPastDueNotWorse)
# Set outlier values to 0.
ind = np.where(df_data.NumberOfTime6089DaysPastDueNotWorse > 11)
df_data.NumberOfTime6089DaysPastDueNotWorse[ind[0]] = 0
Counter(df_data.NumberOfDependents)
ind = np.where(df_data.NumberOfDependents > 10)
df_data.NumberOfDependents[ind[0]] = 10


plt.style.use('ggplot')


form_item_layout = widgets.Layout(
    display='flex',
    flex_flow='row',
    justify_content='space-between'
)


# displaying the text widget
text = widgets.Text(
    placeholder='Enes',
    disabled=False
)
# display(text)
# add button that updates the graph based on the checkboxes
button = widgets.Button(description="Check credibility")
# display(button)
resultLabel = widgets.Label(
    value="",
    visible=False,
    disabled=True
)
# display(resultLabel)
revolve = widgets.FloatSlider(
    value=df_data.RevolvingUtilizationOfUnsecuredLines.median(),
    min=df_data.RevolvingUtilizationOfUnsecuredLines.min(),
    max=df_data.RevolvingUtilizationOfUnsecuredLines.max(),
    step=0.01,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.4f',
    slider_color='black'
)
age = widgets.IntSlider(
    value=df_data.age.median(),
    min=df_data.age.min(),
    max=df_data.age.max(),
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    slider_color='black'
)
income = widgets.FloatSlider(
    value=df_data.MonthlyIncome.median(),
    min=df_data.MonthlyIncome.min(),
    max=df_data.MonthlyIncome.max(),
    step=0.5,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
    slider_color='black'
)
debtRatio = widgets.FloatSlider(
    value=df_data.DebtRatio.median(),
    min=df_data.DebtRatio.min(),
    max=df_data.DebtRatio.max(),
    step=0.01,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.4f',
    slider_color='black'
)
NumberOfTime3059DaysPastDueNotWorse = widgets.IntSlider(
    value=df_data.NumberOfTime3059DaysPastDueNotWorse.median(),
    min=df_data.NumberOfTime3059DaysPastDueNotWorse.min(),
    max=df_data.NumberOfTime3059DaysPastDueNotWorse.max(),
    step=1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    slider_color='black'
)
NumberOfTimes90DaysLate = widgets.IntSlider(
    value=df_data.NumberOfTimes90DaysLate.median(),
    min=df_data.NumberOfTimes90DaysLate.min(),
    max=df_data.NumberOfTimes90DaysLate.max(),
    step=1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    slider_color='black'
)
NumberRealEstateLoansOrLines = widgets.IntSlider(
    value=df_data.NumberRealEstateLoansOrLines.median(),
    min=df_data.NumberRealEstateLoansOrLines.min(),
    max=df_data.NumberRealEstateLoansOrLines.max(),
    step=1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    slider_color='black'
)
NumberOfTime6089DaysPastDueNotWorse = widgets.IntSlider(
    value=df_data.NumberOfTime6089DaysPastDueNotWorse.median(),
    min=df_data.NumberOfTime6089DaysPastDueNotWorse.min(),
    max=df_data.NumberOfTime6089DaysPastDueNotWorse.max(),
    step=1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    slider_color='black'
)
NumberOfOpenCreditLinesAndLoans = widgets.IntSlider(
    value=df_data.NumberOfOpenCreditLinesAndLoans.median(),
    min=df_data.NumberOfOpenCreditLinesAndLoans.min(),
    max=df_data.NumberOfOpenCreditLinesAndLoans.max(),
    step=1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    slider_color='black'
)

NumberOfDependents = widgets.IntSlider(
    value=df_data.NumberOfDependents.median(),
    min=df_data.NumberOfDependents.min(),
    max=df_data.NumberOfDependents.max(),
    step=1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    slider_color='black'
)
algos = widgets.Dropdown(
    options=['Decision Tree', 'SVM', 'Logistic Regression', 'GaussianNB', 'MLP'])
# display(revolve)

form_items = [
    Box([Label(value='Please, enter the name:'), text], layout=form_item_layout),
    Box([Label(value='Revolving Util. of Unsecured Lines:'),
         revolve], layout=form_item_layout),
    Box([Label(value='Age:'), age], layout=form_item_layout),
    Box([Label(value='Monthly Income:'), income], layout=form_item_layout),
    Box([Label(value='Dept Ratio:'), debtRatio], layout=form_item_layout),
    Box([Label(value='NumberOfOpenCreditLinesAndLoans:'),
         NumberOfOpenCreditLinesAndLoans], layout=form_item_layout),
    Box([Label(value='NumberOfTime3059DaysPastDueNotWorse:'),
         NumberOfTime3059DaysPastDueNotWorse], layout=form_item_layout),
    Box([Label(value='NumberOfTimes90DaysLate:'),
         NumberOfTimes90DaysLate], layout=form_item_layout),
    Box([Label(value='NumberRealEstateLoansOrLines:'),
         NumberRealEstateLoansOrLines], layout=form_item_layout),
    Box([Label(value='NumberOfTime6089DaysPastDueNotWorse:'),
         NumberOfTime6089DaysPastDueNotWorse], layout=form_item_layout),
    Box([Label(value='NumberOfDependents:'),
         NumberOfDependents], layout=form_item_layout),
    Box([Label(value='Algorithm:'), algos], layout=form_item_layout),
    button,
    Box([Label(value='Result:'), resultLabel], layout=form_item_layout),
]

form = Box(form_items, layout=Layout(
    display='flex',
    flex_flow='column',
    border='dashed 2px',
    align_items='stretch',
    width='70%'
))

display(form)

# function to deal with the checkbox update button


def on_button_clicked(b):
    name = text.value
    roul = revolve.value
    ageV = age.value
    monI = income.value
    dratio = debtRatio.value
    noOpCL = NumberOfOpenCreditLinesAndLoans.value
    noT3059 = NumberOfTime3059DaysPastDueNotWorse.value
    noT90 = NumberOfTimes90DaysLate.value
    nreL = NumberRealEstateLoansOrLines.value
    noT6089 = NumberOfTime6089DaysPastDueNotWorse.value
    noD = NumberOfDependents.value
    algo = algos.value

    testARR = [[dratio, monI, noD, noOpCL,
                noT3059, noT6089, noT90, nreL, roul, ageV]]
    yGuess = []

    if algo == 'Decision Tree':
        yGuess = clf2.predict(testARR)
    elif algo == 'SVM':
        yGuess = clf3.predict(testARR)
    elif algo == 'Logistic Regression':
        yGuess = clf.predict(testARR)
    elif algo == 'GaussianNB':
        yGuess = gnb.predict(testARR)
    else:
        yGuess = clf4.predict(testARR)

    print(name, roul, ageV, monI, dratio, noOpCL, noT3059,
          noT90, nreL, noT6089, noD, algo, yGuess[0])

    if (resultLabel.visible == False and yGuess[0] == 0):
        resultLabel.value = text.value + ' can be provided with the loan.'
    else:
        resultLabel.value = text.value + ' should not be provided with the loan.'


button.on_click(on_button_clicked)
plt.show()

ind = df_data.SeriousDlqin2yrs[df_data.SeriousDlqin2yrs == 1]
ind = ind[1:100]
ind2 = df_data.SeriousDlqin2yrs[df_data.SeriousDlqin2yrs == 0]
ind2 = ind2[1:100]

plt.figure(figsize=(15, 15))
ax = plt.subplot(211)
# ax.set_ylim(0,20)
plt.plot(df_data.MonthlyIncome[ind.index], df_data.age[ind.index],
         'ko', df_data.MonthlyIncome[ind2.index], df_data.age)

# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_3.py
# 🔹 Analysis Result:
#   Standard => Credit Information Business Act B.E.2545
#   ⦿ Section: 3
#    ⁃ Count of standard compliance in the code block:
#      ◦ age: 14
#      ◦ NumberOfTime3059DaysPastDueNotWorse: 10
#      ◦ DebtRatio: 15
#      ◦ MonthlyIncome: 16
#      ◦ NumberRealEstateLoansOrLines: 10
#      ◦ NumberOfTime6089DaysPastDueNotWorse: 10
#      ◦ NumberOfDependents: 10
#      ◦ RevolvingUtilizationOfUnsecuredLines: 3
#      ◦ income: 3
#      ◦ debtRatio: 3
#      ◦ NumberOfOpenCreditLinesAndLoans: 7
#      ◦ Lines: 1
#      ◦ Age: 1
#      ◦ Income: 1
#      ◦ ageV: 3
#      ◦ loan: 2
#      Total: 109
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ Credit Information Business Act B.E.2545 at section 10
# 🔹 Reference Number: dbb813beb820f92dc84d74f5bee1b96ec320367e641e38cd8fa8c2ddd16bf9a6
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_3.py
# 🔹 Analysis Result:
#   1. Standard => Credit Information Business Act B.E.2545
#   ⦿ Section: 3
#    ⁃ Count of standard compliance in the code block:
#      ◦ age: 14
#      ◦ NumberOfTime3059DaysPastDueNotWorse: 10
#      ◦ DebtRatio: 15
#      ◦ MonthlyIncome: 16
#      ◦ NumberRealEstateLoansOrLines: 10
#      ◦ NumberOfTime6089DaysPastDueNotWorse: 10
#      ◦ NumberOfDependents: 10
#      ◦ RevolvingUtilizationOfUnsecuredLines: 3
#      ◦ income: 3
#      ◦ debtRatio: 3
#      ◦ NumberOfOpenCreditLinesAndLoans: 7
#      ◦ Lines: 1
#      ◦ Age: 1
#      ◦ Income: 1
#      ◦ ageV: 3
#      ◦ loan: 2
#      Total: 109
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ Credit Information Business Act B.E.2545 at section 10
# 🔹 Reference Number: be52a8d6e1daf9104a1715475cefb4bcdad5b5bf483e9a0019470e58477fd31c
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_3.py
# 🔹 Analysis Result:
#   1. Standard => ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Preparation of Credit Information no.8.2
#    ⁃ Count of standard compliance in the code block:
#      ◦ collections: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Credit Scoring Development
#    ⁃ Count of standard compliance in the code block:
#      ◦ data: 4
#      ◦ df_data: 79
#      Total: 83
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.6
#    ⁃ Count of standard compliance in the code block:
#      ◦ training: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.1
#    ⁃ Count of standard compliance in the code block:
#      ◦ training: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
#    ⁃ Count of standard compliance in the code block:
#      ◦ testARR: 6
#      Total: 6
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System I
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System II
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Verification of the Applicant’s Information
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.3
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Overrides in Credit Approval
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Construction of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Definition of Credit Scoring
# 🔹 Reference Number: dcdee9392d64ed729cc9eec3adf391899d18359c9b8529142cb09a1a506479ea
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_3.py
# 🔹 Analysis Result:
#   1. Standard => ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Preparation of Credit Information no.8.2
#    ⁃ Count of standard compliance in the code block:
#      ◦ collections: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Credit Scoring Development
#    ⁃ Count of standard compliance in the code block:
#      ◦ data: 4
#      ◦ df_data: 79
#      Total: 83
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.6
#    ⁃ Count of standard compliance in the code block:
#      ◦ training: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.1
#    ⁃ Count of standard compliance in the code block:
#      ◦ training: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
#    ⁃ Count of standard compliance in the code block:
#      ◦ testARR: 6
#      Total: 6
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System I
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System II
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Verification of the Applicant’s Information
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.3
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Overrides in Credit Approval
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Construction of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Definition of Credit Scoring
# 🔹 Reference Number: cd130dc26b4cd2d2225ef14cccc66c30a6339b4ca95c272129d9d184e48185b5

# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit_score_3.py
# 🔹 Analysis Result: 
#   1. Standard => Credit Information Business Act B.E.2545
#   ⦿ Section: 3
#    ⁃ Count of standard compliance in the code block: 
#      ◦ age: 15
#      ◦ NumberOfTime3059DaysPastDueNotWorse: 11
#      ◦ DebtRatio: 15
#      ◦ MonthlyIncome: 16
#      ◦ NumberRealEstateLoansOrLines: 10
#      ◦ NumberOfTime6089DaysPastDueNotWorse: 10
#      ◦ NumberOfDependents: 10
#      ◦ RevolvingUtilizationOfUnsecuredLines: 3
#      ◦ income: 3
#      ◦ debtRatio: 3
#      ◦ NumberOfOpenCreditLinesAndLoans: 7
#      ◦ Lines: 1
#      ◦ Age: 1
#      ◦ Income: 1
#      ◦ ageV: 3
#      ◦ loan: 2
#      Total: 111
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block: 
#  ◦ Credit Information Business Act B.E.2545 at section 10
# 🔹 Reference Number: 6a8b835ae4287573549b7f96bcc2808de12e740254617b925132607e3abe4b79