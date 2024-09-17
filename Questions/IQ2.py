# Find the average number of products per order, grouped by customer city.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''WITH ORDER_COUNT AS (
           SELECT OI.ORDER_ID,O.CUSTOMER_ID,COUNT(OI.ORDER_ID) AS CNT
           FROM ORDER_ITEMS OI, ORDERS O
           WHERE OI.ORDER_ID = O.ORDER_ID
           GROUP BY OI.ORDER_ID,O.CUSTOMER_ID)
           SELECT  CUSTOMER_CITY,ROUND(AVG(OC.CNT),2)
           FROM ORDER_COUNT OC, CUSTOMERS C
           WHERE OC.CUSTOMER_ID = C.CUSTOMER_ID
           GROUP BY C.CUSTOMER_CITY'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data, columns = ["City","Count"])

print(df)