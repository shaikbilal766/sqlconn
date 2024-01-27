import cx_Oracle
import csv
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table Bilal(id number(1) primary key,name varchar(50))'''
    cur.execute(query)
#createtable()
def insertrecord(rid,name):
    record={'id':str(rid),'name':name}
    cur.execute("insert into Bilal(id,name)values(:id,:name)",record)
    conn.commit()
# insertrecord(6,'vinni')
# insertrecord(7,'vijay')
# insertrecord(8,'vikash')
# insertrecord(9,'vinay')
# insertrecord(10,'vijji')

def read_record():
    query="select* from Bilal"
    cur.execute(query)
    records=cur.fetchall()
    for row in records:
        print(row)
    # with open('records.csv','w',newline='') as csvfile:
    #           data=csv.writer(csvfile)
    #           data.writerow(['id','name'])
    #           for row in records:
    #             data.writerow(row)
#read_record()
def fetch_record(rid):
    record={'id':str(rid)}
    query="select* from Bilal where id=:id"
    cur.execute(query,record)
    row=cur.fetchall()
    print(row)
#fetch_record()
def update_name(rid):
    fetch_record(rid)
    name=input("enter new name")
    record={'id':str(rid),'name':name}
    query='update Bilal set name=:name where id=:id'
    cur.execute(query,record)
    conn.commit()
    fetch_record(rid)
#update_name()
def delete_record(rid):
    record={'id':str(rid)}
    query='delete from Bilal where id=:id'
    cur.execute(query,record)
    conn.commit()
#read_record()
#update_name(7)
def truncate():
     query="truncate table Bilal"
     cur.execute(query)
#truncate()
def insert_from_csv():
    with open('records.csv','r',newline='') as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])