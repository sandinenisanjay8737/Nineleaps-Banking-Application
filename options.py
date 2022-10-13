from login import Login
from beneficiaries import Beneficiaries
from cards import Cards

options = {1:'List Beneficiaries',2:'List Cards',3:'Add a Beneficiary',4:'Update Account information',5:'Transfer Funds',6:'Change card MPIN',7:'Register for a New Card'}

class Info_and_Options:

    '''
    The info_and_options class is for providing different options for the user logged in.

    Those options are:
            1) List Beneficiaries.
            2) List Cards.
            3) Add a Beneficiary.
            4) Update Account information.
            5) Transfer Funds.
            6) Change card MPIN.
            7) Register for a New Card.

    It has one method defined for printing a list of options available for user logged in
    while taking input from the user to select any option among the options. And then the selected operation is carried out.

    When there is a need to display and carry out these options for the user logged in, 
    We need to create an object of this class in that file and we can call this class method depending on our requirement.

    '''

    def __init__(self,userid):

        '''
        Constructs all the necessary attributes for the info_and_options object.

        Parameters:
            userid (str) : Userid input given by the user while logging in.
        '''

        self.userid = userid

    def options(self):

        '''
        This method is used to display all the options and then carry out the option selected by the user.

        Parameters : None
        Returns    : None
        '''

        login = Login()                              # Creating an object of Login class required for updating Account information in this file.
        ben = Beneficiaries(self.userid)             # Creating an object of Beneficiaries class required for adding beneficiaries and transfering funds in this file.
        cards = Cards(self.userid)                   # Creating an object of Cards class required for changing MPIN and registering for a new card in this file.

        while True:

            print()
            print('-'*38)
            for i,j in options.items():              # This prints a table consisting of all the options.
                print('| {} | {:<30} |'.format(i,j))
                print('-'*38)
            
            inp2 = input('\nSelect the field you need : ')

            if inp2 == '1':
                ben.list_beneficiaries()             # Calling list_beneficiaries method from Beneficiaries class for printing all the existing beneficiaries.
                break

            elif inp2 == '2':
                cards.cards_info()                   # Calling cards_info method from Cards class for printing all cards details.
                break

            elif inp2 == '3':
                ben.add_beneficiary()                # Calling add_beneficiary method from Beneficiaries class for adding a new beneficiary.
                break

            elif inp2 == '4':
                login.update_info(self.userid)       # Calling update_info method from Login class for updating the Account information.
                break

            elif inp2 == '5':
                ben.transfer_funds()                 # Calling transfer_funds method from Beneficiaries class to tranfer funds from the account of user logged in.
                break

            elif inp2 == '6':
                cards.change_mpin()                  # Calling change_mpin method from Cards class for changing the MPIN.
                break

            elif inp2 == '7':
                cards.reg_newcard()                  # Calling reg_newcard method from Cards class to register for a new card.
                break

            else:
                print('\nInvalid Input. Try Again...')
