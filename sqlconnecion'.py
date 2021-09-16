
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database = "nanda"
)

print(mydb)

cursor = mydb.cursor()
#cursor.execute("select * from student")
#result = cursor.fetchall() # To fetch all the rows from the student
#result = cursor.fetchone() # To get the only one row from a table called student

#print(result)
#for data in result:
 # print("{}".format(data))
#cursor.execute("create table student1( name VARCHAR(20),RegisterNumber INT(10),Gender VARCHAR(8))")
#cursor.execute("create table Customers( name VARCHAR(20),RegisterNumber INT(10),Gender VARCHAR(8))")
#cursor.execute("create table Customer(name varchar(20),login_Id varchar(18),password varchar(20))")

#sql = "INSERT INTO Customer (name,login_Id,password) VALUES (%s, %s,%s)"
#val = ("Nanda", "Kumar","Konetisetty")
#cursor.execute(sql, val)
#result = cursor.execute("Select * from Customer")
#cursor.execute("create table customer(name VARCHAR(20),address VARCHAR(20)")
#cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, val)

mydb.commit()

print(cursor.rowcount, "was inserted.")