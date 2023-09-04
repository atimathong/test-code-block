import numpy as np  # linear algebra
import os
import scipy.stats as stats  # scientific computing tools
import matplotlib.pyplot as plt  # plots and visualization
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.metrics import silhouette_samples, silhouette_score
import warnings

data = pd.read_csv(
    "/kaggle/input/lending-club-dataset/lending_club_loan_two.csv")
data.head()

data.groupby(by='loan_status')['loan_amnt'].describe()
print(f"GRADE unique: {data.grade.unique()}")
print(f"SUB_GRADE unique: {data.sub_grade.unique()}")

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
grade = sorted(data.grade.unique().tolist())
sns.countplot(x='grade', data=data, hue='loan_status', order=grade)

plt.subplot(2, 2, 2)
sub_grade = sorted(data.sub_grade.unique().tolist())
g = sns.countplot(x='sub_grade', data=data, hue='loan_status', order=sub_grade)
g.set_xticklabels(g.get_xticklabels(), rotation=90)

df = data[(data.grade == 'F') | (data.grade == 'G')]

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
grade = sorted(df.grade.unique().tolist())
sns.countplot(x='grade', data=df, hue='loan_status', order=grade)

plt.subplot(2, 2, 2)
sub_grade = sorted(df.sub_grade.unique().tolist())
sns.countplot(x='sub_grade', data=df, hue='loan_status', order=sub_grade)

data['home_ownership'].value_counts()


data.loc[(data.home_ownership == 'ANY') | (
    data.home_ownership == 'NONE'), 'home_ownership'] = 'OTHER'
data.home_ownership.value_counts()
plt.figure(figsize=(15, 20))

plt.subplot(4, 2, 1)
sns.countplot(x='term', data=data, hue='loan_status')

plt.subplot(4, 2, 2)
sns.countplot(x='home_ownership', data=data, hue='loan_status')

plt.subplot(4, 2, 3)
sns.countplot(x='verification_status', data=data, hue='loan_status')

plt.subplot(4, 2, 4)
g = sns.countplot(x='purpose', data=data, hue='loan_status')
g.set_xticklabels(g.get_xticklabels(), rotation=90)
data.loc[data['home_ownership'] == 'OTHER', 'loan_status'].value_counts()
data.loc[data.annual_inc >= 1000000, 'loan_status'].value_counts()
plt.figure(figsize=(15, 12))

plt.subplot(2, 2, 1)
order = ['< 1 year', '1 year', '2 years', '3 years', '4 years', '5 years',
         '6 years', '7 years', '8 years', '9 years', '10+ years',]
g = sns.countplot(x='emp_length', data=data, hue='loan_status', order=order)
g.set_xticklabels(g.get_xticklabels(), rotation=90)

plt.subplot(2, 2, 2)
plt.barh(data.emp_title.value_counts()[
         :30].index, data.emp_title.value_counts()[:30])
plt.title("The most 30 jobs title afforded a loan")
plt.tight_layout()
data.loc[data['dti'] >= 50, 'loan_status'].value_counts()


def pub_rec(number):
    if number == 0.0:
        return 0
    else:
        return 1


def mort_acc(number):
    if number == 0.0:
        return 0
    elif number >= 1.0:
        return 1
    else:
        return number


def pub_rec_bankruptcies(number):
    if number == 0.0:
        return 0
    elif number >= 1.0:
        return 1
    else:
        return number


data['pub_rec'] = data.pub_rec.apply(pub_rec)
data['mort_acc'] = data.mort_acc.apply(mort_acc)
data['pub_rec_bankruptcies'] = data.pub_rec_bankruptcies.apply(
    pub_rec_bankruptcies)
plt.figure(figsize=(12, 30))

plt.subplot(6, 2, 1)
sns.countplot(x='pub_rec', data=data, hue='loan_status')

plt.subplot(6, 2, 2)
sns.countplot(x='initial_list_status', data=data, hue='loan_status')

plt.subplot(6, 2, 3)
sns.countplot(x='application_type', data=data, hue='loan_status')

plt.subplot(6, 2, 4)
sns.countplot(x='mort_acc', data=data, hue='loan_status')

plt.subplot(6, 2, 5)
sns.countplot(x='pub_rec_bankruptcies', data=data, hue='loan_status')
dummies = ['sub_grade', 'verification_status', 'purpose', 'initial_list_status',
           'application_type', 'home_ownership']
data = pd.get_dummies(data, columns=dummies, drop_first=True)

w_p = data.loan_status.value_counts()[0] / data.shape[0]
w_n = data.loan_status.value_counts()[1] / data.shape[0]

print(f"Weight of positive values {w_p}")
print(f"Weight of negative values {w_n}")

# 🔵 Standard Compliance Report
# 🔹 Product Type: Peer-to-Peer Lending
# 🔹 Code Block Name: peer_to_peer.py
# 🔹 Analysis Result: 
#   Standard => Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending
#   ⦿ Section: Attachment3: Information Disclosure
#    ⁃ Count of standard compliance in the code block: 
#      ◦ matplotlib: 2
#      ◦ pyplot: 2
#      ◦ plots: 1
#      ◦ subplot: 15
#      ◦ countplot: 14
#      ◦ application_type: 2
#      Total: 36
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Conditions for business operation
#    ⁃ Count of standard compliance in the code block: 
#      ◦ lending: 1
#      ◦ lending_club_loan_two: 1
#      Total: 2
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Definition
#    ⁃ Count of standard compliance in the code block: 
#      ◦ application_type: 2
#      Total: 2
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block: 
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment1: Management and Work System
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment1: Management and Work System
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment1: Management and Work System
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment1: Management and Work System
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment1: Management and Work System
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment1: Management and Work System
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment4: Additional Regulations on Market Conduct Management
#  ◦ Notification of the Bank of Thailand No. FPG. 14/2563 Re: Prescription of Rules, Procedures and Conditions for Operating an Electronic System or Network Business for Peer-to-Peer Lending at section Attachment1: Management and Work System
# 🔹 Create Date: Mon, 04 Sep 2023 17:54:00 GMT
# 🔹 Reference Number: b8f8b6317488fccf9ea25a22cdad742a945612579abae3936673391bf1c06da8