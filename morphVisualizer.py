#This code is meant to generate desired behaviours from a behaviour record
#Takes in:
#   The behaviour records file name
#   The desired behaviours
#   The number of runs for each behaviour
import os
import libFBCAGen
import linecache
import math
import re
#generates the Lg for a FBCA defined with a score matrix 
def generateFBCA(scoreMatrix,d,CAMapInit,lambd):
    gif=[];CAMap=[];CAMap=libFBCAGen.copyOver(CAMapInit) #inits

    for n in range(libFBCAGen.numOfGens):
        CAMap=libFBCAGen.updateMap(CAMap,scoreMatrix)
    libFBCAGen.genIm(CAMap,libFBCAGen.numOfGens,d,lambd,1)
    return(CAMap)

#Takes in two score matrices (written as lists) and a value of lambda
#The new score matrix is generated as lamb*(sM1) + (1-lamb)*sM2 -> sM2+lamb*(sM1-sM2)
#note, the score matrices are ASSUMED to be the same dimension
#lambda should go from 0 to 1 but it doesnt check so go wild
def genMorphSM(sM1,sM2,lamb):
    sMNew=[]
    for i in range(len(sM1)):
        sMNew.append(lamb*sM2[i]+(1-lamb)*sM1[i])
    return(sMNew)

#Takes in L_gs, that is the array of states representing the final state of an FBCA
#Checks if every state is the same between two arrays (breaks early if not the case)
#Returns 1 if true and 0 if false
def compareLs(lg1,lg2):
    isSame=1;x=0;y=0
    while (x < libFBCAGen.CALength) and (isSame==1):
        while (y < libFBCAGen.CAWidth) and (isSame==1):
            if (lg1[x][y].state!=lg2[x][y].state):
                isSame=0
            y+=1
        else: 
            x+=1
            continue
        break
    return(isSame)

#Takes two lambdas (as floats) and generates midpoint
#literally (lambda1+lambda2)/2
def getMid(lambda1,lambda2):
    midLamb=(lambda1+lambda2)/2
    return(midLamb)

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
        sMCur=genMorphSM(sM1,sM2,lamb+smallDelta)
        levelMap=generateFBCA(sMCur,d,CAMapInit,str(lamb+smallDelta))
        sMCur=genMorphSM(sM1,sM2,lamb-smallDelta)
        levelMap=generateFBCA(sMCur,d,CAMapInit,str(lamb-smallDelta))


