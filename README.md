# Nineleaps-Banking-Application
This repository consists of different code files for the banking application project.

MySQL

First, I created different tables in MySQL database for each operation as -
    _____________________    
 1) | beneficiaries     |
 2) | credit_cards      |
 3) | debit_cards       |
 4) | login             |
 5) | registration      |
 6) | transactions      |
    ---------------------


1) In the registration table, there are 7 columns namely - id, user_name, address, aadhar, mobile, accno, balance.

        id - primary key and auto-increment.
        User while registering is asked for user_name, address, aadhar, mobile.
        An account number(accno)[12 digits] starting with '251510' gets auto-generated and balance is initialized to Rs.10,000 for each registered user.
        Later (user_name, address, aadhar, mobile, accno, balance) are inserted into this table.

2) In the credit_cards table, there are 4 columns - id (primary key), credit_card, cpin, ccvv.

        First, id column consists of integers from 1 to 100 and later replaced with accno of the newly registered user or any user who apply for a new card.
        I generated 100 different credit card numbers [16 digits] starting with '6518', their corresponding MPINs, CVVs and inserted them into this table.
        
3) In the debit_cards table, there are 4 columns - id (primary key), debit_card, dpin, dcvv.

        First, id column consists of integers from 1 to 100 and later replaced with accno of the newly registered user or any user who apply for a new card.
        I generated 100 different debit card numbers [16 digits] starting with '4582', their corresponding MPINs, CVVs and inserted them into this table.

4) In the login table, there are 3 columns - accno, user_id, password.

        When a user is newly registered, a netbanking account is created after taking a new username and a new password from the user.
        Then (accno,user_id,password) are inserted into the this table.

5) In the beneficiaries table, there are 4 columns - user_id, accno, ben_accno, ben_name.

        When a user logged in adds a new beneficiary, beneficiary account name (ben_name) and beneficiary Account Number (ben_accno) are asked.
        Then (user_id,accno,ben_accno,ben_name) are inserted into this table.

6) In the transactions table, there are 5 columns - transaction_id, from_accno, to_acc, amount, transaction_timestamp.

        transaction_id - primary key and auto-increment.
        When a user transfer funds to one of his beneficiaries, the transaction details along with the system timestamp during transaction are stored.
        Then (transaction_id,from_accno,to_acc,amount,transaction_timestamp) are inserted into this table.


Python

There are 11 .py files for different operations. They are -

1) credentials.py - 
   It contains the details required for the database connection.
   classes:
      1) Details.
         Methods: None.
   
2) connection.py -  
   It has classes for connection with the database and execution of queries.
   classes:
      1) Connection.
         Methods: None.
      2) Execution.
         Methods: execute(query,seq)

3) validation.py -
   It has the Validation class with methods for checking if the user input is valid or not.
   classes:
      1) Validation.
         Methods: name_check(name), aadhar_check(ano), mobile_check(mno).

4) loading.py -
   It has the Loading class with a method to diaplay a status bar.
   classes:
      1) Loading.
         Methods: processing().

5) registration.py - 
   It contains the Registration class with methods for registering a new user and printing the details after registration is completed.
   This will take input details from newly registering users and insert them into the registration table in the database.
   classes:
      1) Registration.
         Methods: register(), print_details().
   
6) netbanking.py - 
   After the registration, the user needs to create a net banking account where he can set the username and password 
   and later these details are inserted into the login table.
   classes:
      1) Netbanking.
         Methods: create_netbanking().

7) login.py - 
   This file checks the userid and password given by the user and after successful login, prints the account info.
   It has the method which is called when the user wants to update Account Information.
   classes:
      1) Login.
         Methods: logging_in() ,acc_info(), update_info(userid).
   
8) beneficiaries.py - 
   In this file, there is a Benefeciaries class with methods for adding a beneficiary, listing the saved beneficiaries, and transfering funds.
   classes:
      1) Beneficiaries.
         Methods: add_beneficiary(), list_beneficiaries(), transfer_funds().

9) cards.py -
   It consists of Cards class with methods defined for displaying Cards details of the user logged in 
   and other options like registering for a new card and changing MPIN.
   classes:
      1) Cards.
         Methods: cards_info(), reg_newcard(), change_mpin().
   
10) options.py - 
    This file contains Info_and_options class with a method defined for printing a list of options.
    And then the selected operation is carried out.
    There are different options for different actions.
    classes:
       1) Cards.
          Methods: cards_info(), reg_newcard(), change_mpin()

11) main.py -
    This file is where all the classes from other files are imported and objects are created.
    Then the methods of each object is called when required.
    Loops are used to maintain the flow of execution of different functions based on the user input.
   

Main Features:

1) Validation of the User input when required.
2) Display of a Status bar while Logging in, transferring funds, Logging Out.
3) Listing the options and Information in Tabular Format.
4) Flexibility of code usage with different parameters like maintenance,locked etc.
5) 3 Attempts given for User to give correct password. If all are used up, program is exited.
6) Not allowing the user to have same User Id like any other user.
7) Asking to confirm password while netbanking account creation and confirm New PIN while changing MPIN of a Card.
8) While adding a beneficiary, Checking if the beneficiary Account Number is from the same bank and also not allowing to add the user's own account.
 
