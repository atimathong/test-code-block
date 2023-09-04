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


def customer_segmentation(data):
    abc = np
    aa = np.big()
    for col in data.select_dtypes(include=[object]):
        print(col, ":", data[col].unique())

    h = "Sex"
    pal = None
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))
    sns.scatterplot(x="Credit amount", y="Duration",
                    hue=h, palette=pal, data=data, ax=ax1)
    sns.scatterplot(x="Age", y="Credit amount", hue=h,
                    palette=pal, data=data, ax=ax2)
    sns.scatterplot(x="Age", y="Duration", hue=h,
                    palette=pal, data=data, ax=ax3)
    plt.tight_layout()

    # Selecting columns for clusterisation with k-means
    selected_cols = ["Age", "Credit amount", "Duration"]
    cluster_data = data.loc[:, selected_cols]
    cluster_log = np.log(cluster_data)
    scaler = StandardScaler()
    cluster_scaled = scaler.fit_transform(cluster_log)

    clusters_range = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    inertias = []

    for c in clusters_range:
        kmeans = KMeans(n_clusters=c, random_state=0).fit(cluster_scaled)
        inertias.append(kmeans.inertia_)

    plt.figure()
    plt.plot(clusters_range, inertias, marker='o')

    clusters_range = range(2, 15)
    random_range = range(0, 20)
    results = []
    for c in clusters_range:
        for r in random_range:
            clusterer = KMeans(n_clusters=c, random_state=r)
            cluster_labels = clusterer.fit_predict(cluster_scaled)
            silhouette_avg = silhouette_score(cluster_scaled, cluster_labels)
            results.append([c, r, silhouette_avg])

    result = pd.DataFrame(
        results, columns=["n_clusters", "seed", "silhouette_score"])
    pivot_km = pd.pivot_table(
        result, index="n_clusters", columns="seed", values="silhouette_score")

    kmeans_sel = KMeans(n_clusters=3, random_state=1).fit(cluster_scaled)
    labels = pd.DataFrame(kmeans_sel.labels_)
    clustered_data = cluster_data.assign(Cluster=labels)

    data.groupby(by='loan_status')['loan_amnt'].describe()

    pd.set_option('mode.chained_assignment', None)

    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))

    df = pd.read_csv(
        '/kaggle/input/bank-customer-segmentation/bank_transactions.csv')

    # Showing preview of the Data (top 5 rows)
    df.head()

    # Convert the data type
    df['CustomerDOB'] = pd.to_datetime(
        df['CustomerDOB'], format='%d/%m/%y', errors='coerce')
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

    # Check the data information again
    df.info()
    # Null and Not-Null Comparison
    pd.DataFrame({
        'null-count': df.isna().sum(),
        'not-null-count': df.notna().sum(),
        'pct-null': df.isna().sum()/len(df)*100
    })
    # Drop the rows that have missing values in 'CustAccountBalance' column
    df.dropna(subset=['CustAccountBalance'], inplace=True)
    # Number Comparison of Unique Values and Total Count of each column
    pd.DataFrame({
        'unique_count': df.nunique(),
        'rows_count': df.count()
    })
    # Descriptive Statistics for datetime variables
    pd.DataFrame({
        'CustomerDOB': df['CustomerDOB'].describe(datetime_is_numeric=True),
        'TransactionDate': df['TransactionDate'].describe(datetime_is_numeric=True)
    })
    # Descriptive Statistics for 'CustomerDOB' anomaly data
    df['CustomerDOB'][df['CustomerDOB'] > max(
        df['TransactionDate'])].describe(datetime_is_numeric=True)
    # Histogram of 'CustomerDOB' column
    plt.hist(df['CustomerDOB'])
    plt.xlabel('Customer DOB')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customer DOB')
    plt.show()

    # Replace the anomaly 'CustomerDOB' with the median value of 'CustomerDOB' (1989-01-01)
    df['CustomerDOB'][df['CustomerDOB'] > max(
        df['TransactionDate'])] = pd.to_datetime('1988-08-06 00:00:00')

    # Verify that the anomaly data have been replaced
    df[df['CustomerDOB'] > max(df['TransactionDate'])]

    # Histogram of CustAccountBalance column
    log_balance = np.log1p(df['CustAccountBalance'])

    plt.hist(log_balance, bins=50, density=True, alpha=0.7)
    plt.xlabel('Logarithm of Transaction Amount (INR)')
    plt.ylabel('Probability Density')
    plt.title('Distribution of Log-transformed Customer Account Balance')
    x = np.linspace(log_balance.min(), log_balance.max(), 100)
    dist = stats.norm(log_balance.mean(), log_balance.std())
    plt.plot(x, dist.pdf(x), color='red', label='PDF')
    plt.legend()
    plt.show()

    # Bar Plot for 'CustGender' column
    gender_counts = df['CustGender'].value_counts()
    plt.bar(gender_counts.index, gender_counts.values)
    plt.xlabel('CustGender')
    plt.ylabel('Count')
    plt.title('Distribution of CustGender')

    # Add labels to the bars
    for i, count in enumerate(gender_counts.values):
        plt.text(i, count, str(count), ha='center', va='bottom')

    plt.show()
    # Replace the anomaly 'CustomerDOB' with the most frequent CustomerDOB (1989-01-01)
    df['CustGender'][df['CustGender'] == 'T'] = 'M'

    # Verify that the data have been replaced
    df['CustGender'].value_counts()

    # Grouping TransactionDate column to YearMonth
    df['YearMonth'] = df['TransactionDate'].dt.to_period('M').astype(str)
    transactions_count = df.groupby('YearMonth')['TransactionID'].count()

    plt.plot(transactions_count.index, transactions_count.values)
    plt.xlabel('Year-Month')
    plt.ylabel('Transaction Frequency')
    plt.title('Transaction Frequency over Time (Year-Month)')
    plt.xticks(rotation=45)
    plt.show()
    # Time series plot for transactions amount over time (year-month)
    monthly_trx_amount = df.groupby(
        'YearMonth')['TransactionAmount (INR)'].sum()
    plt.plot(monthly_trx_amount.index, monthly_trx_amount.values)
    plt.xlabel('Year-Month')
    plt.ylabel('TransactionAmount (INR)')
    plt.title('Transaction Amount over Time (Year-Month)')
    plt.xticks(rotation=45)
    plt.show()
    # Detailed Table of Transaction Happened
    transactions_count.reset_index().rename(columns={'TransactionID': 'TransactionCount'}).merge(
        monthly_trx_amount.reset_index().rename(columns={'TransactionAmount (INR)': 'TotalMonetaryAmount'}), on='YearMonth')
    # Set 'today' variable
    today = max(df['TransactionDate'])
    # Creating 'dfUser' table
    dfUser = df.groupby('CustomerID', as_index=False).agg(TransactionCount=('TransactionID', 'nunique'), LastTransactionDate=(
        'TransactionDate', 'max'), TotalTransactionValue=('TransactionAmount (INR)', 'sum'))
    dfUser.head()
    dfUser['DaySinceLastTransaction'] = (
        today - dfUser['LastTransactionDate']).dt.days
    dfUser.head()
