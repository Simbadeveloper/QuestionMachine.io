#!/usr/bin/python
import psycopg2
conn = psycopg2.connect(database="questionmachinedb", user="postgres", password="silas",
host="127.0.0.1", port="5432")

print ("Opened database successfully")

#create a table for users
cur = conn.cursor()
cur.execute('''CREATE TABLE  USERS
(ID SERIAL PRIMARY KEY NOT NULL,
FNAME VARCHAR NOT NULL,
LNAME VARCHAR NOT NULL,
USERNAME VARCHAR NOT NULL,
EMAIL VARCHAR NOT NULL,
PASSWORD VARCHAR NOT NULL,
REGISTERDATE TIMESTAMP  DEFAULT CURRENT_TIMESTAMP)''')
print ("UsesTable created successfully")
conn.commit()
conn.close()


#after creating a table for users you can add details
cur = conn.cursor()
cur.execute("INSERT INTO USER (FNAME,LNAME,USERNAME,EMAIL,PASSWORD) \
VALUES ('Silas', 'Omurunga', 'Simba', 'silverdeltamega@gmail.com', '1111' )");
cur.execute("INSERT INTO USER (FNAME,LNAME,USERNAME,EMAIL,PASSWORD) \
VALUES ('Paul', 'otieno', 'Misso', 'silverdeltamega@gmail.com', '9999' )");
cur.execute("INSERT INTO USER (FNAME,LNAME,USERNAME,EMAIL,PASSWORD) \
VALUES ('Joshua', 'Mwangi', 'SunJoh', 'silverdeltamega@gmail.com', '1167' )");
cur.execute("INSERT INTO USER (FNAME,LNAME,USERNAME,EMAIL,PASSWORD) \
VALUES ('Peter','nyabera','Rock','silverdeltamega@gmail.com', '1134' )");
conn.commit()
print ("Records created successfully in UserTable")
conn.close()

