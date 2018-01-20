__author__ = 'Michael Johansen'

import tkinter as tk

def initMatrix(difficulty):
    set.delete("objects")
    counter = 0
    factors = []
    numEntities = 0
    facts = []

    inputfile = open('Puzzles/'+difficulty)
    for line in inputfile:
            if(not line.strip()):
                counter+=1
            else:
                if counter==0:
                    factors.append(line)
                elif counter==1:
                    numEntities = line
                else:
                    facts.append(line)
    for i in range(0,len(factors)):
        set.create_text(50, 90 + (i*50),text=factors[i], tags="objects")
    for i in range(0,len(facts)):
        set.create_text(400, 100+(50*len(factors))+17*i, text = facts[i], tags="objects")
    for i in range(0,int(numEntities)):
        set.create_text(((600/int(numEntities))*i)+200,60, text = i+1, tags="objects")

    inputBoxes = [[None for _ in range(len(factors))] for _ in range(int(numEntities))]
    width = (600/int(numEntities))
    height = 20
    heightMod = 70
    set.create_rectangle(125,70,275 ,90)

    for i in range(0,int(numEntities)):
        for j in range(0,len(factors)):
            print("k")
            #inputBoxes = set.create_rectangle(125+(i*(width)),heightMod+(j*height),125+((i+1)*width),heightMod+((j+1)*height), activefill="black", tags="objects")
            heightMod += 17


def onDifficultyClick(event):
    if(event.x<200):
        initMatrix('VeryEasy.txt')
    elif(event.x<400):
        initMatrix('Easy.txt')
    elif(event.x<600):
        initMatrix('Medium.txt')
    else:
        initMatrix('Hard.txt')

def initialize():
    set.create_text(100,20,activefill="gray",text="Very Easy",width="100",tags="veryEasy")
    set.create_text(300,20,activefill="gray",text="Easy",width="100",tags="Easy")
    set.create_text(500,20,activefill="gray",text="Medium",width="100",tags="Medium")
    set.create_text(700,20,activefill="gray",text="Hard",width="100",tags="Hard")
    set.create_line(0,40,800,40,width=3)

    set.tag_bind('veryEasy', '<ButtonPress-1>', onDifficultyClick)
    set.tag_bind('Easy', '<ButtonPress-1>', onDifficultyClick)
    set.tag_bind('Medium', '<ButtonPress-1>', onDifficultyClick)
    set.tag_bind('Hard', '<ButtonPress-1>', onDifficultyClick)

def callback(event):
    print("s")

if __name__ == "__main__":
    root = tk.Tk()
    #puzzle(root).pack(fill="both", expand=True)
    set = tk.Canvas(root, width = 800, height = 800, borderwidth=5, background = 'white')
    initialize()
    set.pack()
    set.bind("<Button-1>",callback)
    root.mainloop()

