from statemachine import StateMachine, State
import threading

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
        self.sensor = sensor
        self.video = video
        super(Curtain, self).__init__()

        self.sensor_thread = threading.Thread(target=self.sensor.listen)
        self.sensor_thread.start()

        self.video_thread = threading.Thread(target=self.video.play)

        self.cycle_thread = threading.Thread(target=self.run_cycle)
        self.cycle_thread.start()

        self.on_enter_closed()


    def run_cycle(self):
        while True:
            try:
                self.cycle()
            except Exception as e:
                print(e)
            threading.Event().wait(1)


    def in_range(self):
        return self.sensor.in_range


    def not_in_range(self):
        return (not self.sensor.in_range and self.sensor.idle_time > 5)


    def video_end(self):
        return self.video.last_frame == self.video.frames - 1


    def video_beginning(self):
        return self.video.last_frame == 0


    def on_enter_opening(self):
        self.video.set_playing(True)
        self.video.set_play_direction(1)
        self.video_thread.start()


    def on_enter_closing(self):
        self.video.set_playing(True)
        self.video.set_play_direction(-1)
        self.video_thread.start()


    def on_enter_opened(self):
        self.video.set_playing(False)
        self.video_thread.start()


    def on_enter_closed(self):
        self.video.set_playing(False)
        self.video_thread.start()