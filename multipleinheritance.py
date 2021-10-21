class Employee:
    company="youtube"
    def showDetails(self):
        print(f"hey there!I am a youtuber {self.desig}")
class Freelancer:
    company="upwork"
    def getDetails(self):
        print("This is another base class")
class Programmar(Employee,Freelancer):
    language="python is the best"
    def details(self):
        print(f"this is the child class having two base class. \n Also, {self.language}")
p=Programmar()
e=Employee()
f=Freelancer()
p.details()
p.getDetails()
print(p.company)
print(f.company)
p.desig="data scientist"
p.showDetails()
