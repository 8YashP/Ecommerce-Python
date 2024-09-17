# Calculate the moving average of order values for each customer over their order history.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''SELECT CUSTOMER_ID,ORDER_PURCHASE_TIMESTAMP,PAYMENT_VALUE,
           ROUND(AVG(PAYMENT_VALUE) OVER (PARTITION BY CUSTOMER_ID ORDER BY ORDER_PURCHASE_TIMESTAMP ROWS BETWEEN 2 PRECEDING AND CURRENT ROW),2) AS MOV_AVG
           FROM (
           SELECT OI.CUSTOMER_ID,OI.ORDER_PURCHASE_TIMESTAMP,P.PAYMENT_VALUE
           FROM PAYMENTS P, ORDERS OI
           WHERE P.ORDER_ID = OI.ORDER_ID) A'''

cur.execute(query)

data = cur.fetchall()

df = SQL.pd.DataFrame(data, columns = ["CUSTOMER_ID","PURCHASE_TIME","PAYMENT","MOV_AVG"])

print(df)