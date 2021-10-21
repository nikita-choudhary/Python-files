class Employee:
    company="google"
    def showDetails(self):
        print("This is an employee class")
class programmar(Employee):
    company="youtube"
    def getdetails(self):
        print("This is the child class")
e=Employee()
p=programmar()
print(e.company)
print(p.company)
p.getdetails()
e.showDetails()
p.showDetails()
