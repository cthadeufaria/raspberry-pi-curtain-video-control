from gpiozero import MotionSensor



# class Sensor:
#     def __init__(self) -> None:
#         self.in_range = False


class Sensor:
    def __init__(self, pin=18, debug=True) -> None:
        self.in_range = False
        if not debug:   
            self.sensor = MotionSensor(pin=pin)
            self.sensor.when_motion = self.motion_detected
            self.sensor.when_no_motion = self.no_motion_detected

    
    def motion_detected(self):
        self.in_range = True
        print("Motion detected.")

    
    def no_motion_detected(self):
        self.in_range = False
        print("No motion detected.")