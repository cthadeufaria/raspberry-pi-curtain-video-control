from statemachine import StateMachine, State

from sensor import Sensor
from video import Video



class Curtain(StateMachine):
    closed = State('Closed', initial=True)
    opened = State('Opened')
    opening = State('Opening')
    closing = State('Closing')

    closed_to_opening = closed.to(opening, cond="in_range")
    opening_to_opened = opening.to(opened, cond="video_end")
    opened_to_closing = opened.to(closing, cond="not_in_range")
    closing_to_opening = closing.to(opening, cond="in_range")
    closing_to_closed = closing.to(closed, cond="video_beginning")


    def __init__(self):
        self.sensor = Sensor(trigger=18, echo=24)
        self.video = Video('flaminghott.mp4')
        super().__init__()


    def in_range(self):
        return self.sensor.in_range
    

    def not_in_range(self):
        return (not self.sensor.in_range & self.video.idle_time > 5)
    

    def video_end(self):
        return self.video.frame == len(self.video.frames) - 1


    def video_beggining(self):
        return self.video.frame == 0


    def on_enter_opening(self):
        self.video.set_playing(True)
        self.video.play_direction = 1

    
    def on_enter_closing(self):
        self.video.set_playing(True)
        self.video.play_direction = -1