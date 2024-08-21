from config import *
import cv2
import asyncio



class Video():
    def __init__(self, filename):
        self.video_path = VIDEO_PATH + filename
        self.finished = False
        cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        self.frames = 0
        self.last_frame = 0
        self.play_direction = 1
        self.playing = False

        self.get_total_frames()


    def get_total_frames(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()
        else:
            self.frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.release()


    async def play(self):
        cap = cv2.VideoCapture(self.video_path)

        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()

        while cap.isOpened():
            cap.set(cv2.CAP_PROP_POS_FRAMES, self.last_frame)
            ret, frame = cap.read()
            if not ret:
                cap.release()
                break

            cv2.imshow('Video', frame)

            if (cv2.waitKey(25) & 0xFF == ord('q')):
                cap.release()
                break
            
            if self.playing:
                self.last_frame += self.play_direction

            await asyncio.sleep(1/240)


    async def set_playing(self, playing):
        self.playing = playing


    async def set_play_direction(self, direction):
        self.play_direction = direction