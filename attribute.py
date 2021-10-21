class Employee:
    company="Google"    #here company is an attribute or adjective of the class employee

nikita=Employee()
radhika=Employee()     #object instantiation
print(nikita.company)
print(radhika.company)   #inoking the object with the attribute
Employee.company = "youtube"     #we may change the value of attribute after object instantiation
print(nikita.company)
print(radhika.company)
