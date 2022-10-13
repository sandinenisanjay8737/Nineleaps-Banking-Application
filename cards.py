from connection import Execution

con = Execution()
cur = con.cursor

class Cards:

    '''
    The Cards class is for displaying Cards details of the user logged in 
    and other options like registering for a new card and changing MPIN.

    It has methods defined for printing a list of cards that the user possess,
    registering for a new card, changing the MPIN of the existing cards of the user.

    When there is a need to display card details or carry out these operations, 
    We need to create an object of this class in that file and we can call these class methods depending on our requirement.

    Parameters:
        userid (str) : Userid input given by the user while logging in.

    Methods:
        1) cards_info().
        2) reg_newcard().
        3) change_mpin().
    '''

    def __init__(self,userid):

        '''
        Constructs all the necessary attributes for the cards object.

        Parameters:
            userid (str) : Userid input given by the user while logging in.
        '''

        self.userid = userid

        query = '''SELECT accno 
                   FROM login 
                   WHERE user_id = (%s)'''

        seq = (self.userid,)                           # Query to get the Account Number of the user logged in.
        con.execute(query,seq)
        accno = cur.fetchone()[0]
        
        self.accno = accno

    def cards_info(self):

        '''
        This method is for printing the list of both credit and debit cards that the user already have.
        Queries are executed to get the details from credit_cards and debit_cards tables.
        Then it iterates through both the query results to print one after the other in a tabular format.

        Parameters: None
        Returns: None
        '''
        
        query1 = '''SELECT credit_card,cpin,crcvv 
                    FROM credit_cards 
                    WHERE id =(%s)'''
                                                       # Queries to get the Credit and Debit card details of the user logged in.
        query2 = '''SELECT debit_card,dpin,dbcvv 
                    FROM debit_cards 
                    WHERE id =(%s)'''
        
        # In both the credit_cards and debit_cards tables, id is the account number of the user.

        seq = (self.accno,)

        con.execute(query1,seq)
        cr_cards = cur.fetchall()

        print('\nGetting Credit Card details...\n')
        
        for i in cr_cards:
            print('-'*38)
            print(f'| Credit card | {i[0]:<20} |')
            print('-'*38)
            print(f'| Card MPIN   | {i[1]:<20} |')     # Prints Credit cards one by one in a tabular format.
            print('-'*38)
            print(f'| Card CVV    | {i[2]:<20} |')
            print('-'*38)
            print()

        
        con.execute(query2,seq)
        db_cards = cur.fetchall()

        print('\nGetting Debit Card details...\n')
        
        for i in db_cards:
            print('-'*38)
            print(f'| Debit card  | {i[0]:<20} |')
            print('-'*38)
            print(f'| Card MPIN   | {i[1]:<20} |')     # Prints Debit cards one by one in a tabular format.
            print('-'*38)
            print(f'| Card CVV    | {i[2]:<20} |')
            print('-'*38)
            print()

    def reg_newcard(self):

        '''
        This method is for registering for a new credit or debit card for the user.
        A query is executed to get the count of credit_cards and debit_cards that the user already have.
        If the count is less than 4, then only user is eligible for applying for a new card. They cannot apply for another card if the count is already 4.

        Parameters: None
        Returns: None
        '''

        query = '''SELECT count(*) 
                   FROM ((SELECT * FROM credit_cards WHERE id = (%s)) 
                            UNION ALL 
                         (SELECT * FROM debit_cards WHERE id = (%s))) AS a'''
        
        seq = (self.accno,self.accno)                  # Query to get the count of cards that the user already have.
        con.execute(query,seq)
        num_cards = cur.fetchone()[0]

        if num_cards < 4:

            print('\n','< Application for a new card >'.center(50,'*'),'\n')

            inp = input('Press 1 to apply for a Credit card or any other key for Debit card : ')

            if inp == '1':
                query = '''UPDATE credit_cards 
                           SET id = (%s) 
                           WHERE id = (SELECT id+50 FROM registration WHERE accno = (%s))'''

                # While creating the credit_cards table and iserting data, I have inserted integers from 1 to 100 in the id column.
                # So my credit_cards table contains pre-defined card numbers with cpin and ccvv already alotted.
                # This query replaces the id in credit_cards table with the user accno.

                seq = (self.accno,self.accno)
                con.execute(query,seq)

                print('\nNew Credit card applied and will be sent to you within 5 working days...')

            else:
                query = '''UPDATE debit_cards 
                           SET id = (%s) 
                           WHERE id = (SELECT id+50 FROM registration WHERE accno = (%s))'''

                # While creating the debit_cards table and iserting data, I have inserted integers from 1 to 100 in the id column.
                # So my debit_cards table contains pre-defined card numbers with dpin and dcvv already alotted.
                # This query replaces the id in debit_cards table with the user accno.

                seq = (self.accno,self.accno)
                con.execute(query,seq)

                print('\nNew Debit card applied and will be sent to you within 5 working days...')

        else:
            print('\nYou already have 4 cards. Number of cards reached maximum limit.\n\nYou cannot apply for another card...')
            

    def change_mpin(self):

        '''
        This method is for changing the MPIN of either credit or debit card that the user already have.
        A query is executed to get the card numbers from either credit_cards table or debit_cards table based on the card type selected by the user.
        These card numbers are displayed in a tabular format. and the user is asked to select the card they have to change the MPIN.
        After the card is selected, another query is executed to get the old MPIN of the selected card from either credit_cards or debit_cards table.


        Parameters: None
        Returns: None
        '''

        def new_pin_check():

            '''
            This function in the change_mpin method is used to validate the New MPIN given by the user after the correct old MPIN is entered.

            Valid MPIN must only contain:

                1) Numeric digits.
                2) Must be 4 digits.

            It must not have:

                1) Special characters.
                2) Alphabets ( UPPER CASE or LOWER CASE ).
                3) Whitespaces.

            Parameters: None

            Returns:
                    new_pin (str): After taking input from the user, it validates the MPIN and this is returned only when it is valid.
        '''

            while True:

                new_pin = input('\nEnter your new_pin : ')

                if len(new_pin) == 4:              # New MPIN Validation.

                    if new_pin.replace(' ','').isnumeric():
                        break
                    else:
                        print('\nMPIN must only have digits.\nNo alphabets or special characters are allowed.\nTry again...')
                else:
                    print('\nMPIN must be 4 digits only. Try Again...')

            return new_pin


        while True:

            inp = input('\nSelect 1 for Credit card MPIN change or 2 for Debit card MPIN change : ')
            print()
            query1 = '''SELECT {0} 
                        FROM {0}s 
                        WHERE id = (SELECT accno FROM login WHERE user_id = (%s))'''
            
            # This query string can be used for both credit_cards and debit_cards just by formatting it.
            
            seq = (self.userid,)
            s={}

            if inp == '1':

                con.execute(query1.format('credit_card'),seq)
                cr_cards = cur.fetchall()

                for i,j in zip(cr_cards,range(1,10)):
                    print(f'{j} : {i[0]}\n')                   # Prints the list of credit card numbers the user already have.
                    s[j] = i[0]
                
                card_no = int(input('Select the Credit card for which you want to change the MPIN : '))

                query2 = '''SELECT cpin 
                            FROM credit_cards 
                            WHERE credit_card = (%s)'''
                
                seq2 = (s[card_no],)
                con.execute(query2,seq2)                       # Query to get the old MPIN of the selected credit card.
                cr_pin = cur.fetchone()[0]

                while True:                                    # Infinite while loop that breaks only when the correct old MPIN is entered by the user.

                    old_pin = input('\nEnter the old MPIN : ')

                    if old_pin == cr_pin:

                        new_pin = new_pin_check()              # Calling the new_pin_check function from the same method to validate New MPIN.

                        query3 = '''UPDATE credit_cards 
                                    SET cpin = (%s) 
                                    WHERE credit_card = (%s)'''
                        
                        seq3 = (new_pin,s[card_no])            # Query to update the MPIN in credit_cards table.
                        con.execute(query3,seq3)

                        print('\nYour Credit card MPIN changed successfully....\n')

                        break
                    
                    else:
                        print('Wrong PIN entered. Try Again...')
                break

            elif inp == '2':

                con.execute(query1.format('debit_card'),seq)
                db_cards = cur.fetchall()

                for i,j in zip(db_cards,range(1,10)):
                    print(f'{j} : {i[0]}\n')                   # Prints the list of debit card numbers the user already have.
                    s[j] = i[0]
                
                card_no = int(input('Select the Debit card for which you want to change the MPIN : '))

                query2 = '''SELECT dpin 
                            FROM debit_cards 
                            WHERE debit_card = (%s)'''
                
                seq2 = (s[card_no],)
                con.execute(query2,seq2)                       # Query to get the old MPIN of the selected debit card.
                cr_pin = cur.fetchone()[0]

                while True:                                    # Infinite while loop that breaks only when the correct old MPIN is entered by the user.

                    old_pin = input('\nEnter the old MPIN : ')

                    if old_pin == cr_pin:

                        new_pin = new_pin_check()              # Calling the new_pin_check function from the same method to validate New MPIN.

                        query3 = '''UPDATE debit_cards 
                                    SET dpin = (%s) 
                                    WHERE debit_card = (%s)'''
                        
                        seq3 = (new_pin,s[card_no])            # Query to update the MPIN in debit_cards table.
                        con.execute(query3,seq3)
                        
                        print('\nYour Debit card MPIN changed successfully....\n')
                        break
                    
                    else:
                        print('\nWrong PIN entered. Try Again...')
                break
            else:

                print('\nInvalid Input. Try Again....')
        

        


