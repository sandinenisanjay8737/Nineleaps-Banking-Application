import mysql.connector as mysqlcon
from config import Details

class Connection:
    det = Details()
    try:
        con= mysqlcon.connect(host=det.host,user=det.user,password=det.password,db=det.db)
        cursor=con.cursor(buffered=True)
    except:
        print("Database details provided are incorrect")

class Execution:
    try:
        a=Connection()
        con=a.con
        cursor=a.cursor
        def execute(self,query,seq):
            self.query = query
            self.seq = seq
            self.cursor.execute(self.query,self.seq)
            self.con.commit()
            
    except:
        print("Query cannot be executed")