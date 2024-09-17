# Identify the correlation between product price and the number of times a product has been purchased.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''SELECT OI.SELLER_ID,ROUND(SUM(P.PAYMENT_VALUE),2) AS PRICE,
           DENSE_RANK() OVER(ORDER BY SUM(P.PAYMENT_VALUE) DESC)
           FROM ORDER_ITEMS OI, PAYMENTS P
           WHERE OI.ORDER_ID = P.ORDER_ID
           GROUP BY OI.SELLER_ID'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data, columns = ["Seller_Id","Revnue","Rank"])

print(df)