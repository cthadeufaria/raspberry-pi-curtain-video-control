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


    def __init__(self):
        super().__init__()
        self.sensor = Sensor(trigger=18, echo=24)
        self.video = Video('flaminghott.mp4')
        self.video_task = None
        self.sensor_task = asyncio.create_task(self.sensor.listen())


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


    async def on_enter_closing(self):
        await self.video.set_playing(True)
        await self.video.set_play_direction(-1)


    async def on_enter_opened(self):
        await self.video.set_playing(False)


    async def on_enter_closed(self):
        await self.manage_task()


    async def manage_task(self):
        if self.video_task is not None:
            self.video_task.cancel()
        self.video_task = asyncio.create_task(self.video.play())
        await asyncio.run(self.video_task)