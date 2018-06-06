Class Bike
    price
    max_speed
    miles
    instance1
    instance2
    instance3
    methods
      displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
      ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
      reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...

class Bike(object):
    def __init__(self, price, max_speed, miles=0):
	# instance attributes
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def ride(self):
        print "riding"
        self.mile += 10
        return self

    def reverse(self):
        print "reversing"
        self.mile -=5
        return self
    
    def displayinfo(self):
        print "price: {}, maximum speed:{}. total miles: {}".format(self.price, self.max_speed, self.miles)
        return self


bike1 = Bike(100, "10mph")
bike1 = Bike(200, "20mph")
bike1 = Bike(300, "30mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()


