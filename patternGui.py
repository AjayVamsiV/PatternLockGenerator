import turtle
import random
import time

def addpoint(lis1,lis2,pos):
    lis2.append(lis1[pos])
    lis1.pop(pos)

def chkCnd(a,b,vis):#For checking the valid paths
    if(abs(a-b)!=6 and a+b!=10 and a+b!=4 and a+b!=16):
        return True
    elif((a+b)/2 in vis):
        return True
    else:
        return False

def getPattern(lis1):
    a = lis1[:]
    b = []
    i = 0
    while(i < PatternLen):
        eleindex = random.randint(0,len(a)-1)
        #print(nonvis[eleindex],vis)
        if(b == []):                           #First point
            addpoint(a,b,eleindex)
        else:
            if(chkCnd(b[-1],a[eleindex],b)):
                addpoint(a,b,eleindex)
            else:
                i-=1
        i+=1
    return b
def draw():
    for n in range(PatternLen):
        i.goto(p[l[n]])
    time.sleep(2)
    i.clear()

nonvis = [1,2,3,4,5,6,7,8,9]
PatternLen = 9
numPatterns = 7

p = {1:(0,0),2:(50,0),3:(100,0),4:(0,-50),5:(50,-50),\
     6:(100,-50),7:(0,-100),8:(50,-100),9:(100,-100)}

k = turtle.Turtle()
for j in range(9):
    k.penup()
    k.goto(p[j+1])
    k.setheading(270)
    k.forward(-5)
    k.setheading(180)
    k.forward(2.5)
    k.pendown()
    k.circle(5)

i = turtle.Turtle()
i.color("cyan")
i.pensize(3)
for n in range(numPatterns):
    l = getPattern(nonvis)
    i.penup()
    i.goto(p[l[0]])
    i.pendown()
    draw()

turtle.done()
