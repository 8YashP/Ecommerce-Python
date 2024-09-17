# Calculate the percentage of total revenue contributed by each product category.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''SELECT P.PRODUCT_CATEGORY,ROUND((SUM(PA.PAYMENT_VALUE)/(SELECT SUM(PAYMENT_VALUE) FROM PAYMENTS))*100,2) AS PERCENTAGE
           FROM PRODUCTS P, ORDER_ITEMS OI, PAYMENTS PA
           WHERE P.PRODUCT_ID = OI.PRODUCT_ID AND OI.ORDER_ID = PA.ORDER_ID
           GROUP BY P.PRODUCT_CATEGORY
           ORDER BY PERCENTAGE DESC'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data, columns = ["Product Category","Percentage"])

print(df)