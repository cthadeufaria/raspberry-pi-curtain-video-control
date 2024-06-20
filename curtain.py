from statemachine import StateMachine, State
import asyncio

from sensor import Sensor
from video import Video



class Curtain(StateMachine):
    closed = State('Closed', initial=True)
    opened = State('Opened')
    opening = State('Opening')
    closing = State('Closing')

    cycle = (
        closed.to(opening, cond="in_range") 
        | opening.to(opened, cond="video_end")
        | opened.to(closing, cond="not_in_range")
        | closing.to(opening, cond="in_range")
        | closing.to(closed, cond="video_beginning")
    )

    def __init__(self, video: Video, sensor: Sensor):
        self.video = video
        self.sensor = sensor
        super(Curtain, self).__init__()

        asyncio.create_task(self.sensor.listen())

        self.on_enter_closed()


    async def in_range(self):
        return self.sensor.in_range
    

    async def not_in_range(self):
        return (not self.sensor.in_range and self.sensor.idle_time > 5)
    

    async def video_end(self):
        return self.video.last_frame == self.video.frames - 1


    async def video_beginning(self):
        return self.video.last_frame == 0


    async def on_enter_opening(self):
        await self.video.set_playing(True)
        await self.video.set_play_direction(1)
        await self.video.play()
    

    async def on_enter_closing(self):
        await self.video.set_playing(True)
        await self.video.set_play_direction(-1)
        await self.video.play()


    async def on_enter_opened(self):
        await self.video.set_playing(False)
        await self.video.play()


    async def on_enter_closed(self):
        await self.video.set_playing(False)
        await self.video.play()