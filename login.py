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

    def logging_in(self):

        print('\n','< LOGIN PAGE >'.center(50,'~'))

        while True:

            userid = input('\nEnter your User Id : ')
            self.userid = userid

            query1 = "select user_id from login"
            seq1 = ()
            con.execute(query1,seq1)
            ids = cur.fetchall()
            l = []
            for i in ids:
                l.append(i[0])            

            if userid in l:

                query2 = "select password from login where user_id = (%s)"
                seq2 = (userid,)
                con.execute(query2,seq2)
                correct_password = cur.fetchone()[0]

                i = 1
                while i<=4:

                    password = input('\nPassword : ')

                    if password == correct_password:
                        break
                    else:
                        print('\nIncorrect Password. Try Again....\n')
                        print('Attempts Left',4-i,'\n')
                        if i == 4:
                            print('\nAll attempts used. Login After 24 hours\n')
                            locked = True
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
        con.execute(query,seq)
        acc_info = cur.fetchone()
        print('-'*54)
        for i in zip(list(info.values()), acc_info):
            print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
            print('-'*54)

    def more_info(self):
        
        while True:

            ben = Beneficiaries(self.userid)
            cards = Cards(self.userid)
            print()
            print('-'*23)
            for i,j in more_info.items():
                print('| {} | {:<15} |'.format(i,j))
                print('-'*23)
            
            a = input('\nSelect 1 for your Beneficiaries or 2 for your Cards information or any other key to exit: ')
            if a == '1':
                ben.list_beneficiaries()    
            elif a == '2':
                cards.cards_info()
            else:
                break


    def update_info(self,userid):

        print()
        query = "desc registration"
        seq = ()
        con.execute(query,seq)
        rows = cur.fetchall()

        while True:

            s={}
            for i in range(1,5):
                print(i,':',rows[i][0].upper(),'\n')
                s[i]=rows[i][0].upper()
            
            while True:
                inp = input('\nSelect the field you want to update : ')
                if inp in ['1','2','3','4']:
                    break
                else:
                    print('\nInvalid Input. Try Again')

            
            if inp == '1':
                
                while True:

                    new_info = input('\nEnter the new {} : '.format(s[1]))

                    flag = val.name_check(new_info)                   # User Name Validation

                    if flag is True:
                        break

            elif inp == '2':

                new_info = input('\nEnter the new {} : '.format(s[2]))
            
            elif inp == '3':
    
                while True:

                    new_info = input('\nEnter the new {} : '.format(s[3]))
                    ano = new_info.replace(' ','')

                    flag = val.aadhar_check(ano)                     # Aadhar Number Validation

                    if flag is True:
                        break
        
            elif inp == '4':

                while True:

                    new_info = input('\nEnter the new {} : '.format(s[4]))
                    mno = new_info.replace('+91 ','').replace('+91','')

                    flag = val.mobile_check(mno)                     # Mobile Number Validation

                    if flag is True:
                        break
                    

            query = "update registration set {} = (%s) where accno = (select accno from login where user_id = (%s))".format(s[int(inp)].lower())
            seq = (new_info,userid)
            con.execute(query,seq)
            print('\nAccount Information updated succesfully')

            inpt = input('\nPress 1 to exit or any other key to update your information again : ')
            print()
            if inpt == '1':
                break
            else:
                pass

