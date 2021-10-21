class Employee:
    company="youtube"
    def showDetails(self):
        print(f"hey there!I am a youtuber {self.desig}")
    def __init__(self):
        print(f"Hello there welcome to art of living")
    def takeBreath(self):
        print("Relax and calm down yourself completely")
class Freelancer(Employee):
    company="upwork"
    def getDetails(self):
        print("This is child class 1")
    def takeBreath(self):
        super().takeBreath()
        print("Take a normal breathe in and breathe out completely")
class Programmar(Freelancer):
    language="python is the best"
    def details(self):
        print(f"this is the child class 2. \n Also, {self.language}")
    def takeBreath(self):
        super().takeBreath()
        print("breathe in to chant om")
    
p=Programmar()
e=Employee()
f=Freelancer()
p.company="google"
print(p.company)
print(f.company)
p.getDetails()
f.desig="data engineer"
f.showDetails()
#f.takeBreath()
p.takeBreath()