# Reindex 'dfUser columns'
    dfUser = dfUser.reindex(columns=[
        'CustomerID', 'DaySinceLastTransaction', 'TransactionCount', 'TotalTransactionValue'])
    dfUser.head()
# Data Binning for Recency Score
    dfUser['Recency Score'] = pd.qcut(
        dfUser['DaySinceLastTransaction'], 5, labels=[5, 4, 3, 2, 1])
# Data Binning for Frequency Score
    dfUser['Frequency Score'] = pd.cut(dfUser['TransactionCount'], bins=[
        0, 2, 4, dfUser['TransactionCount'].max()+1], labels=[1, 2, 3])
# Data Binning for Monetary Score
    dfUser['Monetary Score'] = pd.qcut(
        dfUser['TotalTransactionValue'], 5, labels=[1, 2, 3, 4, 5])

    dfUser.head()
# Make a 'RFM_Score' column to make the segmentation easier
    dfUser['RFM_Score'] = (dfUser['Recency Score'].astype(
        str)) + (dfUser['Frequency Score'].astype(str)) + (dfUser['Monetary Score'].astype(str))
    dfUser.head()
# User Segmentation
    segment_map = {
        r'[4-5]3.': 'High Recency, High Frequency',
        r'[4-5]2.': 'High Recency, Medium Frequency',
        r'[4-5]1.': 'High Recency, Low Frequency',
        r'[2-3]3.': 'Medium Recency, High Frequency',
        r'[2-3]2.': 'Medium Recency, Medium Frequency',
        r'[2-3]1.': 'Medium Recency, Low Frequency',
        r'13.': 'Low Recency, High Frequency',
        r'12.': 'Low Recency, Medium Frequency',
        r'11.': 'Low Recency, Low Frequency'
    }

    dfUser['Customer Segment'] = dfUser['RFM_Score'].replace(
        segment_map, regex=True)
    dfUser.head()
    segment_counts = dfUser['Customer Segment'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(segment_counts.index, segment_counts.values)
    plt.xlabel('Customer Segment')
    plt.ylabel('Count')
    plt.title('Distribution of Customer Segments')
    plt.xticks(rotation=90)

    for i, count in enumerate(segment_counts.values):
        plt.text(i, count, str(count), ha='center', va='bottom')

    plt.show()


# 🔵 Standard Compliance Report
# 🔹 Product Type: Customer Segmentation
# 🔹 Code Block Name: customer_segment1.py
# 🔹 Analysis Result:
#   1. Standard => Bank of Thailand Notification No. SVG. 1/2561
# Re: Regulations on Market Conduct
#   ⦿ Section: Management systems: Product development and client segmentation
#    ⁃ Count of standard compliance in the code block:
#      ◦ customer_segmentation: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block: 0
# 🔹 Reference Number: 0c63a6c38bf978e6077eaebe661fbbc5ae09fe9a62487776c1ea51ae106b2c64

# 🔵 Standard Compliance Report
# 🔹 Product Type: Customer Segmentation
# 🔹 Code Block Name: customer_segment1.py
# 🔹 Analysis Result: 
#   Standard => Bank of Thailand Notification No. SVG. 1/2561 Re: Regulations on Market Conduct
#   ⦿ Section: Attachment4: Minimum standards on sales process
#    ⁃ Count of standard compliance in the code block: 
#      ◦ customer_segmentation: 1
#      ◦ loan_status: 1
#      ◦ loan_amnt: 1
#      ◦ segmentation: 1
#      ◦ bank_transactions: 1
#      ◦ TransactionDate: 10
#      ◦ CustAccountBalance: 2
#      ◦ Transaction: 4
#      ◦ gender_counts: 4
#      ◦ CustGender: 6
#      ◦ transactions_count: 4
#      ◦ TransactionID: 3
#      ◦ TransactionAmount: 4
#      ◦ TransactionCount: 5
#      ◦ LastTransactionDate: 2
#      ◦ TotalTransactionValue: 3
#      ◦ DaySinceLastTransaction: 3
#      ◦ Age: 3
#      Total: 58
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Management systems: Product development and client segmentation
#    ⁃ Count of standard compliance in the code block: 
#      ◦ customer_segmentation: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block: 
#  ◦ Bank of Thailand Notification No. SVG. 1/2561 Re: Regulations on Market Conduct at section Attachment6: Minimum standards on data privacy
#  ◦ Bank of Thailand Notification No. SVG. 1/2561 Re: Regulations on Market Conduct at section Attachment2: Minimum standards on product development and client segmentation
#  ◦ Bank of Thailand Notification No. SVG. 1/2561 Re: Regulations on Market Conduct at section Management systems: Data Privacy
#  ◦ Bank of Thailand Notification No. SVG. 1/2561 Re: Regulations on Market Conduct at section Attachment6: Minimum standards on data privacy
#  ◦ Bank of Thailand Notification No. SVG. 1/2561 Re: Regulations on Market Conduct at section Attachment6: Minimum standards on data privacy
# 🔹 Create Date: Mon, 04 Sep 2023 13:22:20 GMT
# 🔹 Reference Number: 87e3fad47c599253079459f42752ebebc8447a8eec9d36cc0a1d78afeeffbe7d