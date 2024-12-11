import sqlite3

## connect to sqllite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table
cursor = connection.cursor()

## Create the table
table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""
cursor.execute(table_info)

## Insert some more Records
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Ananya', 'Data Science', 'A', 88)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Arjun', 'Data Science', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Sanjana', 'Data Science', 'C', 91)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Ishaan', 'Data Science', 'A', 95)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Priya', 'Data Science', 'B', 87)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Siddharth', 'Data Science', 'C', 89)''')

## Display All The Records
print("The inserted records are")
data = cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)
    
## Commit your changes in the database
connection.commit()
connection.close()