# video-merger-for-basketball

I am a huge fan of automation, and I was wondering if there was a way to either move a camera using computer vision to see what part of the court the game is being played.

Therefor I emailed Dave (http://davidrhoffman.net) from pyimagesearch.com (awesome blog) to ask whats the easiest way of doing this. He got me in to the thought of analysing both sides of the court and then streaming the side with the most movement. I am now finished with the software who can merge the two videos into one file remaining only game footage, no "useless" video.

Thanks Dave and Adrian from Pyimagesearch! (https://www.pyimagesearch.com/)

I could not have done this without this blogpost: https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/ again thanks!

If you record the two sides of a basketball game, this repository will merge it to one video, using frames where the play happens.
