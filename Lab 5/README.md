# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

We played around with a few of the different detection properties. 

Here is us trying out the contour:
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Lab%205/contour.png?width=1500&height=1100) 

Here we tried out the face detection:
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Lab%205/face.png?width=1500&height=1100)

Here we tried simple object detection with a water bottle:
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Lab%205/object.png?width=1500&height=1100)

Here we experimented with the flow. It took us a while to understand that it was following the camera movement, instead of an object or person movement:
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Lab%205/flow.png?width=1500&height=1100)



#### Filtering, FFTs, and Time Series data. (beta, optional)

Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B
### Construct a simple interaction.


Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Lab%205/modified.png?width=1500&height=1100)
We used the face detection. The device detects whether the participant's eyes are open or not. If the participant's eyes are open, the device will ask "Your eyes are open, take a pic?". Then the participant can take a picture by pressing the button

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. When does it what it is supposed to do? 
The device asks if the participant to take a picture when the participant opens the eyes.
2. When does it fail? 
When the participant's eyes are closed, or obstructed, or a face is not detected.
3. When it fails, why does it fail? 
The main idea behind the system is to detect a face, and to detect eyes so that a good picture can be taken. This will fail, correctly, if this conditions are not met. 
4. Based on the behavior you have seen, what other scenarios could cause problems? 
If the user, for example, makes funny faces on purpose for the picture, it is likely that the detection software will not prompt the user or allow them to take a picture because the conditions are not met. Also, because of the nature of the code, it is also likely that the prompt to take a picture shows up for less than a second at a time because the rendering takes a while. This would not be user friendly as it would end up being harder for the user to take a picture.

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?
The user is aware of the conditions that need to be met before they are able to take a picture. However, the uncertainty of the speed at which the detection is performed can lead to issues during production.
2. How bad would they be impacted by a miss classification?
The consequences wouldn't be terrible if a picture was taken when the user wasn't ready, as deleting a picture is fairly straightforward. If the detection software takes too long and the user is unable to take a picture all together, that would be a pretty negative impact as the purpose of the system as a whole would be defeated.
3. How could change your interactive system to address this?
We could change our system to automatically snap pictures when conditions are met. When the user tries to take a picture and they have to move to click the button, sometimes the face form alters and if the detection software processes that too slowly and cannot redirect the face and eyes fast enough, it would cause the picture not to be taken. With automatic picture taking, this fault is taken care of.
4. Are there optimizations you can try to do on your sense-making algorithm.
We could include algorithms from the teachable machines portions to account for more conditions that could be met in order to take a picture. This could include making sure masks are off, etc.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
We can use our system to make it easier for people to snap pictures when their hands are being used or when they are far from the camera.
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

Unstable camera: https://drive.google.com/file/d/1_HV1e8nz-4Y74jzlPzqfG28yZLCzgmdI/view?usp=sharing

The participant is too far away: https://drive.google.com/file/d/1KzVB4p1OHxm7lzeOrHMKOpyz21vZPGJK/view?usp=sharing


### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.
when the camera is stablized, the quality of the detection improves significantly.
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Lab%205/stable.jpg?width=1500&height=1100)



