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

We’ve created a dance dance revolution game. The easy setting is gentle enough for toddlers to play, so if they are just beginning to learn their directional signs. We’ve used sensors and the wires to facilitate capacitive touch, and we make use of the text to speech to have a voice read out the instructions, and let you know how well you are doing in the game. We’ve modeled this against the popular dance dance revolution games seen at many arcades. Only our version is the finger version, instead of the full body dance version. Players get three lives - once they hit three wrong moves, the game is over. 

2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

We started designing the prototype with only the left and right buttons. First, we just used paper to design the display. We drew a dance floor and pretended the sensors were attached. And because this is a game designed for fingers, we had to make sure the left and right sensors were close enough that the player didn't need to significantly move during gameplay, but also far enough to provide a challenge. When designed the box where the pi would sit, we needed to make sure it was at a good position where the player wasn't sitting awkwardly in order to see the screen and play the game at the same time, but we also wanted to make sure we hid all the wires and bits and pieces behind the scenes. 

![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/1.png?width=1500&height=1100)

Then we advanced our prototype to have the up and down buttons (image is showing below) and rearrange the wires behind so that the wires don't get crossed over each other. We also upgraded the display so it looked more like a scaled down version of real life DDR. This includes the multicolored dance floor. To be more interactive, we added the sound effects right after each round. For instance, if the player makes the correct move, the device will say something like "Good job!", and if the player makes a mistake, the device will say "Nonono, try again." We used text to speech to create a better user experience, and had a narrator walking the game player first through the instructions and procedure of the game, and then helping them through the game and letting them know how they were doing. We took into account a couple different types of accessibility features by including speech, but also text on the screen of the pi which provided the same detail and functionality as the voice, so to provide for the hearing impaired as well. We also gave players 3 lives instead of 1 so they are not too frustrated by ending the game with only one mistake and are willing to stay longer in the game. We also included, to simulate the real life version of DDR better, moves that incorporated more than one direction (like tapping up and left at the same time). 

![alt text](https://github.com/nicole-zy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/prototype.png?width=1500&height=1100)

Our code is in code.py

3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)

We are demoing the one player version here - but the two player mode allows two players to rally against each other. 
Here is the demo in action. https://drive.google.com/file/d/16Im6LzqkTqIcfEQMOxO5LTp1bfeqlAMs/view?usp=drivesdk

4. Reflections on process (What have you learned or wish you knew at the start?)

The lesson we learned is that we should put ourselves in user's shoes and think like users. For example, the game used to just show the instruction "left" or "right" in each round in text and says "game over" when the player makes one mistake, and we thought it was good enough. However,  after we tested the game out on several players, the common feedback was that it's hard to know if the player makes the right move or not when the same instruction showing consecutively. For instance, the "left" sign shows in two rounds back to back. Therefore, we advanced the system by giving immediate feedback in each round that the device speaks out either "Right" or "Wrong" depending on the player's move. Additionally, in further iterations we'd like to create a larger scale version of the game. We were constrained to the size of the pi screen for this process, which is why we created a "finger" version of DDR. Using the materials and sensors we have, scaling the system bigger to create an actual full body version of DDR would be useful, especially when playing with more than one player, and it would make the system's user experience better because they wouldn't be confined to looking at and trying to read from a small screen. We also tried to incorporate adding music, but it was hard to include a sound that would fit well with the timings, since we don't specify a time limit for the user to tap an arrow.

## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

Our team has Mehma Bhasin mkb229,Ahaan Parekh ap2397 and Nicole Zhang yz2778. Ahaan and Mehma were working on writing and advancing the code and Nicole was working on designing and making the prototype.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.
