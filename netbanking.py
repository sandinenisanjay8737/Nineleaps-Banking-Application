import time
from connection import Execution
import re

con = Execution()
cur = con.cursor

class Netbanking:

    def __init__(self,accno):
        self.accno = accno

    def create_netbanking(self):
        
        time.sleep(1)
        print('\nDigital Banking at your Mobile....\nEnable your Net Banking in no-time\n')
        time.sleep(1)

        while True:
    
            query1 = "select user_id from login"
            seq1 = ()
            con.execute(query1,seq1)
            ids = cur.fetchall()
            l = []
            for i in ids:
                l.append(i[0])

            user_id = input('\nCreate a User Id : ')         

            if user_id in l:                                           # User Id Validation

                print('\nUser_id not Available. Try another..')
            
            else:

                if re.match("^[a-zA-Z0-9_.]+$", user_id) is not None:
                    break
                
                else:
                    print('\nInvalid User Id\nUser Id should not contain Whitespaces and special characters except ( \'_\' or \'.\' ) are not allowed.\nTry Again....')

        while True:

            password = input('\nNew Password     : ')

            if len(password) < 8:

                print('\nPassword must be atleast 8 characters long. Try another..')
            
            else:

                if re.match("^[a-zA-Z0-9@._]+$", password) is not None:
                    break
                
                else:
                    print('Password must not contain Whitespaces and special characters except ( \'@\' or \'_\' or \'.\' ) are not allowed.\nTry Again....')
        
        while True:

            confirmpassword = input('\nConfirm Password : ')
            if confirmpassword == password:
                query = "insert into login (accno, user_id, password) values (%s,%s,%s)"
                seq = (self.accno,user_id,password)
                con.execute(query,seq)
                print('\nNet Banking Enabled...\n')
                for i in range(10):
                    print("\U0001F973",end='  ')
                print('\n')
                break
            else:
                print('\nPassword didn\'t match.\nPlease Try again\n')
