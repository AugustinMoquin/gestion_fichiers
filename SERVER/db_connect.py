import mysql.connector

# Database configuration
host = 'localhost'  # usually 'localhost' or '127.0.0.1'
user = 'root'
password = ''
database = 'python_tkinter'

# Create a connection to the database
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Check if the connection was successful
if connection.is_connected():
    print("Connected to the database!")

    # Perform database operations here

    # Close the connection when you're done
    connection.close()
    print("Connection closed.")
else:
    print("Connection failed.")