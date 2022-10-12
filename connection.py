import mysql.connector as mysqlcon
from credentials import Details

class Connection:

    '''
    The Connection class is for making the connection with the Database.
    An object of the Details class is created here. We can access the credentials as attributes of the object.

    '''

    det = Details()

    try:
        con= mysqlcon.connect(host=det.host,user=det.user,password=det.password,db=det.db)
        cursor=con.cursor(buffered=True)
    except:
        print("Database details provided are incorrect")

class Execution:

    '''
    The Execution class is for the execution of SQL queries after a connection with the Database is made.
    An object of the Connection class is created here to make the connection. We can access the connection and cursor objects as attributes.

    When there is a need to execute the queries, 
    We need to create an object of this class in that file and we can call this class method depending on our requirement.

    '''

    try:
        a=Connection()
        con=a.con
        cursor=a.cursor

        def execute(self,query,seq):

            '''
            This method is used to execute the SQL queries after the connection is made with the Database.

            Parameters:
                    query (str): SQL query that is to be executed.
                    seq (tuple): Tuple consisting of parameters that takes their corresponding positions in the query string.
            Returns: None.

            '''

            self.query = query
            self.seq = seq
            self.cursor.execute(self.query,self.seq)
            self.con.commit()
            
    except:
        print("Query cannot be executed")