# Calculate the retention rate of customers, defined as the percentage of customers who make another purchase within 6 months of their first purchase.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''
        WITH A AS (
        SELECT C.CUSTOMER_ID,MIN(O.ORDER_PURCHASE_TIMESTAMP) AS FIRST_ORDER
        FROM CUSTOMERS C, ORDERS O
        WHERE C.CUSTOMER_ID = O.CUSTOMER_ID
        GROUP BY C.CUSTOMER_ID),
        B AS (
        SELECT A.CUSTOMER_ID, COUNT(DISTINCT O.ORDER_PURCHASE_TIMESTAMP) AS NEXT_ORDER
        FROM A, ORDERS O
        WHERE O.CUSTOMER_ID = A.CUSTOMER_ID
        AND O.ORDER_PURCHASE_TIMESTAMP > A.FIRST_ORDER
        AND O.ORDER_PURCHASE_TIMESTAMP < DATE_ADD(FIRST_ORDER,INTERVAL 6 MONTH)
        GROUP BY A.CUSTOMER_ID
        )
        SELECT 100 * (COUNT(DISTINCT A.CUSTOMER_ID)/COUNT(DISTINCT B.CUSTOMER_ID))
        FROM A,B
        WHERE A.CUSTOMER_ID = B.CUSTOMER_ID
        '''

cur.execute(query)

data = cur.fetchall()

print(data[0][0])

# df = SQL.pd.DataFrame(data, columns = ["Year","Payment","Pre","Lag"])

# print(df)