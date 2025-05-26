# import mysql.connector

# # Get user input for a login form
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# # Create a SQL query to check the user's login credentials
# query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';"

# # Connect to the database and execute the query
# db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', port= '6603', database='PE07')
# cursor = db.cursor()
# cursor.execute(query)

# # Fetch the results
# result = cursor.fetchone()

# # Check if the user exists and the password is correct
# if result is not None:
#     print("Login successful!")
# else:
#     print("Invalid username or password.")
    
# # Close the database connection
# db.close()

#THIS IS THE FIX TO PREVENT SQL INJECTION

from sqlalchemy import create_engine, text

# Get user input for a login form
username = input("Enter your username: ")
password = input("Enter your password: ")

query = text("SELECT * FROM users WHERE username = :username AND password = :password")

# Connect to the database and execute the query
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:6603/PE07')

with engine.connect() as conn:
  result = conn.execute(query, {"username": username, "password": password}).fetchone()

# Check if the user exists and the password is correct
if result:
  print("Login successful!")
else:
  print("Invalid username or password.")
