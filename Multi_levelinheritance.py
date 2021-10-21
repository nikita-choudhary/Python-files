class Employee:
    company="youtube"
    def showDetails(self):
        print(f"hey there!I am a youtuber {self.desig}")
class Freelancer(Employee):
    company="upwork"
    def getDetails(self):
        print("This is child class 1")
class Programmar(Freelancer):
    language="python is the best"
    def details(self):
        print(f"this is the child class 2. \n Also, {self.language}")
p=Programmar()
e=Employee()
f=Freelancer()
p.company="google"
print(p.company)
print(f.company)
p.getDetails()
f.desig="data engineer"
f.showDetails()