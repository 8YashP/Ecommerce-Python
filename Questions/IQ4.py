# Identify the correlation between product price and the number of times a product has been purchased.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''SELECT P.PRODUCT_CATEGORY,COUNT(OI.PRODUCT_ID) AS ORDER_COUNT,ROUND(AVG(OI.PRICE),2) AS PRICE
           FROM PRODUCTS P, ORDER_ITEMS OI
           WHERE P.PRODUCT_ID = OI.PRODUCT_ID
           GROUP BY P.PRODUCT_CATEGORY'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data, columns = ["Product_Category","Order_Count","Avg_Price"])

arr1 = df["Order_Count"]
arr2 = df["Avg_Price"]

y = SQL.np.corrcoef([arr1,arr2])

print(data)

print(y)

# print(df)