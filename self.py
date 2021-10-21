class Employee:
    company="microsoft"
    def getSalary(self):
        print(f"the salary of this person in {self.company} is {self.salary}")

nikita= Employee()
nikita.salary=100000
nikita.getSalary()     
#Employee.getSalary(nikita)