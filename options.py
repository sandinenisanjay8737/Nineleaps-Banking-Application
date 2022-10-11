from login import Login
from beneficiaries import Beneficiaries
from cards import Cards

options = {1:'Add a Beneficiary',2:'Update Account information',3:'Transfer Funds',4:'Change card MPIN',5:'Register for a New Card'}

class info_and_options:

    def __init__(self,userid):
        self.userid = userid

    def options(self):

        login = Login(self.userid)
        ben = Beneficiaries(self.userid)
        cards = Cards(self.userid)

        while True:

            print()
            print('-'*38)
            for i,j in options.items():
                print('| {} | {:<30} |'.format(i,j))
                print('-'*38)
            inp2 = input('\nSelect the field you need : ')

            if inp2 == '1':
                ben.add_beneficiary()
            elif inp2 == '2':
                login.update_info(self.userid)
            elif inp2 == '3':
                ben.transfer_funds()
            elif inp2 == '4':
                cards.change_mpin()
            elif inp2 == '5':
                cards.reg_newcard()

            else:
                print('\nInvalid Input. Try Again...')

            inp5 = input('\nPress 1 to view options again or any other key to exit : ')

            if inp5 == '1':
                pass
            else:
                break

