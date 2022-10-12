from connection import Execution
from registration import Registration
from netbanking import Netbanking
from beneficiaries import Beneficiaries
from cards import Cards
from validation import Validation


info = {1:'Name',2:'Account number',3:'Mobile',4:'Balance'}
more_info = {1:'Beneficiaries',2:'Cards'}

con = Execution()
cur = con.cursor
val = Validation()


class Login:

    def __init__(self,locked=False,maintenance=False):
        self.locked = locked
        self.maintenance = maintenance

    def logging_in(self):

        print('\n'+('-'*14).center(50,' '))
        print('<| LOGIN PAGE |>'.center(50,'~'))
        print(('-'*14).center(50,' '))

        while True:

            userid = input('\nEnter your User Id : ')
            self.userid = userid                                            # Creating a class attribute to store the userid for accessing again when required.

            query1 = "select user_id from login"
            seq1 = ()
            con.execute(query1,seq1)                                        # Query to get all the existing usernames from the login table.
            ids = cur.fetchall()
            l = []
            for i in ids:
                l.append(i[0])

            if userid in l:

                query2 = "select password from login where user_id = (%s)"
                seq2 = (userid,)
                con.execute(query2,seq2)                                    # Query to get the correct password of the entered userid from login table.
                correct_password = cur.fetchone()[0]

                i = 1
                while i<=4:                                                 # Loop with only 4 iterations to ask correct password from the user.

                    password = input('\nPassword           : ')

                    if password == correct_password:
                        break

                    else:
                        print('\nIncorrect Password. Try Again....\n')
                        print('Attempts Left - ( {} )'.format(4-i))
                        if i == 4:                                          # Breaks out of while loop when all attempts are used.

                            print('\nAll attempts used. Login After 24 hours.\n')
                            self.locked = True                              # Creating a class attribute "locked" for accessing again when required. 
                        i+=1                                                                
                break

            else:

                print('\nUser Id not found. Try again...')

                while True:

                    inp = input('\nPress 1 to give User Id again or 2 if have not registered before : ')
                    
                    if inp == '1':
                        break
                    
                    elif inp == '2':

                        reg = Registration()
                        reg.register()
                        reg.print_details()
                        nb = Netbanking(reg.accno)
                        nb.create_netbanking()
                    
                    else:
                        print('\nInvalid Input. Try Again...')

    def acc_info(self):

        print('\n','< Account Information >'.center(50,'*'),'\n')
        query = "select user_name, accno, mobile, balance from registration where accno = (select accno from login where user_id = (%s))"
        seq = (self.userid,)
        con.execute(query,seq)                                              # Query to get account details of the user from registration table.
        acc_info = cur.fetchone()

        print('-'*64)
        for i in zip(list(info.values()), acc_info):
            print('|  {:^16}  |      {:<30}     |'.format(i[0],i[1]))       # Prints all the Account details in tabular form.
            print('-'*64)

    def more_info(self):
        
        while True:

            ben = Beneficiaries(self.userid)
            cards = Cards(self.userid)
            print()
            print('-'*23)
            for i,j in more_info.items():
                print('| {} | {:<15} |'.format(i,j))
                print('-'*23)
            
            a = input('\nSelect 1 for your Beneficiaries or 2 for your Cards information or any other key for Options : ')
            if a == '1':
                ben.list_beneficiaries()                                    # Prints all the beneficiaries present.
            elif a == '2':
                cards.cards_info()                                          # Prints the Card details.
            else:
                break


    def update_info(self,userid):

        print()
        query = "desc registration"
        seq = ()
        con.execute(query,seq)                                              # Query to get different fields in the registration table.
        rows = cur.fetchall()

        enterstring = '\nEnter the new {:15} : '

        while True:

            s={}
            for i in range(1,5):
                print(i,':',rows[i][0].upper(),'\n')                        # This will print a tabular form consisting of 4 fields.
                s[i]=rows[i][0].upper()
            
            while True:
                inp = input('\nSelect the field you want to update : ')
                if inp in ['1','2','3','4']:
                    break
                else:
                    print('\nInvalid Input. Try Again...')

            
            if inp == '1':
                
                while True:

                    new_info = input(enterstring.format(s[1]))              # New User Name Validation.

                    flag = val.name_check(new_info)                         # Calling name_check method from Validation class.

                    if flag is True:                                        # User name while loop breaks only if the new name is valid.
                        break

            elif inp == '2':

                new_info = input(enterstring.format(s[2]))                  # No Validation for new address as it may contain alphabets,digits and special characters.
            
            elif inp == '3':
    
                while True:

                    new_info = input(enterstring.format(s[3]))              # New Aadhar Number Validation.
                    ano = new_info.replace(' ','')

                    flag = val.aadhar_check(ano)                            # Calling aadhar_check method from Validation class.

                    new_info = ano
                    
                    if flag is True:                                        # Aadhar number while loop breaks only if it is valid.
                        break
        
            elif inp == '4':

                while True:

                    new_info = input(enterstring.format(s[4]))              # New Mobile Number Validation.
                    mno = new_info.replace('+91 ','').replace('+91','')

                    flag = val.mobile_check(mno)                            # Calling mobile_check method from Validation class.

                    new_info = mno

                    if flag is True:                                        # Mobile number while loop breaks only if it is valid.
                        break
                    

            query = "update registration set {} = (%s) where accno = (select accno from login where user_id = (%s))".format(s[int(inp)].lower())
            seq = (new_info,userid)
            con.execute(query,seq)                                          # Query to update the input field in the registration table.
            print('\nAccount Information updated succesfully')

            inpt = input('\nPress 1 to exit or any other key to update your information again : ')
            print()
            if inpt == '1':
                break
            else:
                pass

