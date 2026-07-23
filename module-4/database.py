import pyodbc

# Define the connection string
conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=VPW1902ASQL01\\sqlstudent1;"
    "DATABASE=S21471878;"
    "UID=S21471878;"
    "PWD=S21471878;"
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