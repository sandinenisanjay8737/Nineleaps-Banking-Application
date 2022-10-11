from connection import Execution
from loading import Loading

con = Execution()
cur = con.cursor

class Beneficiaries:

    def __init__(self,userid):
        self.userid = userid

    def add_beneficiary(self):
        
        print('\n','< Add a Benficiary >'.center(50,'*'))
        ben_name = input('\nEnter the Beneficiary Name : ')
        ben_accno = input('\nEnter Beneficiary Account Number : ')
        query1 = "select accno from login where user_id = (%s)"
        seq1 = (self.userid,)
        con.execute(query1,seq1)
        accno = cur.fetchone()[0]
        query2 = "insert into beneficiaries (accno, ben_accno, ben_name) values (%s,%s,%s)"
        seq2 = (accno,ben_accno,ben_name)
        con.execute(query2,seq2)
        print('\nNew Beneficiary Added\n')

    def list_beneficiaries(self):
        
        print('\n','< List of Beneficiaries >'.center(50,'*'),'\n')
        
        query = "select ben_name,ben_accno from beneficiaries where accno = (select accno from login where user_id = (%s))"
        seq = (self.userid,)
        con.execute(query,seq)
        rows = cur.fetchall()
        s = {}
        print('-'*73)
        for i,j in zip(range(1,10),rows):
            print('| {0} | Name : {1:<20}| Account Number : {2:<20}|'.format(i,j[0],j[1]))
            s[i] = j[1]
            print('-'*73)
        self.s = s

    def transfer_funds(self):

        query = "select accno from login where user_id = (%s)"
        seq = (self.userid,)
        con.execute(query,seq)
        accno = cur.fetchone()[0]

        print('\n','< Money Transfer >'.center(50,'*'),'\n')
        self.list_beneficiaries()
        inp = int(input('\nSelect the Account to which you want to transfer the money : '))

        query1 = "select balance from registration where accno = (%s)"
        seq1 = (accno,)
        con.execute(query1,seq1)
        cur_balance = int(cur.fetchone()[0])

        while True:

            amount = int(input('\nEnter the amount : '))
            if amount < cur_balance:

                print('\nTransaction Processing...')   

                load = Loading()
                load.processing()

                query2 = "update registration set balance = balance - (%s) where accno = (%s)"
                seq2 = (amount,accno)
                con.execute(query2,seq2)

                query3 = "update registration set balance = balance + (%s) where accno = (%s)"
                seq3 = (amount,self.s[inp])
                con.execute(query3,seq3)

                query4 = "insert into transactions(from_acc,to_acc,amount,transaction_timestamp) values (%s,%s,%s,now())"
                seq4 = (accno,self.s[inp],amount)
                con.execute(query4,seq4)

                print('\nTransaction Successful....')

                break
                
            else:
                print('\nInsufficient Funds in your account. Try with a lesser Amount.')

