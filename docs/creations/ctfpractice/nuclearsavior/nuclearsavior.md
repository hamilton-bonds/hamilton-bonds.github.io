# NuclearSavior
Oh no! An Atropian Officer just started the countdown to launch nukes at the Ahuristanis, and you are the only person that can save them!  Unfortunately, you just knocked out the Atropian Officer and have only 2 hours until the nukes are headed towards your allies.  You make your way to the control room.

You are faced with a 16x16 panel of buttons that you must push in a certain order, like in the diagram below:
```
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
[o][o][o][o][o][o][o][o][o][o][o][o][o][o][o][o]
```
You must press 16 of the buttons in a certain order to get the flag.  Another way of visualizing the buttons is:
```
00-0F
10-1F
...
E0-EF
F0-FF
```
As if things couldn't get any worse, the button order resets after 3 incorrect guesses.  Despite your misfortune, you do have something going for you: the Atropian Officer left the source code that generates the algorithm!  Write a program that gets you the password for the encrypted flag file so you can stop the countdown!

*NOTE*: IF YOU ARE NOT RUNNING THIS ON A SERVER SEPARATE FROM THE USER, INCLUDE encthis.txt (the answer) IN YOUR FILES BUT DO NOT CAT PREMATURELY
- Problem Riles: [nuclearsavior.py](https://hamilton-bonds.github.io/creations/ctfpractice/nuclearsavior/nuclearsavior.py),[README.txt](https://hamilton-bonds.github.io/creations/ctfpractice/nuclearsavior/README.txt)
- Solution Files: [ns_solution.py](https://hamilton-bonds.github.io/creations/ctfpractice/nuclearsavior/ns_solution.py),[encthis.txt](https://hamilton-bonds.github.io/creations/ctfpractice/nuclearsavior/encthis.txt)
