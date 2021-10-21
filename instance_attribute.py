class Employee:
    company="youtube"
    salary=200
#instance attribute is an attribute created by the object or instance.
nikita = Employee()
radhika = Employee()
nikita.salary = 400   #this is an instance attribute(instance means object)
#radhika.salary= 500
print(nikita.salary)
print(radhika.salary)