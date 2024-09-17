# Calculate the percentage of orders that were paid in installments.

import MySqlConnect as MySqlConnect

cur = MySqlConnect.db.cursor()

query = '''SELECT 
           ROUND(((COUNT(CASE WHEN PAYMENT_INSTALLMENTS >= 1 THEN 1 END))/COUNT(*))*100,3)
           FROM PAYMENTS'''

cur.execute(query)

data = cur.fetchall()

print(f"Percentage of orders which were paid in installment was :: {data[0][0]} %")