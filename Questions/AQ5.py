# Identify the top 3 customers who spent the most money in each year.

import MySqlConnect as SQL

cur = SQL.db.cursor()

query = '''
        SELECT *
        FROM (
        SELECT YEAR(O.ORDER_PURCHASE_TIMESTAMP) AS YEAR, O.CUSTOMER_ID, ROUND(SUM(P.PAYMENT_VALUE),2) AS AMOUNT,
        DENSE_RANK() OVER (PARTITION BY YEAR(O.ORDER_PURCHASE_TIMESTAMP) ORDER BY SUM(P.PAYMENT_VALUE) DESC) AS D_RANK
        FROM ORDERS O, PAYMENTS P
        WHERE O.ORDER_ID = P.ORDER_ID
        GROUP BY
        YEAR(O.ORDER_PURCHASE_TIMESTAMP), O.CUSTOMER_ID) A
        WHERE D_RANK <= 3
        '''

cur.execute(query)

data = cur.fetchall()

# print(data)

df = SQL.pd.DataFrame(data, columns = ["Year","Customer_ID","Amount","Rank"])

SQL.sns.barplot(x = "Customer_ID", y = "Amount", data = df, hue = "Year")

SQL.plt.xticks(rotation = 90)

SQL.plt.show()

print(df)