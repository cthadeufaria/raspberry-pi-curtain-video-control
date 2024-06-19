from config import *
import cv2



class Video:
    def __init__(self, filename):
        """
        Initializes the Video class.
        """

        cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        self.playing = False
        self.video_path = VIDEO_PATH + filename
        self.frames = 0
        self.last_frame = 0
        self.play_direction = 1
        self.finished = False

        cap = cv2.VideoCapture(self.video_path)
        
        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()
        
        else:
            self.frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        cap.release()


    def play(self):
        """
        Plays the video.
        """

        while True:
            if self.playing:           
                cap = cv2.VideoCapture(self.video_path)

                if not cap.isOpened():
                    print("Error: Could not open video.")
                    exit()

                while (self.last_frame >= 0 or self.last_frame < self.frames) and self.playing == True:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, self.last_frame)
                    ret, frame = cap.read()
                    
                    if not ret:
                        print("Reached the end of the video or failed to read the frame.")
                        self.finished = True
                        break

                    cv2.imshow('Video', frame)

                    if cv2.waitKey(33) & 0xFF == ord('q'):
                        break

                    self.last_frame += self.play_direction


    def set_playing(self, playing):
        if playing:
            self.playing = True
        else:
            self.playing = False