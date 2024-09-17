# Calculate the cumulative sales per month for each year.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''SELECT YEAR,MONTH,PAYMENT,
           ROUND(SUM(PAYMENT) OVER (ORDER BY YEAR,MONTH),2) AS CUMULATIVE_SALES 
           FROM (
           SELECT YEAR(O.ORDER_PURCHASE_TIMESTAMP) AS YEAR, MONTH(O.ORDER_PURCHASE_TIMESTAMP) AS MONTH,
           ROUND(SUM(P.PAYMENT_VALUE),2) AS PAYMENT
           FROM ORDERS O, PAYMENTS P
           WHERE O.ORDER_ID = P.ORDER_ID
           GROUP BY YEAR,MONTH
           ORDER BY YEAR,MONTH) A'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data, columns = ["CUSTOMER_ID","PURCHASE_TIME","PAYMENT","MOV_AVG"])

print(df)