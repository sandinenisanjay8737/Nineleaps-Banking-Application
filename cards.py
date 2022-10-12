from connection import Execution

con = Execution()
cur = con.cursor

class Cards:

    def __init__(self,userid):
        self.userid = userid

        query = "select accno from login where user_id = (%s)"
        seq = (self.userid,)
        con.execute(query,seq)
        accno = cur.fetchone()[0]
        
        self.accno = accno

    def cards_info(self):
        
        query1 = "select credit_card,cpin,crcvv from credit_cards where id =(select accno from login where user_id = (%s))"
        query2 = "select debit_card,dpin,dbcvv from debit_cards where id =(select accno from login where user_id = (%s))"
        seq = (self.userid,)

        con.execute(query1,seq)
        cr_cards = cur.fetchall()
        print('\nGetting Credit Card details...\n')
        for i in cr_cards:
            print(f'Credit card : {i[0]}')
            print(f'Card MPIN   : {i[1]}')
            print(f'Card CVV    : {i[2]}')
            print('-'*35)

        
        con.execute(query2,seq)
        db_cards = cur.fetchall()
        print('\nGetting Debit Card details...\n')
        for i in db_cards:
            print(f'Debit card  : {i[0]}')
            print(f'Card MPIN   : {i[1]}')
            print(f'Card CVV    : {i[2]}')
            print('-'*35)

    def reg_newcard(self):

        query = "select count(*) from ((select * from credit_cards where id = (%s)) union all (select * from debit_cards where id = (%s))) a"
        seq = (self.accno,self.accno)
        con.execute(query,seq)
        num_cards = cur.fetchone()[0]

        if num_cards < 4:

            print('\n','< Application for a new card >'.center(50,'*'),'\n')
            inp = input('Press 1 to apply for a Credit card or any other key for Debit card : ')
            if inp == '1':
                query = "update credit_cards set id = (%s) where id = (select id+50 from registration where accno = (%s))"
                seq = (self.accno,self.accno)
                con.execute(query,seq)
                print('\nNew Credit card applied and will be sent to you within 5 working days...')
            else:
                query = "update debit_cards set id = (%s) where id = (select id+50 from registration where accno = (%s))"
                seq = (self.accno,self.accno)
                con.execute(query,seq)
                print('\nNew Debit card applied and will be sent to you within 5 working days...')

        else:
            print('\nNumber of cards reached maximum limit.\nYou cannot apply for another...')
            

    def change_mpin(self):

        while True:
            inp = input('\nSelect 1 for Credit card MPIN change or 2 for Debit card MPIN change : ')
            print()
            query1 = "select {0} from {0}s where id =(select accno from login where user_id = (%s))"
            seq = (self.userid,)
            s={}

            if inp == '1':
                con.execute(query1.format('credit_card'),seq)
                cr_cards = cur.fetchall()
                for i,j in zip(cr_cards,range(1,10)):
                    print(f'{j} : {i[0]}\n')
                    s[j] = i[0]
                card_no = int(input('Select the Credit card for which you want to change the MPIN : '))
                query2 = "select cpin from credit_cards where credit_card = (%s)"
                seq2 = (s[card_no],)
                con.execute(query2,seq2)
                cr_pin = cur.fetchone()[0]
                while True:
                    old_pin = int(input('\nEnter the old MPIN : '))
                    if old_pin == cr_pin:

                        while True:
                            new_pin = input('\nEnter your new_pin : ')

                            if len(new_pin) == 4:
                                if new_pin.replace(' ','').isalnum():
                                    break
                                else:
                                    print('\nMPIN must only have digits.\nNo alphabets or special characters are allowed.\nTry again...')
                            else:
                                print('\nMPIN must be 4 digits only. Try Again...')

                        query3 = "update credit_cards set cpin = (%s) where credit_card = (%s)"
                        seq3 = (new_pin,s[card_no])
                        con.execute(query3,seq3)
                        print('\nMPIN changed successfully....\n')
                        break
                    else:
                        print('Wrong PIN entered. Try Again...')
            elif inp == '2':
                con.execute(query1.format('debit_card'),seq)
                db_cards = cur.fetchall()
                for i,j in zip(db_cards,range(1,10)):
                    print(f'{j} : {i[0]}\n')
                    s[j] = i[0]
                card_no = int(input('Select the Debit card for which you want to change the MPIN : '))
                query2 = "select dpin from debit_cards where debit_card = (%s)"
                seq2 = (s[card_no],)
                con.execute(query2,seq2)
                cr_pin = cur.fetchone()[0]
                while True:
                    old_pin = int(input('\nEnter the old MPIN : '))
                    if old_pin == cr_pin:
                        new_pin = int(input('\nEnter your new_pin : '))
                        query3 = "update debit_cards set dpin = (%s) where debit_card = (%s)"
                        seq3 = (new_pin,s[card_no])
                        con.execute(query3,seq3)
                        print('\nMPIN changed successfully\n')
                        break
                    else:
                        print('\nWrong PIN entered. Try Again')
            else:
                print('\nInvalid Input. Try Again....')
        

        


