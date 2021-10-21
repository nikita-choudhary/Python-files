class Train:
    train_name="Rajdhani express"
    def bookTicket(slf):
        print(f"Name : {slf.name}")
        print(f"age : {slf.age}")
        print(f"contact_no : {slf.contact_no}")
    
    """def getStatus(self,seats):
        self.seats=seats
        if(self.seats>0):
            print(f"total {self.seats} seats are left")
            self.seats=self.seats-1
        else:
            print("seat is not vacant")"""
    def getStatus(self):
        #self.seats=seats
        if(self.seats>0):
            print(f"total {self.seats} seats are left")
            self.seats=self.seats-1
        else:
            print("seat is not vacant")


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
t.seats=30
t.getStatus()
t.getStatus()
t.getStatus()
t.getStatus()

t.getFareinfo("jaipur", 1000)