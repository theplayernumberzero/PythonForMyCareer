class Parent:
    def __init__(self):
        self.balance_dad = 5000

    def display_balance(self):
        print(f"Parent balance is: {self.balance_dad}")

class Childeren(Parent):
    pass

class Step_Childeren(Parent):
    #override method and constructor
    def __init__(self):
        #constructor override edildiği için oto inherit olayı kalktı. Manuel eklememiz lazım
        super().__init__()  #super class constructor inherit edildi.
        self.balance = 2000

    def display_balance(self):
        #we can use upper class att with self keyword with reaching upper class constructor
        print(f"total balance is: {self.balance + self.balance_dad}")


childeren1 = Childeren()
#Constructor inherited from upper class
childeren1.display_balance()

step_childeren1 = Step_Childeren()
step_childeren1.display_balance()