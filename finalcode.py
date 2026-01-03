###################################################################
# Author: Luning Wang
# Purpose: This program animates fireworks shooting into the sky at 
#          night using arrays 
###################################################################

#Initialize Tkinter with these
from tkinter import *
from math import *
from time import *
from random import *

myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()

# typing shortcuts
oval = screen.create_oval
rect = screen.create_rectangle
line = screen.create_line
poly = screen.create_polygon
text = screen.create_text
arc = screen.create_arc

# creates sky gradient
y = 0
y2 = 15.5
skyOpt = [
"#000000",
"#010001",
"#020101",
"#030102",
"#040203",
"#050204",
"#060305",
"#070406",
"#080407",
"#090508",
"#0a0509",
"#0b060a",
"#0c060b",
"#0c070c",
"#0d070d",
"#0e080e",
"#0e090f",
"#0f0910",
"#0f0a10",
"#0f0a11",
"#100b12",
"#100c13",
"#100c14",
"#100d15",
"#110e15",
"#110e16",
"#110f17",
"#110f18",
"#111018",
"#111019",
"#11111a",
"#11121a",
"#11121b",
"#11131b",
"#10131c",
"#10141d",
"#10141d",
"#10151e",
"#0f151e",
"#0f161f"]
# prints the sky in a gradient 
for sky in range (1,40):
    skyColour = (skyOpt[sky%40])
    rect (0,y,905,y2, fill = skyColour, outline = skyColour)
    y = y + 15.5
    y2 = y2 + 15.5
    
# draws the stars
for i in range(300):
    x = randint(0, 800)
    y = randint(0, 600)
    r = randint(1,4)
    oval(x,y, x+r, y+r, fill = "#767b82", outline="#767b82")

# sets the possible colours for fireworks
colourOpt = ["#a8ded3",
"#6679bf",
"#ce89c3",
"#eaf9f8",
"#dc8283",
"#fda423",
"#f3a333",
"#f28535",
"#cf8ac4"]

# sets the number of firework waves and how big the explosion is
ballNum = 50
fireworkWaves = 5

# for loop to run multiple waves of fireworks
for wave in range(fireworkWaves): 
    # randomly picks a number of fireworks for each wave
    fireworkNum = randint(2,5) 
    
    # empty arrays for firework lines
    startlinex = []
    startliney = []
    stopliney = []
    startlinespeed = []
    startlinelength = []
    linedrawings = []
    linestop = []
    
    # array for firework colours
    colours = []
    
    # empty arrays for firework balls/firework explosion
    newXposition = []
    newYposition = []
    explodeXlist = []
    explodeYlist = []
    ballDrawingslist = [] 
    startingX = []
    startingY = []
    ballxSpeed = []
    ballySpeed = []
    ballRadius = []
    

    # fills empty firework line arrays with values 
    for i in range(fireworkNum):
        startlinex.append(randint(50,750))
        startlinespeed.append(randint(2,5))
        startlinelength.append(randint(50,100))
        linedrawings.append(0)
        linestop.append(randint(100,200))
        startliney.append(600)
        
        # calculates where the line stops
        stopliney.append(startliney[i] - startlinelength[i])
        
        # randomly picks 3 colours for this firework's explosion
        threeColours = sample(colourOpt, 3)
        colours.append(threeColours)
        
        # empty arrays for firework balls/firework explosion
        explodeXlist.append([])
        explodeYlist.append([])
        startingX.append([])
        startingY.append([])
       
    
    # animates the firework line shooting up into the sky
    for f in range(125): 
        for i in range(fireworkNum):
            linedrawings[i] = line(startlinex[i], startliney[i], startlinex[i], stopliney[i], fill = colours[i][0], width = 5)
            
            # changes speed of the line
            startliney[i] = startliney[i] - startlinespeed[i]
            stopliney[i] = startliney[i] - startlinelength[i]
            
    
            # stops the firework if it gets too close the top of the screen
            if stopliney[i] < linestop[i]:
                startlinespeed[i] = 0
                
        # updates the screen
        screen.update()
        sleep(.003)
        
        #  deletes the fireworks
        for i in range(fireworkNum):
            screen.delete(linedrawings[i])
    
    # sets the intital positions for the explosion that happens at the top of the firework
    newXposition = startlinex 
    for i in range(fireworkNum):
        newYposition.append(stopliney[i])
        
    # fills empty firework ball/explosion arrays with values
    for n in range(fireworkNum):
        explodeXlist.append([])
        explodeYlist.append([])
        ballDrawingslist.append([])
        ballxSpeed.append([])
        ballySpeed.append([])
        ballRadius.append([])
        
        # fills empty firework ball/explosion arrays with values
        for i in range(ballNum):
            explodeXlist[n].append(newXposition[n])
            explodeYlist[n].append(newYposition[n])
            startingX[n].append(newXposition[n])
            startingY[n].append(newYposition[n])
            
            # randomly picks a radius for each ball
            radius = randint(5,15)
            ballRadius[n].append(radius)
            
            # randomly picks a speed for each ball
            ballxSpeed[n].append(randint(-5,5))
            ballySpeed[n].append(randint(-5,5))
            
            # creates each ball with one of the 3 colours and stores it
            ball = oval(explodeXlist[n][i] - radius, explodeYlist[n][i]-radius, explodeXlist[n][i]+radius, explodeYlist[n][i]+radius, fill = colours[n][i%3], outline = colours[n][i%3])
            ballDrawingslist[n].append(ball)
    
    # animate the explosions
    for f in range(100):
        for n in range(fireworkNum):
            for i in range(ballNum): 
                # calculates distance traveled by each ball
                distance = hypot(explodeXlist[n][i] - startingX[n][i], explodeYlist[n][i] - startingY[n][i])
                            
                # stops the ball if it goes past a certain distance
                if distance > 100: 
                    ballxSpeed[n][i]=0
                    ballySpeed[n][i]=0
                    if ballDrawingslist[n][i] is not None: 
                        screen.delete(ballDrawingslist[n][i])
                        ballDrawingslist[n][i] = None
                        
                # increases the speed of each ball
                if ballxSpeed[n][i] != 0 or ballySpeed[n][i] != 0: 
                    explodeXlist[n][i] = explodeXlist[n][i] + ballxSpeed[n][i]
                    explodeYlist[n][i] = explodeYlist[n][i] + ballySpeed[n][i] 
                    # updates the coordinates of the balls
                    if ballDrawingslist[n][i] is not None: 
                        screen.coords(ballDrawingslist[n][i], explodeXlist[n][i]-ballRadius[n][i], explodeYlist[n][i]-ballRadius[n][i], explodeXlist[n][i]+ballRadius[n][i], explodeYlist[n][i]+ballRadius[n][i])
          
    #   updates the screen
        screen.update()
        sleep(0.03)
    # deletes any remaining balls after the animation loop
    for n in range(fireworkNum):
        for i in range(ballNum):
            if ballDrawingslist[n][i] is not None:
                screen.delete(ballDrawingslist[n][i])
    
    
#Grid lines
# spacing = 50
# for x in range(0, 800, spacing): 
#     screen.create_line(x, 25, x, 600, fill="white")
#     screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")

# for y in range(0, 600, spacing):
#     screen.create_line(25, y, 800, y, fill="white")
#     screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")

screen.mainloop()