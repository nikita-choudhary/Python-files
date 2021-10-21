class Programmar:
    company="microsoft"
    @staticmethod
    def details():
        print("programmer class is created!\nHere is the details of the programmers:\n")

    def __init__(self,name,id,salary,designation):
        self.name=name
        self.id=id
        self.salary=salary
        self.designation=designation
        print(f"the name of the programmar is {self.name}\nprogrammar's id : {self.id}\nHis salary is : {self.salary}\nDesignation is {self.designation}")

n= Programmar("nikita", 23456, 1000000, "data scientist")
n.details()
n=Programmar("radhika", 140199, 200000, "data engineer")
n= Programmar("charvi",140209,3000000,"salesforce engineer")