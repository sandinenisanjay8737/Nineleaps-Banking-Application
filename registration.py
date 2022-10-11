from random import randint
import time
from connection import Execution
from validation import Validation

con = Execution()
val = Validation()

reg = {1:'Name', 2:'Address', 3:'Aadhar Number', 4:'Mobile'}

class Registration:

    def register(self):

        print('\nWelcome to Nineleaps Bank....\nLet\'s get started\n')
        time.sleep(1)

        while True:

            name = input(f'\nEnter your {reg[1]} : ')

            flag = val.name_check(name)                      # User Name Validation

            if flag is True:
                break


        address = input(f'\nEnter your {reg[2]} : ')         # No Validation for address as it may contain alphabets,digits and special characters

        while True:

            aadhar = input(f'\nEnter your {reg[3]} : ')
            ano = aadhar.replace(' ','')

            flag = val.aadhar_check(ano)                     # Aadhar Number Validation

            if flag is True:
                break
        
        while True:

            mobile = input(f'\nEnter your {reg[4]} : ')
            mno = mobile.replace('+91 ','').replace('+91-','').replace('+91','').replace(' ','')

            flag = val.mobile_check(mno)                     # Mobile Number Validation

            if flag is True:
                break

        self.accno = '251510'+str(randint(10**5,(10**6-1)))                  # Generating Account Number
        balance = 0

        s = [name,address,ano,mobile,self.accno,balance]
        self.s = s

        query = "insert into registration (user_name, address, aadhar, mobile, accno, balance) values (%s,%s,%s,%s,%s,%s)"
        con.execute(query,self.s)

        # Alloting one credit card and one debit card to the new user

        query2 = "update credit_cards set id = (%s) where id = (select id from registration where user_name = (%s) and mobile = (%s))"
        query3 = "update debit_cards set id = (%s) where id = (select id from registration where user_name = (%s) and mobile = (%s))"
        seq2 = seq3 = (self.accno,self.s[0],self.s[3])
        con.execute(query2,seq2)
        con.execute(query3,seq3)
        
        print('\n','< Registration completed >'.center(40,'*'),'\n')
        for i in range(10):
            print("\U0001F973",end='  ')
        print('\n')

    def print_details(self):

        print('\n','< Your Account Details >'.center(50,'*'),'\n')
        cur = con.cursor
        query = "select * from registration order by id desc limit 1"
        cur.execute(query,())
        output = cur.fetchone()
        acc = list(reg.values())
        acc.extend(['Account Number','Balance'])
        print('-'*54)
        for i in zip(acc,output[1:]):
            print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
            print('-'*54)
