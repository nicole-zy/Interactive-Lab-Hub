# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project Github page set up - May 3

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12

Final Project Documentation due - May 19



## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
Your project is to design and build an interactive device to suit a specific application of your choosing. 

## Deliverables

1. Documentation of design process

We’ve created a DDR game. The easy setting is gentle enough for toddlers to play, so if they are just beginning to learn their directional signs. We’ve used sensors and the wires to facilitate capacitive touch, and we make use of the text to speech to have a voice read out the instructions, and let you know how well you are doing in the game. We’ve modeled this against the popular dance dance revolution games seen at many arcades. Only our version is the finger version, instead of the full body dance version. Players get three lives - once they hit three wrong moves, the game is over. 
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/1.png?width=1500&height=1100)

2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

We started designing the prototype with only the left and right buttons. First, we just used paper to design the display. We drew a dance floor and pretended the sensors were attached. And because this is a game designed for fingers, we had to make sure the left and right sensors were close enough that the player didn't need to significantly move in during gameplay, but also far enough to provide a challenge. When designed the box where the pi would sit, we needed to make sure it was at a good position where the player wasn't sitting awkwardly in order to see the screen and play the game at the same time, but we also wanted to make sure we hid all the wires and bits and pieces behind the scenes.

Then we advanced our prototype to have the up and down buttons (image is showing below) and rearrange the wires behind so that the wires don't get crossed over each other. To be more interactive, we added the sound effects right after each round. For instance, if the player makes the correct move, the device will say something like "Good job!", and if the player makes a mistake, the device will say "Nonono, try again." We also gave players 3 lives instead of 1 so they are not too frustrated by ending the game with only one mistake and are willing to stay longer in the game.
![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/prototype.png?width=1500&height=1100)

Our code is in code.py

3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)

We are demoing the one player version here - but the two player mode allows two players to rally against each other. 
Here is the demo in action. https://drive.google.com/file/d/16Im6LzqkTqIcfEQMOxO5LTp1bfeqlAMs/view?usp=drivesdk

4. Reflections on process (What have you learned or wish you knew at the start?)


## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.
