#This code is meant to generate desired behaviours from a behaviour record
# Takes in:
# # The behaviour records file name
# # The desired behaviours
# # The number of runs for each behaviour
# Outputs:
# # A png file representing the linear morph
# The image represents the linear morph by colouring each region of 
import os
import libFBCAGen
import linecache
import math

#This function parses the text data generated by 
def convTextListToList(listAsText):
    importantStuff=[]
    importantStuff=listAsText.split(",")
    importantStuff[0]=importantStuff[0].split("[")[1]
    l=len(importantStuff)
    importantStuff[l-1]=importantStuff[l-1].split("]")[0]
    importantStuff=[float(i) for i in importantStuff]
    return(importantStuff)

##DEFINITIONS OF STUFF
d=[];d=os.getcwd()+"/"
#defintions for FBCA generation
libFBCAGen.CALength=20 #Length of the generated image (for min use 5)
libFBCAGen.CAWidth=20 #Width of the generated image (for min use 4)
libFBCAGen.useImages=1 #checks if you want images This is annoying
libFBCAGen.numOfGens=20 #number of generations
libFBCAGen.numOfStates=2 #number of states (good until 10)
CAMapInit=[]
borderLambdas=[]
CAMapInit=libFBCAGen.initCA(CAMapInit) 

##START
morphRecord = open("morphPortrait record Two at 1000 rand(4)", "r")
#loops through files
sM1=[];sM2=[];lambdas=[];levelMap=[];splits=[]
for idx,line in enumerate(morphRecord):
    if idx == 0:
        splits=line.split("sMs")
        sM1=convTextListToList(splits[1])
        sM2=convTextListToList(splits[2])
    else:
        splits=line.split(" ")
        lambdas.append(float(splits[len(splits)-2]))
for lamb in lambdas:
    sMCur=libFBCAGen.genMorphSM(sM1,sM2,lamb)
    levelMap=libFBCAGen.generateFBCA(sMCur,d,CAMapInit,str(lamb))


