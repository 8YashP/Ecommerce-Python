# Calculate the number of orders per month in 2018.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''SELECT MONTHNAME(ORDER_PURCHASE_TIMESTAMP),COUNT(ORDER_ID) 
           FROM ORDERS 
           WHERE YEAR(ORDER_PURCHASE_TIMESTAMP) = 2018
           GROUP BY MONTHNAME(ORDER_PURCHASE_TIMESTAMP),MONTH(ORDER_PURCHASE_TIMESTAMP)
           ORDER BY MONTH(ORDER_PURCHASE_TIMESTAMP) ASC'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data,columns = ["Month","Count"])

ax = SQL.sns.barplot(x = df["Month"], y = df["Count"], data = df)

SQL.plt.xticks(rotation = 45)

ax.bar_label(ax.containers[0])

SQL.plt.title("Number of orders per month in 2018")

print(df)

SQL.plt.show()

# print(data)