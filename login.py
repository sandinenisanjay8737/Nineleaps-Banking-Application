from connection import Execution
from registration import Registration
from netbanking import Netbanking
from validation import Validation


info = {1:'Name',2:'Account number',3:'Mobile',4:'Balance'}

con = Execution()           # Creating an object of Execution class to execute queries in this file.
cur = con.cursor
val = Validation()          # Creating an object of Validation class to validate the inputs given by the user.


class Login:

    '''
    The Login class is for Logging the user in and display the details after Logging in
    and it has an option of updating the Account information.

    It has methods defined for carrying out the Login process, printing the account details of the user,
    updating the Account information and validating the New information given by the user.

    When there is a need for the user to Login and display Account details or carry out the update information process, 
    We need to create an object of this class in that file and we can call these class methods depending on our requirement.

    Parameters:
             locked (bool) : Keyword argument initiated as False.( default is False )
                             Changes to True if all the password attempts are used.
        
        maintenance (bool) : Keyword argument initiated as False.( default is False )
                                Must be passed as True when we don't want the users to login during maintenance of the Application.

    Methods:
        1) logging_in().
        2) acc_info().
        3) update_info(userid).
    '''

    def __init__(self,locked=False,maintenance=False):

        """
        Constructs all the necessary attributes for the Login object.

        Parameters:

                 locked (bool) : Keyword argument initiated as False.( default is False )
                                 Changes to True if all the password attempts are used.
            
            maintenance (bool) : Keyword argument initiated as False.( default is False )
                                 Must be passed as True when we don't want the users to login during maintenance of the Application.
        """

        self.locked = locked
        self.maintenance = maintenance

    def logging_in(self):

        '''
        This method is for Logging the user in.

        A query is executed to get all the existing usernames of users in our Bank. After user enters the User Id, it is validated.
        If the User Id does not exist, then user is asked again for the User Id. And after the correct user id is entered,
        a query is executed to get the correct password of the user from login table, then there are 3 attempts provided for the user.
        In case of wrong password entered, if all the attempts are used, program is exited.

        Parameters: None
        Returns: None
        '''

        print('\n'+('-'*14).center(50,' '))
        print('<| LOGIN PAGE |>'.center(50,'~'))
        print(('-'*14).center(50,' '))

        while True:                                     # Infinite while loop that breaks only when the user enters valid username and correct password.

            userid = input('\nEnter your User Id : ')
            self.userid = userid                        # Creating a class attribute to store the userid for accessing again when required.

            query1 = '''SELECT user_id FROM login'''
            seq1 = ()
            con.execute(query1,seq1)                    # Query to get all the existing usernames from the login table.
            ids = cur.fetchall()
            l = []
            for i in ids:
                l.append(i[0])

            if userid in l:                                  

                query2 = '''SELECT password 
                            FROM login 
                            WHERE user_id = (%s)'''
                
                seq2 = (userid,)
                con.execute(query2,seq2)                # Query to get the correct password of the entered userid from login table.
                correct_password = cur.fetchone()[0]

                i = 1
                while i<=4:                             # Loop with only 4 iterations to ask correct password from the user.

                    password = input('\nPassword           : ')

                    if password == correct_password:
                        break

                    else:
                        print('\nIncorrect Password. Try Again....\n')
                        print('Attempts Left - ( {} )'.format(4-i))

                        if i == 4:                      # Breaks out of while loop when all attempts are used.

                            print('\nAll attempts used. Login After 24 hours.\n')
                            self.locked = True          # Overwriting the class attribute "locked" to True for accessing again when required. 
                        i+=1                                                                
                break

            else:

                print('\nUser Id not found. Try again...')

                while True:                             # This while loop is for registration for the user if they are not registered before.

                    inp = input('\nPress 1 to give User Id again or 2 if have not registered before : ')
                    
                    if inp == '1':
                        break
                    
                    elif inp == '2':                    # Flow enters this snippet if user selects registration.

                        reg = Registration()            # Creating an object of Registration class.
                        reg.register()                  # Calling the register method to start the registration process.
                        reg.print_details()             # Calling the print_details method to display the Account information after the registration is completed.
                        nb = Netbanking(reg.accno)      # Creating an object of Netbanking class.
                        nb.create_netbanking()          # Calling the create_netbanking method to start the netbanking account creation process.
                    
                    else:
                        print('\nInvalid Input. Try Again...')

    def acc_info(self):

        '''
        This method is for displaying the Account information once the user is logged in.
        A query is executed to get account details of the user from the registration table.
        Then it prints the details from the query result in a tabular from.

        Parameters: None
        Returns: None
        '''

        print('\n','< Account Information >'.center(50,'*'),'\n')

        query = '''SELECT user_name, accno, mobile, balance 
                   FROM registration 
                   WHERE accno = (SELECT accno FROM login WHERE user_id = (%s))
'''
        seq = (self.userid,)
        con.execute(query,seq)                          # Query to get account details of the user from registration table.
        acc_info = cur.fetchone()

        print('-'*64)
        for i in zip(list(info.values()), acc_info):    # Prints all the Account details in tabular form.
            print('|  {:^16}  |      {:<30}     |'.format(i[0],i[1]))
            print('-'*64)

    def update_info(self,userid):

        '''
        This method is for updating the Account information after validating the user input of the selected field.
        A query is executed to get column names in the registration table. Then it prints the list of column names. 
        Then asks the user to select the field they want to update.
        After validating the user input, a query is executed to update the selected field in the registration table.

        Parameters:
            userid (str) : User Id of the User Logged in.
        Returns: None
        '''

        print()
        query = "DESC registration"
        seq = ()
        con.execute(query,seq)                          # Query to get column names in the registration table.
        rows = cur.fetchall()

        enterstring = '\nEnter the new {:15} : '

        while True:

            s={}
            for i in range(1,5):
                print(i,':',rows[i][0].upper(),'\n')    # This will print a tabular form consisting of 4 fields.
                s[i]=rows[i][0].upper()
            
            while True:

                inp = input('\nSelect the field you want to update : ')

                if inp in ['1','2','3','4']:
                    break
                else:
                    print('\nInvalid Input. Try Again...')

            
            if inp == '1':
                
                while True:

                    new_info = input(enterstring.format(s[1]))   # New User Name Validation.

                    flag = val.name_check(new_info)              # Calling name_check method from Validation class.

                    if flag is True:                             # User name while loop breaks only if the new name is valid.
                        break

            elif inp == '2':

                new_info = input(enterstring.format(s[2]))       # No Validation for new address as it may contain alphabets,digits and special characters.
            
            elif inp == '3':
    
                while True:

                    new_info = input(enterstring.format(s[3]))   # New Aadhar Number Validation.
                    ano = new_info.replace(' ','')

                    flag = val.aadhar_check(ano)                 # Calling aadhar_check method from Validation class.

                    new_info = ano
                    
                    if flag is True:                             # Aadhar number while loop breaks only if it is valid.
                        break
        
            elif inp == '4':

                while True:

                    new_info = input(enterstring.format(s[4]))   # New Mobile Number Validation.

                    mno = new_info.replace('+91 ','').replace('+91','')

                    flag = val.mobile_check(mno)                 # Calling mobile_check method from Validation class.

                    new_info = mno

                    if flag is True:                             # Mobile number while loop breaks only if it is valid.
                        break
                    

            query = '''UPDATE registration 
                       SET {} = (%s) 
                       WHERE accno = (SELECT accno FROM login WHERE user_id = (%s))'''.format(s[int(inp)].lower())
            
            seq = (new_info,userid)
            con.execute(query,seq)                               # Query to update the input field in the registration table.
            
            print('\nAccount Information updated succesfully')

            inpt = input('\nPress 1 to exit or any other key to update your information again : ')
            print()
            if inpt == '1':
                break
            else:
                pass

