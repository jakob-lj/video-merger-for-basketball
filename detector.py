
import imutils
import cv2

class Detect:
    def __init__(self, path, name):
        self._path = path
        self._name = name
        self._cap = cv2.VideoCapture(self._path)
        self._frame = None
        self._gray = None
        self._first_frame = None
        self._out = None

    def show(self, real_name):
        if real_name:
            cv2.imshow(self._name, self._frame)
        else:
            cv2.imshow("Main", self._frame)

    def read(self):
        (self._grabbed, self._frame) = self._cap.read()
        if self._grabbed:
            self._gray = cv2.cvtColor(self._frame, cv2.COLOR_BGR2GRAY)
        return self._grabbed

    def resize(self, size):
        self._frame = imutils.resize(self._frame, width=size)

    def detect(self):
        fd = cv2.absdiff(self._first_frame, self._gray)
        th = cv2.threshold(fd, 25, 255, cv2.THRESH_BINARY)[1]
        th = cv2.dilate(th, None, iterations=2)
        (_, countors, _) = cv2.findContours(th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        x_points = []
        for countor in countors:
            if cv2.contourArea(countor) < 600:
                continue
            (x, y, w, h) = cv2.boundingRect(countor)
            x_points.append(x)
        return len(x_points)

    def set_frame(self):
        if self._gray is None:
            return False
        else:
            self._first_frame = self._gray
            return True

    def is_first_frame(self):
        if self._first_frame is None:
            return False
        else:
            return True

    def release(self):
        self._cap.release()

    def rec(self):
        return self._frame
