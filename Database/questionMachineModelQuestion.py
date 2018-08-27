#!/usr/bin/python
import psycopg2
conn = psycopg2.connect(database="questionmachinedb", user="postgres", password="silas",
host="127.0.0.1", port="5432")

print ("Opened database successfully")
#create a table for question
cur = conn.cursor()
cur.execute('''CREATE TABLE  QUESTION
(QUESTIONID SERIAL PRIMARY KEY NOT NULL,
USERNAME VARCHAR NOT NULL,
QUESTION TEXT NOT NULL,
ID INT NOT NULL,
TIME TIMESTAMP  DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()
print ("QuestionTable created successfully")
conn.close()

#after creating a table for question you can add the details
cur = conn.cursor()
cur.execute("INSERT INTO QUESTION (USERNAME,QUESTION,ID) \
VALUES ('Simba', 'what does yoyo mean?', 1 )");
cur.execute("INSERT INTO QUESTION (USERNAME,QUESTION,ID) \
VALUES ('Misso', 'why do you love coding?', 1 )");
cur.execute("INSERT INTO QUESTION (USERNAME,QUESTION,ID) \
VALUES ('Sunjoh', 'what does EPIC mean?', 1 )");
cur.execute("INSERT INTO QUESTION (USERNAME,QUESTION,ID) \
VALUES ('Rock', 'what does KISS mean?', 1 )");
conn.commit()
print ("Records created successfully in QuestionTable")
conn.close()
