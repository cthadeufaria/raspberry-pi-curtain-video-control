from time import sleep
import threading

from sensor import Sensor
from video import Video



def main():
    in_range = True
    # sensor = Sensor(trigger=18, echo=24)
    video = Video('flaminghott.mp4')

    # sensor_thread = threading.Thread(target=sensor.listen)
    video_thread = threading.Thread(target=video.play)
    
    # sensor_thread.start()
    video_thread.start()

    while True:
        sleep(0.5)

        # print("Distance: {} cm".format(sensor.distance))
        print("Looping...")

        if in_range: # if sensor.in_range:
            video.set_playing(True)
        else:
            video.set_playing(False)


if __name__ == "__main__": 
    main()