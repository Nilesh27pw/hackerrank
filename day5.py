class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.__Age=initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.__Age<0:
            print("Age is not valid, setting age to 0.")
            self.__Age=0
        if self.__Age<13:
            print("You are young.")
        elif self.__Age>=13 and self.__Age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.__Age+=1

