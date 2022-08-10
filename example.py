import sqlite3
import time
import datetime
import random
 
conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()
 
def create_table():
  c.execute("CREATE TABLE IF NOT EXISTS tabla1(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")
 
def data_entry():
  c.execute("INSERT INTO tabla1 VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
 
  conn.commit()
  c.close()
  conn.close()
 
def dynamic_data_entry():
 
  unix = int(time.time())
  date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
  keyword = 'Python'
  value = random.randrange(0,10)
 
  c.execute("INSERT INTO tabla1(unix, fecha, palabraclave, valor) VALUES (?, ?, ?, ?)",(unix, date, keyword, value))
 
  conn.commit()
 
for i in range(10):
  dynamic_data_entry()
  time.sleep(1)