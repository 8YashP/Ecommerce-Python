# Find the total sales per category.

import MySqlConnect as MySqlConnect

cur = MySqlConnect.db.cursor()

query = '''SELECT PR.PRODUCT_CATEGORY,ROUND(SUM(P.PAYMENT_VALUE),2) AS PRICE
           FROM PAYMENTS P, ORDER_ITEMS OI, PRODUCTS PR
           WHERE P.ORDER_ID = OI.ORDER_ID AND OI.PRODUCT_ID = PR.PRODUCT_ID
           GROUP BY PR.PRODUCT_CATEGORY'''

cur.execute(query)

data = cur.fetchall()

print(data)

# df = MySqlConnect.pd.DataFrame(data,columns = ["Category","Sales"])

# print(df)

# for category in data:
#     for item in category:
#         print(item)