class Details:

    '''
    The Details class is for storing the details required for the connection with the Database.
    The reason for creating this class is that We do not want to display our credentials everytime we need to make a connection.
    An object of this class is created later in the Connection class. There we can access these details as attributes of the object.

    '''

    host='localhost'
    user="root"
    password="Your_password"   # Replace it with your MySQL password.
    db="DB_name"               # Replace it with your database name.