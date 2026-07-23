import pyodbc

# Define the connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=VPW1902ASQL01\\sqlstudent1;"
    "DATABASE=S<replace this with your student id>;"
    "UID=S<replace this with your student id>;"
    "PWD=S<replace this with your student id>"
)

# Connect to the database
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL statement
cursor.execute("SELECT id, name FROM employee_contacts")

# Loop through the result set
for row in cursor:
    print("ID:", row.id, "Name:", row.name)

# Close the cursor and connection
cursor.close()
conn.close()