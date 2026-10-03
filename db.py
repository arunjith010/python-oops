import sqlite3

# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table using DDL comments
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dob DATE,
        age INTEGER,
        genter TEXT,
        mobile INTEGER,
        email TEXT,
        password TEXT,
        preferred_language TEXT
       


    )
""")

 
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")