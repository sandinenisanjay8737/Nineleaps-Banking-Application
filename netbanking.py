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
            con.execute(query1,seq1)                    # Query to get all the existing userid's.
            ids = cur.fetchall()
            l = []
            for i in ids:
                l.append(i[0])

            user_id = input('\nCreate a User Id : ')         

            if user_id in l:         # Checks if the user_id matches with any of the existing usernames.

                print('\nUser_id not Available. Try another..')
            
            else:

                if re.match("^[a-zA-Z0-9_.]+$", user_id) is not None:     # User Id Validation
                    break
                
                else:
                    print('\nInvalid User Id\nUser Id should not contain Whitespaces and special characters except ( \'_\' or \'.\' ) are not allowed.\nTry Again....')

        while True:

            password = input('\nNew Password     : ')

            if len(password) not in range(8,21):                          # Password Length Validation

                print('\nPassword length must be atleast 8 and less than 20.\nTry another..')
            
            else:

                if re.match("^[a-zA-Z0-9@._]+$", password) is not None:   # Password Validation
                    break
                
                else:
                    print('Password must not contain Whitespaces and special characters except ( \'@\' or \'_\' or \'.\' ) are not allowed.\nTry Again....')

        while True:

            # Infinite loop that asks to confirm password and breaks only when user enters the right password.

            confirmpassword = input('\nConfirm Password : ')

            if confirmpassword == password:                               # Password Confirmation

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