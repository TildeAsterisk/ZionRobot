# ZionRobot
This is a ROS packages that uses the kinect as the head of your robot.
Make sure you have installed the `freenect_stack` and `kinect_aux` ROS packages.

~*~*~* Start the robot with the following command: *~*~*~
`roslaunch zionrobot zionrobot.launch`


| Spec Type:    | Info:          |
| -------------:| -------------- |
| OS:           | Ubuntu 20.04.5 |
| ROS Version:  | Noetic         |
| ROS Packages: | freenect_stack |
| ''            | kinect_aux     |
| ''            |                |
| ''            | googleassistant?|
| ''            | AI ?           |
| ''            | Mapping?       |





``` 
My Dev Creations Commands:
==========================
(~*) my Python3.8.10 virtual environment
source /~\*/bin/activate

roslaunch zionrobot zionrobot.launch

freenect-[TAB]
roslaunch freenect-[TAB]

source ~/env/bin/activate
googlesamples-assistant-pushtotalk

googlesamples-assistant-hotword --credentials /home/tildeasterisk/Documents/client_secret

googlesamples-assistant-pushtotalk --project_id [___] --device_model_id [___] 

Terminal Clipboard:
===================

/home/tildeasterisk/env/bin/googlesamples-assistant-pushtotalk

roslaunch freenect_launch freenect.launch depth_registration:=true

roslaunch opencv_apps face_detection.launch use_camera_info:=true

roslaunch cv_basics cv_basics_py.launch

# Dependencies are listed here
#freenect_stack == 0.4.3
#kinect_aux == 0.0.1
```
