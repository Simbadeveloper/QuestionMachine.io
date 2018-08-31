#!/usr/bin/python
import psycopg2
conn = psycopg2.connect(database="questionmachinedb", user="postgres", password="silas",
host="127.0.0.1", port="5432")

print ("Opened database successfully")

#creating table for answer
cur = conn.cursor()
cur.execute("INSERT INTO ANSWER(USERNAME,ANSWER,ID) \
VALUES ('Simba', 'You own your own', 1 )");
cur.execute("INSERT INTO ANSWER (USERNAME,ANSWER,ID) \
VALUES ('Misso', 'itsmy passion', 1 )");
cur.execute("INSERT INTO ANSWER (USERNAME,ANSWER,ID) \
VALUES ('Sunjoh', 'excellence passion intergrity collaboration', 1 )");
cur.execute("INSERT INTO ANSWER (USERNAME,ANSWER,ID) \
VALUES ('Rock', 'keep it simple and stupid', 1 )");
conn.commit()
print ("Records created successfully in AnswerTable")
conn.close()

#after creating a table you can insert your details
cur = conn.cursor()
cur.execute("INSERT INTO ANSWER(USERNAME,ANSWER,ID) \
VALUES ('Simba', 'You own your own', 1 )");
cur.execute("INSERT INTO ANSWER (USERNAME,ANSWER,ID) \
VALUES ('Misso', 'itsmy passion', 1 )");
cur.execute("INSERT INTO ANSWER (USERNAME,ANSWER,ID) \
VALUES ('Sunjoh', 'excellence passion intergrity collaboration', 1 )");
cur.execute("INSERT INTO ANSWER (USERNAME,ANSWER,ID) \
VALUES ('Rock', 'keep it simple and stupid', 1 )");
conn.commit()
print ("Records created successfully in AnswerTable")
conn.close()

