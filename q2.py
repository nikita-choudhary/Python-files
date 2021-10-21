class Calculator:
    @staticmethod
    def greet():
        print("Hello User!")
    def squareOfNumber(self,number):
        self.number=number
        p=self.number**2
        print(f"the square of {self.number} is {p}")
        q=self.number**3
        print(f"the cube of {self.number} is {q}")
        r=self.number**0.5
        print(f"the square root of {self.number} is {int(r)}")
n=Calculator()
n.greet()
n.squareOfNumber(25)