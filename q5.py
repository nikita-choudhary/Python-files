class Train:
    train_name="Rajdhani express"
    def bookTicket(self):
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"contact_no : {self.contact_no}")
    @staticmethod
    def getStatus():
        print("total 10 seats are lect")

    def getFareinfo(self,place,fare):
        self.place=place
        self.fare=fare
        print(f"The fare for {self.place} is {self.fare}")

t=Train()
print(t.train_name)
t.name="Nikita"
t.age="25"
t.contact_no=9079272745
t.bookTicket()
t.getStatus()
t.getFareinfo("jaipur", 1000)