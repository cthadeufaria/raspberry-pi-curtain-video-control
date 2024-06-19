from gpiozero import DistanceSensor



class Sensor:
    def __init__(self, trigger, echo):
        self.sensor = DistanceSensor(trigger=trigger, echo=echo)
        self.distance = 100
        self.in_range = False
        self.out_of_range = True


    def get_distance(self):
        return self.sensor.distance


    def get_distance_cm(self):
        return self.sensor.distance * 100


    def get_distance_rounded(self, places):
        return round(self.get_distance_cm, places)


    def get_distance_cm_rounded(self, places):
        return round(self.sensor.distance * 100, places)

    
    def listen(self):
        while True:
            self.distance = self.get_distance_cm_rounded(2)
            
            if self.distance < 10:
                self.in_range = True
            else:
                self.in_range = False