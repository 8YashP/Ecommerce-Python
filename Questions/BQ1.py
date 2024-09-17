# List all unique cities where customers are located.

import MySqlConnect as MySqlConnect

cur = MySqlConnect.db.cursor()

query = '''SELECT DISTINCT CUSTOMER_CITY FROM CUSTOMERS'''

cur.execute(query)

data = cur.fetchall()

for city in data:
    for item in city:
        print(item)

# print(data)