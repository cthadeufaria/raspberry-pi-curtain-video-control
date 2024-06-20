from gpiozero import DistanceSensor
from time import time
import asyncio



class Sensor:
    def __init__(self, trigger, echo):
        self.sensor = DistanceSensor(trigger=trigger, echo=echo)
        self.distance = 100
        self.in_range = False
        self.out_of_range = True
        self.idle_time = 0.
        self.last_change_time = 0.

        print("Sensor initialized.")
        print("Distance: {} cm".format(self.get_distance_cm_rounded(2)))


    def get_distance(self):
        return self.sensor.distance


    def get_distance_cm(self):
        return self.sensor.distance * 100


    def get_distance_rounded(self, places):
        return round(self.get_distance_cm, places)


    def get_distance_cm_rounded(self, places):
        return round(self.sensor.distance * 100, places)

    
    async def listen(self):
        while True:
            self.distance = self.get_distance_cm_rounded(2)
            print("Distance: {} cm".format(self.distance))
            
            current_time = time()
            if self.distance < 10:
                if not self.in_range:
                    self.idle_time = 0
                    self.in_range = True
                    self.last_change_time = current_time
                else:
                    self.idle_time += current_time - self.last_change_time
                    self.last_change_time = current_time
            else:
                if self.in_range:
                    self.idle_time = 0
                    self.in_range = False
                    self.last_change_time = current_time
                else:
                    self.idle_time += current_time - self.last_change_time
                    self.last_change_time = current_time
            
            await asyncio.sleep(0.5)