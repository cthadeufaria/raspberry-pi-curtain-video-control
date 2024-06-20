import statemachine
import asyncio

from video import Video
from sensor import Sensor
from curtain import Curtain

# class Sensor():
#     def __init__(self, trigger, echo):
#         self.in_range = False
#         self.idle_time = 0



async def main():
    sensor = Sensor(trigger=18, echo=24)
    video = Video('flaminghott.mp4')
    curtain = Curtain(video, sensor)

    while True:
        await asyncio.sleep(0.5)
        try:
            print(curtain.current_state)
            await curtain.cycle()
        except statemachine.exceptions.TransitionNotAllowed as e:
            print(e)

        # print("Distance: {} cm".format(sensor.distance))
        


if __name__ == "__main__": 
    asyncio.run(main())