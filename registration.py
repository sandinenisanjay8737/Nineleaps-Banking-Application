from random import randint
import time
from connection import Execution
from validation import Validation

con = Execution()
cur = con.cursor
val = Validation()

reg = {1:'Name', 2:'Address', 3:'Aadhar Number', 4:'Mobile'}

class Registration:

    def register(self):

        print('\nWelcome to Nineleaps Bank....\nLet\'s get started\n')
        time.sleep(1)

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

        s = [name,address,ano,mno,self.accno,balance]
        self.s = s

        query = "insert into registration (user_name, address, aadhar, mobile, accno, balance) values (%s,%s,%s,%s,%s,%s)"

        con.execute(query,self.s)                            # Query to insert the new user information into the registration table.

        query2 = "update credit_cards set id = (%s) where id = (select id from registration where user_name = (%s) and mobile = (%s))"
        query3 = "update debit_cards set id = (%s) where id = (select id from registration where user_name = (%s) and mobile = (%s))"
        seq2 = seq3 = (self.accno,self.s[0],self.s[3])
        con.execute(query2,seq2)                             # Queries to allot one credit card and one debit card to the new user.
        con.execute(query3,seq3)
        
        print('\n','| Registration completed |'.center(40,'*'),'\n')
        for i in range(10):
            print("\U0001F973",end='  ')                     # This prints a sequence of emojis.
        print()

    def print_details(self):

        print('\n','< Your Account Details >'.center(50,'*'),'\n')
        
        query = "select * from registration order by id desc limit 1"
        cur.execute(query,())
        output = cur.fetchone()                              # Query to fetch the latest inserted entry i.e.,the new user's details.

        acc = list(reg.values())
        acc.extend(['Account Number','Balance'])

        print('-'*56)                                        # This prints the details in a Tabular format.
        for i in zip(acc,output[1:]):
            print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
            print('-'*56)
