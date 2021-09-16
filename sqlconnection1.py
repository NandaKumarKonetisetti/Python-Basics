import mysql.connector.mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database = "nanda"
)

print(mydb)

cursor = mydb.cursor()
#cursor.execute("create table employees(name varchar(10),employeeid int(10),qualification varchar(10))")
sql = "INSERT INTO employees (name, employeeid,qualification) VALUES (%s, %s,%s)"
values = ('Nanda',1918,'BTech')
#cursor.execute(sql,values)
#mydb.commit()  # If we use commit method then only it will  insert the values otherwise not
#cursor.execute("insert into employees values('kumar',1919,'MTech')")

#mydb.commit()
cursor.execute("select * from employees")
res = cursor.fetchall()
print(res)
for i in res:
    print(i)