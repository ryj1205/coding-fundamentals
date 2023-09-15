##################################################################
# Classes
##################################################################
# A programatic object containing data and methods
# i.e. variables and functions
##################################################################

class Login:

    # Attributes:
    def __init__(self,passeduser,passedpw,passedserver):
        self.username = passeduser
        self.password = passedpw
        self.server = passedserver

    # Method - MANDATORY TO ADD A VARIABLE - YOU CAN USE THE SELF KEYWORD:
    def login(self):
        print("You are logged in as {} on {}".format(self.username, self.server))

    def emailcheck(self):
        self.login()
        print("You got mail:", self.server)

##################################################################

gmail = Login("ryanjackson", "p@ssword", "gmail.smtp.com")

print(gmail.emailcheck())

##################################################################