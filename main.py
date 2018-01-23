
from detector import *
from recorder import Record
from sys import exit, argv


if len(argv) != 2:
    print("No output name selected")
    exit(1)
else:
    output_name = argv[1]

if output_name[-4:] != ".avi":
    print("Filname must be .avi")
    exit(1)

info = [["src/left.mp4", "left stream"], ["src/right.mp4", "right stream"]]
st1 = Detect(info[0][0], info[0][1])
st2 = Detect(info[1][0], info[1][1])

streams = [st1, st2]
values = [0, 0]

flip_treshold = 120
flip_countor = 15
last_selected = 0
diff_treshold = 3

index = None
mval = None

recorder = Record(output_name, 30.0, (640, 360))

while True:
    for stream, i in zip(streams, range(2)):
        if stream.read():
            stream.resize(640)
            if not stream.is_first_frame():
                stream.set_frame()
            values[i] = stream.detect()
    #print("%s: %f, %s: %f, diff: %f" % (info[0][1], values[0], info[1][1], values[1], abs(values[0] - values[1])))
    mval = max(values)
    index = values.index(mval)
    diff = abs(values[0] - values[1])
    if last_selected != index:
        if flip_countor > flip_treshold and diff > diff_treshold:
            flip_countor = 0
        else:
            if index == 0:
                index = 1
            else:
                index = 0

    flip_countor += 1
    last_selected = index
    streams[index].show(False)
    recorder(streams[index].rec())
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

for s in streams:
    s.release()
recorder.release()
cv2.destroyAllWindows()
