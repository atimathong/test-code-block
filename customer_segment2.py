unique_desc = cs_df[["StockCode", "Description"]].groupby(by=["StockCode"]).\
    apply(pd.DataFrame.mode).reset_index(drop=True)
q = '''
select df.InvoiceNo, df.StockCode, un.Description, df.Quantity, df.InvoiceDate,
       df.UnitPrice, df.CustomerID, df.Country
from cs_df as df INNER JOIN 
     unique_desc as un on df.StockCode = un.StockCode
'''

cs_df = pysqldf(q)
fig = plt.figure(figsize=(25, 7))
f1 = fig.add_subplot(121)
g = cs_df.groupby(["Country"]).amount.sum().sort_values(
    ascending=False).plot(kind='bar', title='Amount Sales by Country')
cs_df['Internal'] = cs_df.Country.apply(
    lambda x: 'Yes' if x == 'United Kingdom' else 'No')
f2 = fig.add_subplot(122)
market = cs_df.groupby(["Internal"]).amount.sum().sort_values(ascending=False)
g = plt.pie(market, labels=market.index,
            autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Internal Market')
plt.show()

fig = plt.figure(figsize=(25, 7))
PercentSales = np.round((cs_df.groupby(["CustomerID"]).amount.sum().
                         sort_values(ascending=False)[:51].sum()/cs_df.groupby(["CustomerID"]).
                         amount.sum().sort_values(ascending=False).sum()) * 100, 2)
g = cs_df.groupby(["CustomerID"]).amount.sum().sort_values(ascending=False)[:51].\
    plot(kind='bar', title='Top Customers: {:3.2f}% Sales Amount'.format(
        PercentSales))

fig = plt.figure(figsize=(25, 7))
f1 = fig.add_subplot(121)
PercentSales = np.round((cs_df.groupby(["CustomerID"]).amount.sum().
                         sort_values(ascending=False)[:10].sum()/cs_df.groupby(["CustomerID"]).
                         amount.sum().sort_values(ascending=False).sum()) * 100, 2)
g = cs_df.groupby(["CustomerID"]).amount.sum().sort_values(ascending=False)[:10]\
    .plot(kind='bar', title='Top 10 Customers: {:3.2f}% Sales Amont'.format(PercentSales))
f1 = fig.add_subplot(122)
PercentSales = np.round((cs_df.groupby(["CustomerID"]).amount.count().
                         sort_values(ascending=False)[:10].sum()/cs_df.groupby(["CustomerID"]).
                         amount.count().sort_values(ascending=False).sum()) * 100, 2)
g = cs_df.groupby(["CustomerID"]).amount.count().sort_values(ascending=False)[:10].\
    plot(kind='bar', title='Top 10 Customers: {:3.2f}% Event Sales'.format(
        PercentSales))
refrence_date = cs_df.InvoiceDate.max() + datetime.timedelta(days=1)
print('Reference Date:', refrence_date)
cs_df['days_since_last_purchase'] = (
    refrence_date - cs_df.InvoiceDate).astype('timedelta64[D]')
customer_history_df = cs_df[['CustomerID', 'days_since_last_purchase']].groupby(
    "CustomerID").min().reset_index()
customer_history_df.rename(
    columns={'days_since_last_purchase': 'recency'}, inplace=True)
customer_history_df.describe().transpose()
support = 0.01
print("num of required transactions = ", int(
    input_assoc_rules.shape[0]*support))
num_trans = input_assoc_rules.shape[0]*support
itemsets = dict(frequent_itemsets(data_tran_en, support))
print('Items Set Size:', len(itemsets))
