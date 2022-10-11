from registration import Registration
from netbanking import Netbanking
from login import Login
from options import info_and_options
from loading import Loading

while True:

    inp = input('\nPress 1 if you are an existing customer or 2 if you are new to Nineleaps Banking : ')

    if inp == '1':

        login = Login()
        login.logging_in()
        userid = login.userid

        if login.locked is True:
            break
        
        else:

            print('\nLogging In. Please wait...')

            load = Loading()
            load.processing()

            print('< Login Successful >'.center(50,'='))

            login.acc_info()

            uinpt1 = input('\nPress 1 to View more Information or any other key to View Options : ')

            if uinpt1 == '1':

                login.more_info()
            

            optionsobj = info_and_options(userid)
            optionsobj.options()

            uinpt2 = input('\nPress 1 to logout or any other key to login again : ')

            if uinpt2 == '1':

                print('\nLogging out. Please Wait...')

                load = Loading()
                load.processing()

                print('< Logged Out >'.center(50,'*'),'\n')

                break

            else:

                pass

    
    elif inp == '2':

        reg = Registration()
        reg.register()
        reg.print_details()
        nb = Netbanking(reg.accno)
        nb.create_netbanking()
    
    else:
        print('\nInvalid Input. Try Again...')

        
        