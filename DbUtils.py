__author__ = 'ge'
import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
    'port':3307,
  'raise_on_warnings': True,
}


cnx = mysql.connector.connect(**config)
cnx.database="DianPingHui"

cur = cnx.cursor(buffered=True)

cur.execute("show create table HUI_CouponOffer")
result = cur.fetchone()
# can get the column and it's value
print(cur.column_names)
print(result)
cur.close()
cnx.close()


