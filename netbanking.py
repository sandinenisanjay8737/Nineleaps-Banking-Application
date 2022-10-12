import time
from connection import Execution
import re

con = Execution()
cur = con.cursor

class Netbanking:

    '''
    The Netbanking class is for enabling netbanking for the newly registered user.

    It has one method defined for creating a netbanking account for the new user 
    while taking inputs from the user for different fields like userid, password after registration is completed.

    When there is a need to create a netbanking account for the new user, 
    We need to create an object of this class in that file and we can call this class method depending on our requirement.

    Parameters:
        accno (str) : Account number assigned to the newly registered user.
    
    Methods:
        1) create_netbanking().
    '''

    def __init__(self,accno):

        """
        Constructs all the necessary attributes for the Netbanking object.

        Parameters:
            accno (str) : Account number assigned to the newly registered user.
        """

        self.accno = accno                # While creating an instance of this class, we have to pass accno as argument.

    def create_netbanking(self):

        '''
        This method is for creating a netbanking account for the new user 
        while taking inputs from the user for different fields like userid, password after registration is completed.

        A query is executed to get all the existing Userid's of Users in our Bank. 
        After the user enters the New User Id, it is checked for validation.

        If the User Id is already existing in the same bank for another user, 
        then user is asked to give another User Id. Then the User Id is validated.

        Valid User Id must only contain:

            1) Numeric digits are allowed.
            2) Alphabets ( UPPER CASE or LOWER CASE ).
            3) Only Two Special characters are allowed:
                    A) '.' (dot).
                    B) '_' (underscore).

        It must not have:

            1) Whitespaces.
        
        If the User Id is Valid, then the user is asked for a password, once they onter one, it is validated.

        Valid Password must only contain:

            1) Numeric digits are allowed.
            2) Alphabets ( UPPER CASE or LOWER CASE ).
            3) Only Three Special characters are allowed:
                    A) '.' (dot).
                    B) '_' (underscore).
                    C) '@' (at the rate of).
            4) Length must be greater than 8 and less than 20.

        It must not have:

            1) Whitespaces.

        Once the User Id and Password are valid, then the user is asked to confirm password.
        It keeps asking the user to confirm password till they enter the correct password.

        Once everything is done, a query is executed to insert the netbanking details into the login table.

        Parameters: None
        Returns: None
        '''
        
        time.sleep(1)
        print('\nDigital Banking at your Mobile....\nEnable your Net Banking in no-time\n')
        time.sleep(1)

        while True:
    
            query1 = '''SELECT user_id 
                        FROM login'''
            seq1 = ()                     # Query to get all the existing userid's.
            con.execute(query1,seq1)
            ids = cur.fetchall()
            l = []
            for i in ids:
                l.append(i[0])

            user_id = input('\nCreate a User Id : ')         

            if user_id in l:              # Checks if the user_id matches with any of the existing usernames.

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
                    print('\nPassword must not contain Whitespaces and special characters except ( \'@\' or \'_\' or \'.\' ) are not allowed.\nTry Again....')

        while True:

            # Infinite loop that asks to confirm password and breaks only when user enters the right password.

            confirmpassword = input('\nConfirm Password : ')

            if confirmpassword == password:                               # Password Confirmation

                query = '''INSERT INTO login (accno, user_id, password) 
                           VALUES (%s,%s,%s)'''
                
                seq = (self.accno,user_id,password)                       # Query to insert the netbanking details into the login table.
                con.execute(query,seq)
                print('\nNet Banking Enabled...\n')
                for i in range(10):
                    print("\U0001F973",end='  ')
                print('\n')
                break
            
            else:
                print('\nPassword didn\'t match.\nPlease Try again\n')
