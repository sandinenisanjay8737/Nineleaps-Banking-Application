from random import randint
import time
from connection import Execution
from validation import Validation

con = Execution()                 # Creating an object of Execution class to execute queries in this file.
cur = con.cursor
val = Validation()                # Creating an object of Validation class to validate the inputs given by the user.

class Registration:

    '''
    The Registration class is for registering a new user while taking inputs from the user for different fields like Name, Address, Aadhar Number and Mobile Number.
    It has methods defined for registering a new user and printing the details after registration is completed.

    When there is a need to register a new user, 
    We need to create an object of this class in that file and we can call these class methods depending on our requirement.

    Methods:
        1) register().
        2) print_details().
    '''

    def register(self):

        '''
        This method is used to register a new user.
        It asks the user inputs for different fields like Name, Address, Aadhar Number, Mobile Number.
        It validates the each input by calling the methods from Validation class.

        A new Account Number is generated and allotted to the new user. And Balance is initiated to 10,000.
        One new credit and one new debit card are allotted the user.

        Then a query is executed to insert the New User details into the registration table.
        Two queries are executed to update the account number assigned to the new user in both the credit_cards and debit_cards tables.

        Parameters: None.
        Returns: None.

        '''

        print('\nWelcome to Nineleaps Bank....\nLet\'s get started\n')
        time.sleep(1)

        reg = {1:'Name', 2:'Address', 3:'Aadhar Number', 4:'Mobile'}

        enterstring = '\nEnter your {:15} : '

        while True:

            name = input(enterstring.format(reg[1]))         # User Name Validation.

            flag = val.name_check(name)                      # Calling name_check method from Validation class.

            if flag is True:                                 # User name while loop breaks only if the name is valid.
                break


        address = input(enterstring.format(reg[2]))          # No Validation for address as it may contain alphabets,digits and special characters.

        while True:

            aadhar = input(enterstring.format(reg[3]))       # Aadhar Number Validation
            ano = aadhar.replace(' ','')

            flag = val.aadhar_check(ano)                     # Calling aadhar_check method from Validation class.

            if flag is True:                                 # Aadhar number while loop breaks only if it is valid. 
                break
        
        while True:

            mobile = input(enterstring.format(reg[4]))       # Mobile Number Validation

            mno = mobile.replace('+91 ','').replace('+91-','').replace('+91','').replace(' ','')

            flag = val.mobile_check(mno)                     # Calling mobile_check method from Validation class.

            if flag is True:                                 # Mobile number while loop breaks only if it is valid.
                break

        self.accno = '251510'+str(randint(10**5,(10**6-1)))  # Generating Account Number

        balance = 10000                                      # Balance initiated to 10000.

        s = [name,address,ano,mno,self.accno,balance]        # Taking the filtered aadhar number (ano) and mobile number (mno) to store in the registration table.
        self.s = s

        query = '''INSERT INTO registration (user_name, address, aadhar, mobile, accno, balance) 
                    VALUES (%s,%s,%s,%s,%s,%s)'''

        con.execute(query,self.s)                            # Query to insert the new user information into the registration table.

        query2 = '''UPDATE credit_cards SET id = (%s) 
                    WHERE id = (SELECT id 
                                FROM registration 
                                WHERE user_name = (%s) AND mobile = (%s))'''
         
                                                             # Queries to allot one credit card and one debit card to the new user.
        
        query3 = '''UPDATE debit_cards SET id = (%s) 
                    WHERE ID = (SELECT id 
                                FROM registration 
                                WHERE user_name = (%s) AND mobile = (%s))'''
        
        seq2 = seq3 = (self.accno,self.s[0],self.s[3])
        con.execute(query2,seq2)
        con.execute(query3,seq3)
        
        print('\n','| Registration completed |'.center(40,'*'),'\n')
        for i in range(10):
            print("\U0001F973",end='  ')                     # This prints a sequence of emojis.
        print()

    def print_details(self):

        '''
        This method is used to print the details of the new user once the registration is completed.
        A query is executed to fetch the latest inserted entry from the registration table i.e.,the new user's details.
        Then it iterates through the query result to print the information in a tabular format.
        
        Parameters: None.
        Returns: None.

        '''
        reg = {1:'Name', 2:'Address', 3:'Aadhar Number', 4:'Mobile'}

        print('\n','< Your Account Details >'.center(50,'*'),'\n')
        
        query = '''SELECT * 
                    FROM registration 
                    ORDER BY id DESC LIMIT 1'''              # Query to fetch the latest inserted entry i.e.,the new user's details.
        
        cur.execute(query,())
        output = cur.fetchone()

        acc = list(reg.values())
        acc.extend(['Account Number','Balance'])

        print('-'*56)                                        # This prints the details in a Tabular format.
        for i in zip(acc,output[1:]):
            print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
            print('-'*56)
