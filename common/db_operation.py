'''
Created on 28 Jun 2016
@author: jophy.cui
'''
#coding=utf-8 
import psycopg2

conn = psycopg2.connect(database="pc1", user="stanford", password="stanford", host="127.0.0.1", port="5432") 

 
cur = conn.cursor() 
cur.execute('select * from student_test_packages')
rows = cur.fetchall()   
for i in rows:   
    print i 
cur.close()   
conn.commit()   
conn.close() 