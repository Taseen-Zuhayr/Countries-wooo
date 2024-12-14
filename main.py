class Bangladesh():
    def capital(self):
        print("Capital of Bangladesh is Dhaka.")
        print("\n")
    def language(self):
        print("The official language of Bangladesh is Bangla.")
        print("\n")
    def funfact(self):
        print("Bangladesh is home to the world's largest mangrove forest, the Sundarbans.")
        print("\n")

class America():
    def capital(self):
        print("Capital of America is Washinton D.C.")
        print("\n")
    def language(self):
        print("The official language of America is American English.")
        print("\n")
    def funfact(self):
        print("The U.S. is the only country to have successfully landed humans on the moon.")
        print("\n")

ban = Bangladesh()
USA = America()

for i in (ban,USA):
    i.capital()
    i.language()
    i.funfact()


