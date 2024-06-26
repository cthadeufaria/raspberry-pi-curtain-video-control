import threading
from time import sleep

from video import Video
from sensor import Sensor
from curtain import Curtain

# class Sensor():
#     def __init__(self, trigger, echo):
#         self.in_range = False
#         self.idle_time = 0
    
#     def listen(self):
#         while True:
#             print("Sensor listening")
#             sleep(1)


def main():
    sensor = Sensor(trigger=18, echo=24)
    video = Video('flaminghott.mp4')
    curtain = Curtain(video, sensor)

    while True:
        print(curtain.current_state)
        threading.Event().wait(1)



if __name__ == "__main__": 
    main()