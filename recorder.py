
import cv2
class Record:
    def __init__(self, name, fps, size):
        self._out = None
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self._out = cv2.VideoWriter(name, fourcc, fps, size)

    def __call__(self, frame):
        if self._out is not None:
            self._out.write(frame)
        else:
            assert False, "A recorder is not defined, use .record(name, fps, size)"

    def release(self):
        self._out.release()
