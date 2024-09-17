# Count the number of customers from each state.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''SELECT CUSTOMER_STATE,COUNT(CUSTOMER_ID) AS CUST_COUNT FROM CUSTOMERS
           GROUP BY CUSTOMER_STATE ORDER BY COUNT(CUSTOMER_ID) DESC'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data,columns = ["State","Count"])

print(df)

SQL.plt.bar(df["State"],df["Count"])

SQL.plt.show()

# print(data)