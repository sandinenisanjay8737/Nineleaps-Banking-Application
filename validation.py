class Validation:

    '''
    The Validation class is for validating inputs given by the user for respective fields and 
    It has methods defined for each of the Name, Aadhar Number and Mobile Number.

    When there is a need to validate the user inputs, 
    We need to create an object of this class in that file and we can call these class methods depending on our requirement.

    '''

    def name_check(self,name,flag=False):                           # User Name Validation

        '''
        This method is used to validate the Name given by the user either while registering or while updating the Account information.

        Valid USER NAME must only contain:

            1) Alphabets ( UPPER CASE or LOWER CASE ).
            2) Whitespaces are allowed.

        It must not have:

            1) Special characters.
            2) Numeric digits.

        Parameters:
                name (str): Name given as input by the user.
                flag (bool): Keyword argument initiated as False.( default is False )
        Returns:
                flag (bool): False if the input name is invalid and True if it is valid.
        '''

        if name.replace(' ','').isalpha() is True:       
            flag = True
        else:
            print('\nInvalid Input\nUser name should not contain digits or special characters.\nTry Again....')

        return flag

    def aadhar_check(self,ano,flag=False):                          # Aadhar Number Validation

        '''
        This method is used to validate the Aadhar Number given by the user either while registering or while updating the Account information.

        Valid Aadhar Number must only contain:

            1) Numeric digits.
            2) Must be 12 digits.

        It must not have:

            1) Special characters.
            2) Alphabets ( UPPER CASE or LOWER CASE ).
            3) Whitespaces.

        Parameters:
                ano (str): Aadhar Number given as input by the user.
                flag (bool): Keyword argument initiated as False.( default is False )
        Returns:
                flag (bool): False if the input Aadhar Number is invalid and True if it is valid.
        '''

        if (ano.isnumeric() and len(ano)==12) is True:       
            flag = True
        else:
            print('\nInvalid Input\nAadhar Number should not contain alphabets or special characters and must be 12 digits long (excluding spaces).\nTry Again...')

        return flag

    def mobile_check(self,mno,flag=False):                          # Mobile Number Validation

        '''
        This method is used to validate the Mobile Number given by the user either while registering or while updating the Account information.

        Valid Mobile Number must only contain:

            1) Numeric digits.
            2) Must be 10 digits.
            3) Must start with any of [ 6,7,8,9 ].

        It must not have:

            1) Special characters.
            2) Alphabets ( UPPER CASE or LOWER CASE ).
            3) Whitespaces.

        Parameters:
                mno (str): Mobile Number given as input by the user.
                flag (bool): Keyword argument initiated as False.( default is False )
        Returns:
                flag (bool): False if the input Mobile Number is invalid and True if it is valid.
        '''

        if (mno.isnumeric() and len(mno)==10):

            if (mno[0] in ['6','7','8','9']) is True:
                flag = True
            else:
                print('\nInvalid Mobile Number.\nMobile number must start with any of [ 6,7,8,9 ].')
        else:
            print('\nInvalid Input\nMobile Number must be 10 digits long and should not contain alphabets or special characters.\nTry Again...')

        return flag

