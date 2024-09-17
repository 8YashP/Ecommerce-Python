# Count the number of orders placed in 2017.

import MySqlConnect as MySqlConnect

cur = MySqlConnect.db.cursor()

query = '''SELECT COUNT(ORDER_ID) FROM ORDERS WHERE YEAR(ORDER_PURCHASE_TIMESTAMP) = 2017'''

cur.execute(query)

data = cur.fetchall()

print(f"Total Orders Placed in 2017 is :: {data[0][0]}")