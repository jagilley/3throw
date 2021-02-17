# IE3Throw

Seems like this might be very useful: https://github.com/BerkeleyAutomation/perception. Make sure to run `pip install -e .` when cd'ed into its folder, though, to install dependencies.

Also worth checkingsifej out, a different approach: https://github.com/af-3/Stereo_Vision

## Raspberry Pi Connection wiht laptop

boot up Raspberry Pi and run `ifconfig` to check ip address.

run `ssh pi@ipaddress` in terminal 

## Dependencies

*After cloning,* make sure to run `git clone https://github.com/davisking/dlib`, `git clone https://github.com/BerkeleyAutomation/perception`, and `git clone https://github.com/shantnu/Webcam-Face-Detect` from within the folder you just cloned. GitHub's handling of submodules (that is, repos within a repo) is not great.

## To run single-image face recognition

Run `python3 facial_recognition.py`

## To run realtime face recognition

Run `python3 Webcam-Face-Detect/webcam_cv3.py`

Drawing documentation for opencv
https://docs.opencv.org/2.4/doc/tutorials/core/basic_geometric_drawing/basic_geometric_drawing.html
https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html


Video streaming tutorial: get your camera to stream a video! https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html


Motor control: https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051

Potentially helpful stereo vision stuff
https://docs.opencv.org/3.1.0/dd/d53/tutorial_py_depthmap.html

Another stereo solution:
https://albertarmea.com/post/opencv-stereo-camera/

Very helpful Flask video streaming explanation:
https://blog.miguelgrinberg.com/post/video-streaming-with-flask

## activate opencv virtual environment
Run `source venv/bin/activate`
