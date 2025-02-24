class Car:

    #for use inner class on outer class object you need to create instance on constructor
    def __init__(self):
        self.steering_object = self.Steering()

    #inner class (nested class)
    class Steering():
        @staticmethod
        def rotate():
            print("Rotating")

    @staticmethod
    def drive():
        print("Driving")

car = Car()

car.drive()

car.steering_object.rotate()