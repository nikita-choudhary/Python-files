class employee:
    def getSalary(self,greeting):
        print(f"the salary is {self.salary} {greeting}")
    @staticmethod
    def greet():       #since greet doesn,t need to be passed an arguement
        print("Good morning mam")
nikita=employee()
nikita.greet()
nikita.salary=2000000
nikita.getSalary("thanks")