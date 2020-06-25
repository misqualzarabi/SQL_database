import os 
import sqlite3

##DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "northwind_small.sqlite3")
connection = sqlite3.connect('northwind_small.sqlite3')
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()



##What are the ten most expensive items (per unit price) in the database?
cursor.execute('''
    SELECT ProductName, UnitPrice FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
    ''')
expensive_items = cursor.fetchall()
print (expensive_items)

##What is the average age of an employee at the time of their hiring?
cursor.execute('''
    SELECT
        FirstName,
        LastName,
        strftime('%Y', BirthDate) As Birthdate,
        strftime('%Y', HireDate) As Hiredate,
        (strftime('%Y', HireDate) - strftime('%Y', BirthDate)) As HiringAge
    FROM Employee    
   
    ''')
Age = cursor.fetchall() ##Age of all the employees at the time of hiring 
print(Age)   

cursor.execute('''
    SELECT
        round(avg(strftime('%Y', HireDate) - strftime('%Y', BirthDate))) As Average_Age
    FROM Employee    
   
    ''')
Average_Age= cursor.fetchall() ##Average age of an employee at the time of hiring 
print(Average_Age)   


## What are the ten most expensive items (per unit price) in the database *and*
  ##their suppliers? 
  

cursor.execute('''
    SELECT Product.ProductName, Product.UnitPrice, Supplier.Id
    FROM Product
    LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10

    ''') 
join_columns = cursor.fetchall()  
print(join_columns) 

##What is the largest category (by number of unique products in it)?
cursor.execute('''
    SELECT Product.ProductName, count(distinct Product.Id) as unique_no_product, Category.Id, Category.CategoryName
    FROM Category
    LEFT JOIN Product ON Product.CategoryId = Category.Id
    ''')
largest_category = cursor.fetchall()  
print(largest_category)  

