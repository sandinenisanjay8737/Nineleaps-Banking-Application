from registration import Registration
from netbanking import Netbanking
from login import Login
from options import Info_and_Options
from loading import Loading

while True:

    inp = input('\nPress 1 if you are an existing customer or\nPress 2 if you are new to Nineleaps Banking : ')

    login = Login(maintenance=False)             # Creating an object of Login class.
    ''' The parameter "maintenance" must be passed as True in case of maintenance.'''

    if login.maintenance is True:                # While loop breaks when maintenance is passed as True.

        print('\nApplication under Maintenance.\nSorry for the inconvenience.\nPlease try again after few hours...\n')
        break

    else:

        if inp == '1':

            login.logging_in()                   # Calling the logging_in method to start the Logging process.
            userid = login.userid

            if login.locked is True:             # While loop breaks when locked becomes True which occurs when all the password attemps are used.
                break
            
            else:

                print('\nLogging In. Please wait...')

                load = Loading()                 # Creating an object of Loading class.
                load.processing()                # Calling the processing method to display the status bar.

                print('\n'+'Login Successful....'+'\n')

                for i in range(10):
                    print("\U0001F973",end='  ') # This prints a sequence of emojis.
                print('\n')

                login.acc_info()                 # Calling the acc_info method to display the Account information after user is logged in.

                while True:

                    uinpt1 = input('\nPress 1 to View Options or any other key to Logout : ')

                    if uinpt1 == '1':
                                       
                        optionsobj = Info_and_Options(userid)  # Creating an object of info_and_options class.

                        optionsobj.options()     # Calling the options method to display options and perform operations.

                    else:

                        print('\nLogging out. Please Wait...')

                        load.processing()        # Calling the processing method to display the status bar.

                        print('\n'+'Logged Out..\n\nThank You for visiting...','\n')

                        break
        
        elif inp == '2':                         # Flow enters this snippet if user selects registration.

            reg = Registration()                 # Creating an object of Registration class.
            reg.register()                       # Calling the register method to start the registration process.
            reg.print_details()                  # Calling the print_details method to display the Account information after the registration is completed.
            nb = Netbanking(reg.accno)           # Creating an object of Netbanking class.
            nb.create_netbanking()               # Calling the create_netbanking method to start the netbanking account creation process.
        
        else:

            print('\nInvalid Input. Try Again...')

        
        