import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'working.......!'

@app.route('/dbinit')
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS m_test_db")
  cursor.execute("CREATE DATABASE m_test_db")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="m_test_db"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS m_test_table")
  cursor.execute("CREATE TABLE m_test_table (name VARCHAR(255), description VARCHAR(255))")
  sql = "INSERT INTO m_test_table VALUES (%s, %s)"
  val1 = ('item1', 'test1')
  val2 = ('item2', 'test2')
  cursor.execute(sql, val1)
  cursor.execute(sql, val2)
  cursor.close()
  mydb.commit()

  return 'init database'

@app.route('/getdata')
def get_widgets():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="m_test_db"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM m_test_table")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

if __name__ == "__main__":
  app.run(host ='0.0.0.0')
