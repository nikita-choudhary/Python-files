class Employee:
    company = "e and y"
    #def __init__(self):       #init acts as a constructor
        #print("hey yaa")
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
        print("employee class is created")
        print(f"the department of the employee is {self.department}")
    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        
        
n=Employee("harry",100000,"data science")
n.getDetails()