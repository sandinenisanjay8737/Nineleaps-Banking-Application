from connection import Execution
from loading import Loading

con = Execution()
cur = con.cursor

class Beneficiaries:

    '''
    The Beneficiaries class is for displaying beneficiary details of the user logged in 
    and other options like adding a new beneficiary and transferring funds.

    It has methods defined for each of the operation like printing a list of beneficiaries that the user possess,
    adding a new beneficiary, transferring funds to the existing beneficiaries of the user.

    When there is a need to display beneficiary details or carry out these operations, 
    We need to create an object of this class in that file and we can call these class methods depending on our requirement.

    Parameters:
        userid (str) : Userid input given by the user while logging in.
    
    Methods:
        1) add_beneficiary().
        2) list_beneficiaries().
        3) transfer_funds().
    '''

    def __init__(self,userid):

        '''
        Constructs all the necessary attributes for the beneficiaries object.

        Parameters:
            userid (str) : Userid input given by the user while logging in.
        '''

        self.userid = userid


        query1 = '''SELECT accno FROM login WHERE user_id = (%s)'''
        seq1 = (self.userid,)
        con.execute(query1,seq1)
        accno = cur.fetchone()[0]               # Query to get the accno of the user logged in.

        self.accno = accno

    def add_beneficiary(self):

        '''
        This method is for adding a new beneficiary for the user.
        A query is executed to get all the existing Account Numbers in our Bank. After user enters the beneficiary Account Number, it is validated.
        If the beneficiary Account Number is in the same bank, then only user can add this beneficiary. Beneficiary cannot be added otherwise.
        Also the user cannot add their own Account as a beneficiary. These exceptions are handled in this method.

        Parameters: None
        Returns: None
        '''
        
        print('\n','< Add a Benficiary >'.center(50,'*'))

        ben_name = input('\nEnter the Beneficiary Name : ')

        while True:                              # Infinite while loop that breaks only when user enters beneficiary accno from the same Bank and not his own.

            ben_accno = input('\nEnter Beneficiary Account Number : ')

            query = '''SELECT accno FROM registration'''
            seq = ()
            con.execute(query,seq)               # Query to get the existing Account numbers in our Bank.
            result = cur.fetchall()
            l = []
            for i in result:
                l.append(i[0])

            if ben_accno in l:

                if ben_accno != self.accno:      # While loop breaks when entered Beneficiary Account Number is not his own.

                    query2 = "INSERT INTO beneficiaries VALUES (%s,%s,%s,%s)"
                    seq2 = (self.userid,self.accno,ben_accno,ben_name)

                    con.execute(query2,seq2)     # Query to insert the newly added beneficiary details in the beneficiaries table after validation.

                    print('\nNew Beneficiary Added successfully.....\n')
                    break
                
                else:
                    print('\nYou cannot add your Account as beneficiary.\nTry Again...')


            else:
                print('\nAccount Number is not from our bank.\nYou can add a beneficiary only if they are from Nineleaps Bank...\nTry Again...')

        

    def list_beneficiaries(self):

        '''
        This method is for printing the list of beneficiaries that the user already have.
        A query is executed to get all the existing beneficiaries of the user from beneficiaries table.
        Then it iterates through the query result to print one after the other in a tabular format.

        Parameters: None
        Returns: None
        '''
        
        print('\n','< List of Beneficiaries >'.center(50,'*'),'\n')
        
        query = '''SELECT ben_name,ben_accno 
                    FROM beneficiaries 
                    WHERE accno = (%s)'''
        
        seq = (self.accno,)
        con.execute(query,seq)                   # Query to get all the existing beneficiaries of the user from beneficiaries table.
        rows = cur.fetchall()
        s = {}

        print('-'*73)
        for i,j in zip(range(1,10),rows):
            print('| {0} | Name : {1:<20}| Account Number : {2:<20}|'.format(i,j[0],j[1]))
            s[i] = j[1]
            print('-'*73)                        # Prints the list of beneficiaries in a tabular format.
        self.s = s

    def transfer_funds(self):

        '''
        This method is for transferring funds to the beneficiaries that the user already have.
        The list_beneficiaries method from the same class is called to list all the existing beneficiaries of the user.
        A query is executed to get the current balance of the user. After the user enters the transfer amount,
        It checks if the entered amount is less than the available balance, then tranfer funds. Otherwise, amount is asked again.
        And a query is executed to insert the transaction details with the transaction timestamp into the transactions table.

        Parameters: None
        Returns: None
        '''
        print('\n','< Money Transfer >'.center(50,'*'),'\n')

        self.list_beneficiaries()                 # Calling list_beneficiaries method from the same class to list all the existing beneficiaries of the user.

        inp = int(input('\nSelect the Account to which you want to transfer the money : '))

        query1 = "SELECT balance FROM registration WHERE accno = (%s)"
        seq1 = (self.accno,)

        con.execute(query1,seq1)                  # Query to get the available balance of the Account of the user.
        cur_balance = int(cur.fetchone()[0])

        while True:                               # Infinite While loop that breaks only when a transaction is completed.

            amount = int(input('\nEnter the amount : '))

            if amount < cur_balance:

                print('\nTransaction Processing...')   

                load = Loading()                  # Creating an object of Loading class.
                load.processing()                 # Calling the processing method to display the status bar.

                query2 = '''UPDATE registration
                            SET balance = balance - (%s) 
                            WHERE accno = (%s)'''
                
                seq2 = (amount,self.accno)        # Query to subtract the entered amount from the User Account.
                con.execute(query2,seq2)

                query3 = '''UPDATE registration
                            SET balance = balance + (%s) 
                            WHERE accno = (%s)'''
                
                seq3 = (amount,self.s[inp])       # Query to add the entered amount to the selected beneficiary Account.
                con.execute(query3,seq3)

                query4 = '''INSERT INTO transactions(from_acc,to_acc,amount,transaction_timestamp) 
                            VALUES (%s,%s,%s,now())'''
                
                seq4 = (self.accno,self.s[inp],amount)
                con.execute(query4,seq4)          # Query to insert the transaction details into the transactions table.

                print('\nTransaction Successful....')

                break
                
            else:
                print('\nInsufficient Funds in your account. Try with a lesser Amount.')

