#Generates a 'phase portrait' for a linear moprh of two score matrices
#This is done by checking for weak behavioural equivalence by directly comparing L_gs 
#done in python because the phase portrait work is done in python

#imports of libraries
from PIL import Image
import random
import math
import os 
import numpy

#each cell has a score and a state (calculated by standard FBCA methods)
class CACell:
    state=0
    score=0
   
#FBCA are described by their score matrix (decided by x and y but its useful to be able to plot later) and its resulting level map 
#That being said, the level map and score matrix are technically decided y the global inits above
class Fbca:
    levelMap=[]
    scoreMatrix=[]
    behaviourNum=0
#global inits
morphRes=1000 #Resolution of morph 
imageHeight=100 #Height of the generated image 
numOfGens=20 #number of generations to check equi-behaviours (20 is a good default?)
numOfStates=4 #number of states (good until 10)
random.seed(1)  #1 for held   

sM1=[0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596]
sM2=[0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,]
sMs=[sM1,sM2] #morphed guys
# sMs=[[0.320205,0.952292,0.351335,0.837774],[0.390741,0.728013,0.614486,0.378596]]
CALength=20
CAWidth=20

#COMMENT (works)
def determineSteps(sMs,resolution,stepSizes):
    for entry in range(len(sMs[0])):
        stepSizes.append(abs(sMs[0][entry]-sMs[1][entry])/resolution)
    return(stepSizes)

def initCA(CAMap):
    #fills empty list with random states (x then y: downward strips)
    for x in range(0,CALength):
        holder=[]
        for y in range(0,CAWidth):
            holder.append(CACell())
            holder[y].state=random.randint(0,numOfStates-1)
        CAMap.append(holder)
    return(CAMap)
def generateSM(x,oldSM,stepSizes):
    newSM=[]
    for idx,entry in enumerate(oldSM):
        newSM.append(float(entry+x*stepSizes[idx]))
    return(newSM)
def copyOver(CAMapInit):
    CAMap=[]
    for x in range(0,CALength):
        holder=[]
        for y in range(0,CAWidth):
            holder.append(CACell())
            holder[y].state=CAMapInit[x][y].state
        CAMap.append(holder)
    return(CAMap)
def copySM(sM):
    holder=[]
    for x in sM:
        holder.append(x)
    return(holder)

def updateMap(CAMap,scoreMatrix):

    #To start, hardcode the neighbourhood. It is a list of tuples representing the x and y offset from the center square
    neighbours=[]
    neighbours.append((0,1))#top (1 up)
    neighbours.append((0,-1))#bot (1 down)
    neighbours.append((-1,0))#left (1 left)
    neighbours.append((1,0))#right (1 right)
    for x in range(0,CALength):
        for y in range(0,CAWidth):
            #Need to get score from center square and its neighbours.
            row=0; row = CAMap[x][y].state*numOfStates #the center colour determines the row of the score matrix used 
            col=0; #the col of the score matrix used will depend on the  neighbours state

            CAMap[x][y].score=0 #resets center square's score

            #sums scores
            for z in neighbours:
                col=CAMap[(x+z[0])%CALength][(y+z[1])%CAWidth].state #mod used to connect edges
                CAMap[x][y].score+=scoreMatrix[row+col] #since the score matrix is a list, row+col gives the correct entry
    #start by copying the map
    CAMapCopy=copyOver(CAMap)
    #for every cell, find the highest score among neighbours
    for x in range(0,CALength):
        for y in range(0,CAWidth):
            #NOTE: We give priority to the center square on ties. Priority continues up with the last defined neighbour to have the worst priority
            bigScore=0;bigScore=CAMap[x][y].score
            #compares neighbours scores, reassigning bigScore and state if someone is bigger
            for z in neighbours:
                if(bigScore<CAMap[(x+z[0])%CALength][(y+z[1])%CAWidth].score):
                    bigScore=CAMap[(x+z[0])%CALength][(y+z[1])%CAWidth].score
                    CAMapCopy[x][y].state=CAMap[(x+z[0])%CALength][(y+z[1])%CAWidth].state
    return(CAMapCopy)

def genLG(sM,numOfGens,CAMapInit):
    CAMap=[]
    CAMap=copyOver(CAMapInit)
    for n in range(numOfGens):
        CAMap=updateMap(CAMap,sM)
    print("Finished "+str(sM))
    return(CAMap)
#MAIN 
#COMMENT
morph=[] 
CAMapInit=[]
CAMapInit=initCA(CAMapInit)
stepSizes=[]
stepSizes=determineSteps(sMs,morphRes,stepSizes)
print("Generating score matricies and L_gs")
for x in range(morphRes+1):
    sM=generateSM(x,sMs[0],stepSizes)
    morph.append(Fbca())
    morph[len(morph)-1].scoreMatrix=copySM(sM)
    morph[len(morph)-1].levelMap=genLG(sM,numOfGens,CAMapInit)
    morph[len(morph)-1].x=x    
print("Comparing FBCA via weak behavioural equivalence")
ignoreList=[] #used to avoid double counting for the behaviours
behaviourNum=0
for idx1,fbcaCur in enumerate(morph):
    ignore=False
    for val in ignoreList: #checks if we should ignore it by checking the ignoreList
        if idx1 == val:
            ignore=True
    if ignore==False:
        for idx2,fbcaNew in enumerate(morph):
            isSame=True
            for x in range(CALength):
                for y in range(CAWidth):
                    if fbcaNew.levelMap[x][y].state != fbcaCur.levelMap[x][y].state:
                        isSame=False
            if isSame == True: #if they are the same
                fbcaNew.behaviourNum=behaviourNum
                ignoreList.append(idx2)
        fbcaCur.behaviourNum=behaviourNum
        ignoreList.append(idx1)                
    behaviourNum+=1
    print("Finished comparison on "+str(idx1)+" out of " +str(len(morph)-1)+str(" total"))

print("Generating Image")
imageColourStep=(255*3)/(behaviourNum+1)
im= Image.new('RGB', (morphRes+1, 1))
for x in range(morphRes):
    r=int(imageColourStep*morph[x].behaviourNum)
    g=int(imageColourStep*morph[x].behaviourNum)
    b=int(imageColourStep*morph[x].behaviourNum)
    im.putpixel((x,0),(r,g,b))
# directory = os.getcwd()+"/"+str(fileName)+"/"
im.save("phaseMorph of "+str(numOfStates)+".png")#+str(sMs[0])+" "+str(sMs[1])+".png")
    