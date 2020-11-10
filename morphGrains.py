#This code is meant to generate desired behaviours from a behaviour record
#Takes in:
#   The behaviour records file name
#   The desired behaviours
#   The number of runs for each behaviour
import os
import libFBCAGen
import linecache
import math

## DATA STRUCTURES BELOW ##
class lGContainer:
    def __init__(curContainer,lambd,scoreMatrix,lG,side):
        curContainer.lG=lG
        curContainer.lambd=lambd
        curContainer.sM=scoreMatrix
        curContainer.side=side

## FUNCTIONS BELOW ##

# Takes two lambdas (as floats) and generates midpoint
# literally (lambda1+lambda2)/2
def getMid(lambda1,lambda2):
    midLamb=(lambda1+lambda2)/2
    return(midLamb)   

## DEFINITIONS
# define the two score matrices for the morph
# sM1=[-0.5,-0.5,0.5,-0.5]
# sM2=[0.5,-0.5,-0.5,-0.5]
sM1=[0.320205,0.952292,0.351335,0.837774]
sM2=[0.390741,0.728013,0.614486,0.378596]
sMs=[sM1,sM2]
numberOfTimes=10 # Number of times we attempt to get to an edge before stopping
# sM1=[0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596]
# sM2=[0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,]

# For FBCA gen
libFBCAGen.CALength=20 #Length of torus
libFBCAGen.CAWidth=20 #Width of torus
libFBCAGen.useImages=0 #Keep 0
libFBCAGen.finalImage=0 #Keep 0
libFBCAGen.numOfGens=20 #number of generations
libFBCAGen.numOfStates=2 #number of states (good until 10)

## BORING INITS
d=[];d=os.getcwd()+"/"
curSide=["Left","Right","Middle"]
CAMapInit=[];CAMapInit=libFBCAGen.initCA(CAMapInit) 
borderLambdas=[]

## MAIN ##
# Generates the inital L_g containers 
lGLeft = lGContainer(0,sM1,libFBCAGen.generateFBCA(sM1,d,CAMapInit,curSide[0]),curSide[0])
lGRight = lGContainer(1,sM2,libFBCAGen.generateFBCA(sM2,d,CAMapInit,curSide[1]),curSide[1])
lGMid = lGContainer(0.5,libFBCAGen.genMorphSM(sM1,sM2,0.5),libFBCAGen.generateFBCA(libFBCAGen.genMorphSM(sM1,sM2,0.5),d,CAMapInit,curSide[2]),curSide[2])

direction=0
lastDifferentLambda=0
##Goes left to right 
for n in range(0,len(sMs)): # because we may have many 
    if n%2 == 0:
        while (libFBCAGen.compareLs(lGRight,lGLeft) == 0):
            if (libFBCAGen.compareLs(lGLeft,lGMid) == 1):
                ##Get lambdas Left -> Mid  and new Mid
                lGLeft = lGContainer(lGMid.lambd,libFBCAGen.copyList(lGMid.sM),libFBCAGen.copyOver(lGMid.lG),curSide[0])
                lGMid.lambd = getMid(lGLeft.lambd,lGRight.lambd)
                lGMid.sM = libFBCAGen.genMorphSM(sM1,sM2,lGMid.lambd)
                lGMid.lG = libFBCAGen.generateFBCA(lGMid.sM,d,CAMapInit,curSide[2])
                direction+=1
            else:
                ##Record last different lamdba
                lastDifferentLambda=lGMid.lambd
                ##Get lambdas Right -> Mid and new Mid
                lGRight = lGContainer(lGMid.lambd,libFBCAGen.copyList(lGMid.sM),libFBCAGen.copyOver(lGMid.lG),curSide[2])
                lGMid.lambd = getMid(lGLeft.lambd,lGRight.lambd)
                lGMid.sM = libFBCAGen.genMorphSM(sM1,sM2,lGMid.lambd)
                lGMid.lG = libFBCAGen.generateFBCA(lGMid.sM,d,CAMapInit,curSide[2])
                direction+=1

            if (direction==numberOfTimes):
                borderLambdas.append(lGMid.lambd)
                # Get the left
                tempSM = libFBCAGen.genMorphSM(sM1,sM2,lastDifferentLambda)
                lGLeft = lGContainer(lastDifferentLambda,tempSM,libFBCAGen.generateFBCA(tempSM,d,CAMapInit,curSide[0]),curSide[0])
                # Get the right
                lGRight = lGContainer(1,sM2,libFBCAGen.generateFBCA(sM2,d,CAMapInit,curSide[1]),curSide[1])
                # Get the mid
                tempLambd = getMid(lGLeft.lambd,lGRight.lambd)
                tempSM = libFBCAGen.genMorphSM(sM1,sM2,tempLambd)        
                lGMid = lGContainer(tempLambd,tempSM,libFBCAGen.generateFBCA(tempSM,d,CAMapInit,curSide[2]),curSide[2])
                # Reset our number of goes
                direction=0
        # Collect our edges and clean them up
        finalLambs = [round(x,5) for x in borderLambdas]
        for idx1,x in enumerate(finalLambs):
            for idx2,y in enumerate(finalLambs):
                #dont worry about the infinity case
                if (abs(x-y)/min(abs(x),abs(y))<1e-4)and(idx1!=idx2):
                    finalLambs.remove(y)
        print(finalLambs)
        # Print them off 
        edgeRecord = open(f"morphEdges", "w")
        for n in range(len(sMs)):
            if (n%2==0):
                edgeRecord.write(f"{finalLambs}sMs{sMs[n]}sMs{sMs[n+1]}")