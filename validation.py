class Validation:

    def name_check(self,name,flag=False):

        if name.replace(' ','').isalpha() is True:                  # User Name Validation       
            flag = True
        else:
            print('\nInvalid Input\nUser name should not contain digits or special characters.\nTry Again....')

        return flag

    def aadhar_check(self,ano,flag=False):

        if (ano.isnumeric() and len(ano)==12) is True:              # Aadhar Number Validation       
            flag = True
        else:
            print('\nInvalid Input\nAadhar Number should not contain alphabets or special characters and must be 12 digits long (excluding spaces).\nTry Again...')

        return flag

    def mobile_check(self,mno,flag=False):

        if (mno.isnumeric() and len(mno)==10):                      # Mobile Number Validation

            if (mno[0] in ['6','7','8','9']) is True:
                flag = True
            else:
                print('\nInvalid Mobile Number.\nMobile number must start with any of [ 6,7,8,9 ].')
        else:
            print('\nInvalid Input\nMobile Number must be 10 digits long and should not contain alphabets or special characters.\nTry Again...')

        return flag
