import time,sys

class Loading:

    '''
    The Loading class is for printing an Animation of status bar that is displayed while Logging in or Transferring funds or Logging out.
    It has a method defined for displaying the status bar.

    When there is a need to display the status bar, 
    We need to create an object of this class in that file and we can call this class method depending on our requirement.

    Method:
        1) processing().
    '''

    animation = ["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□",
                "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]

    def processing(self):

        
        '''
        This method is for printing an Animation of status bar that is displayed while Logging in or Transferring funds or Logging out.
        It iterates through the animation list and prints the elements one after the other.

        Parameters: None
        Returns: None
        '''

        print()
        for i in range(len(self.animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + self.animation[i % len(self.animation)])
            sys.stdout.flush()
        print()
