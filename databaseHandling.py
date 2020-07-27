import sqlite3
conection = sqlite3.connect('MyDatabase.db')
print ("Opened database connection successfully")

conection.execute('DROP TABLE STUDENT')

conection.execute('''CREATE TABLE STUDENT
         (ROLLNO INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL);''')
print("Table STUDENT created successfully")

conection.execute("INSERT INTO STUDENT (ROLLNO,NAME) VALUES (1, 'Tom')")
conection.execute("INSERT INTO STUDENT (ROLLNO,NAME) VALUES (2, 'Sam')")
conection.execute("INSERT INTO STUDENT (ROLLNO,NAME) VALUES (3, 'Harry')")
conection.commit()

rows = conection.execute("SELECT ROLLNO,NAME FROM STUDENT")
for row in rows:
  print(row)

conection.close()