import random

class Seats:
    def __init__(self):
        self.total = 180
        self.window = 1
        self.seat_type = {"Seat":["B","C","D","E"],"WindowSeats":["A","F"]}
        self.seat_Number = {"SeatNumber":[i for i in range(1,31)]}
        self.classes = {"Economy":1,"Premuium Economy":1.5,"Business":2.5,"First Class":4}
        self.count = {"Economy":72,"Premium Economy": 28,"Business":12,"First":8,"Economy Window":36,"Premuim Economy Window":14,"Business Window":6,"First Class Window":4}
        self.date = 0
        self.month = 0
        self.hour = 0
        self.min = 0

    def list_adding(self):
        pass
    
    def price_config(self,price):
        classes = self.random_classes()
        self.window = self.random_window()
        have_window = "No"
        #print(f"Classes: {classes}, Window {self.window}")
        price = price * self.classes[classes] * self.window
        if (self.window) == 1.2:
            have_window = "Yes"
        else:
            pass
            
        return int(price),classes,have_window
    
    def seat_number_config(self):
       
        number = random.randint(1,30)
        if self.window == 1.2:
            seat_num = self.seat_type.get((list(self.seat_type.keys())[1]))[random.randint(0,1)]
        else:
            seat_num = self.seat_type.get((list(self.seat_type.keys())[0]))[random.randint(0,3)]
        seat_num = f"{seat_num}{number}"

        return seat_num

    def random_day(self):
        self.month = random.randint(1,12)

        if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            self.day = random.randint(1,30)
        elif self.month == 2:
            self.day = random.randint(1,28)
        else:
            self.day = random.randint(1,31)

        return self.day,self.month
    
    def random_date(self,year):
        day,month = self.random_day()

        if day < 10 and month < 10:
            return f"{year}/0{month}/0{day}"
        elif month < 10:
            return f"{year}/0{month}/{day}"
        elif day < 10:
            return f"{year}/{month}/0{day}"
        else:
            return f"{year}/{month}/{day}"

    def random_time(self):
        self.hour = random.randint(0,23)
        self.time = random.randint(0,59)
        if self.time < 10:
            self.time = f"{0}{self.time}"
        if self.hour < 10:
            self.hour = f"{0}{self.hour}"

        return f"{self.hour}:{self.time}"

    def random_classes(self):
        return list(self.classes.keys())[random.randint(0, 3)]
    
    def random_window(self):
        window_seat =[1.2,1,1][random.randint(0, 2)]
        return window_seat
    
