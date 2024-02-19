import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin123",
  database="Employee_db"
)

emp_table_name = "Nash_employee"