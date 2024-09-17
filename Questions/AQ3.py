# Calculate the year-over-year growth rate of total sales.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''
        SELECT
        YEAR, PAYMENT, LAG(PAYMENT) OVER (ORDER BY YEAR) AS PRE,
        ROUND((((PAYMENT - (LAG(PAYMENT) OVER (ORDER BY YEAR))) / (LAG(PAYMENT) OVER (ORDER BY YEAR))) * 100),2)
        FROM (
        SELECT YEAR(O.ORDER_PURCHASE_TIMESTAMP) AS YEAR,
        ROUND(SUM(P.PAYMENT_VALUE),2) AS PAYMENT
        FROM ORDERS O, PAYMENTS P
        WHERE O.ORDER_ID = P.ORDER_ID
        GROUP BY YEAR
        ORDER BY YEAR) A'''

cur.execute(query)

data = cur.fetchall()

# print(data)

df = SQL.pd.DataFrame(data, columns = ["Year","Payment","Pre","Lag"])

print(df)