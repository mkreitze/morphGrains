#This code is meant to generate desired behaviours from a behaviour record
#Takes in:
#   The behaviour records file name
#   The desired behaviours
#   The number of runs for each behaviour
import os
import libFBCAGen
import linecache
import math

#Takes two lambdas (as floats) and generates midpoint
#literally (lambda1+lambda2)/2
def getMid(lambda1,lambda2):
    midLamb=(lambda1+lambda2)/2
    return(midLamb)

#This function parses the text data 
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
curSide=["Left","Right","Middle"]
#defintions for FBCA generation
libFBCAGen.CALength=20 #Length of the generated image (for min use 5)
libFBCAGen.CAWidth=20 #Width of the generated image (for min use 4)
libFBCAGen.useImages=1 #checks if you want images This is annoying
libFBCAGen.numOfGens=20 #number of generations
libFBCAGen.numOfStates=2 #number of states (good until 10)
smallDelta=1e-6
CAMapInit=[]
borderLambdas=[]
CAMapInit=libFBCAGen.initCA(CAMapInit) 

##START
edgeRecord = open("morphEdges", "r")
#loops through files
for line in edgeRecord:
    splits=[];sM1=[];sM2=[];lambdas=[];levelMap=[]
    splits=line.split("sMs")
    lambdas=convTextListToList(splits[0])
    sM1=convTextListToList(splits[1])
    sM2=convTextListToList(splits[2])
    for lamb in lambdas:
        sMCur=libFBCAGen.genMorphSM(sM1,sM2,lamb+smallDelta)
        levelMap=libFBCAGen.generateFBCA(sMCur,d,CAMapInit,str(lamb+smallDelta))
        sMCur=libFBCAGen.genMorphSM(sM1,sM2,lamb-smallDelta)
        levelMap=libFBCAGen.generateFBCA(sMCur,d,CAMapInit,str(lamb-smallDelta))


