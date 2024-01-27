import cx_Oracle
import csv
a=cx_Oracle.Connection('system/manager@mother')
b=a.cursor()

def createtable():
    query='''create table mcanaresh(id number(2) primary key, name varchar(50))'''
    b.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    b.execute("insert into mcanaresh(id,name) values(:id,:name)",record)
    a.commit()
# insertrecord(2,'ramesh')
# insertrecord(3,'suresh')
# insertrecord(4,'ganesh')
# insertrecord(5,'mahesh')
    
def read_records():
    query='select * from mcanaresh'
    b.execute(query)
    records = b.fetchall()
    for row in records:
        print(row)
    with open('records.csv','w',newline='') as csvfile:
      data=csv.writer(csvfile)
      data.writerow(['id','name'])
      for row in records:
        data.writerow(row)
def fetch_record(sid):
    record={'id':str(sid)}
    query='select * from mcanaresh where id = :id'
    b.execute(query,record)
    record=b.fetchall()
    for row in record:
        print(row)


def update_name(sid):
   fetch_record(sid)
   name=input('enter new name:- ')
   record={'id':str(sid),'name':name}
   query = 'update mcanaresh set name = :name where id = :id'
   b.execute(query,record)
   a.commit()
   fetch_record(sid)

def delete_name(sid):
    fetch_record(sid)
    record={'id':str(sid)}
    query = 'delete from mcanaresh where id = :id'
    b.execute(query,record)
    a.commit()
    fetch_record(sid)


def truncate():
    query='truncate table mcanaresh'
    b.execute(query)




def insert_from_csv():
    with open('records.csv','r') as csvfile:
        data=csv.reader(csvfile)
        data= list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])