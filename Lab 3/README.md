# You're a wizard, [Nicole]

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Lab%203/IMG_0667.jpg)

## Share your idea sketches with Zoom Room mates and get feedback

Brian: first i will say, it was a bit hard to understand her voice, in the first part (before you said your ID number) .... Also if the system didnt recognize the ID, it should ask the user to try again before asking the user to re-register

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

We use two buttons (red and green) as the sensors and have the speaker and the microphone connected to the Pi to mimic the medical hotline system. The goal is to make appointment with the doctors autonomously. The system will ask questions like “Have you registered before?”, “What’s your phone number?” and etc. The participant can press the green button for yes and the red button for no, and can also speak to the microphone to answer the question.

https://drive.google.com/file/d/1LtZDsXPwL0k3kdAggsy1rjUuUYvEcYX0/view?usp=sharing

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
Worked well: The instruction the system performed was pretty clear and easy to follow. At first we thought the automated voice was too harsh and hard to understand, so we were easily able to switch to a voice from the demo that we thought was better.

Not worked well: Because we don't know how long it will take for someone to respond, the time period for participants to respond between some questions are too short. We tried to play with the speech to text functionality but we couldn't get it to work accurately at all, so we hard coded the pauses the system took where it would actually be waiting for someone to respond.


### What worked well about the controller and what didn't?

Worked well: Easy to use. We used a lot of the text to speech functionality to make sure the user knew exactly what to expect and how to interact with the system.

Not worked well: Sometimes the buttons don’t work. We were having a hard time getting the Qwiic buttons to accurately display as outputs, even after using i2cdetect. It seemed to connect on and off and randomly, which we tried to troubleshoot but couldn't find a good explanation for.


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

We found it hard to make the system to have a natural conversation as a human and there are some specific verbal cues that we have't captured. For instance, the change in volume and in tone can change the dynamic of the conversation. Additionally, it would have really helped to use the speech to text functionality as it would help guide the conversation more accurately. We are still trying to figure that out.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

There can be a screen showing what information has the hotline recorded or a live transcript. It could also be useful to sense the tone of the individual interacting with the automated machine to gauge for any misunderstandings or frustrations they might have with the system, so we can iterate on it and make it more user friendly.
