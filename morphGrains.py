#This code is meant to generate desired behaviours from a behaviour record
#Takes in:
#   The behaviour records file name
#   The desired behaviours
#   The number of runs for each behaviour
import os
import libFBCAGen
import linecache
import math
#generates the Lg for a FBCA defined with a score matrix 
def generateFBCA(scoreMatrix,side,d,CAMapInit):
    gif=[];CAMap=[];CAMap=libFBCAGen.copyOver(CAMapInit) #inits

    for n in range(libFBCAGen.numOfGens):
        CAMap=libFBCAGen.updateMap(CAMap,scoreMatrix)
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

##DEFINITIONS OF STUFF
#define the two score matrices for the morph
# sM1=[-0.5,-0.5,0.5,-0.5]
# sM2=[0.5,-0.5,-0.5,-0.5]
sM1=[0.320205,0.952292,0.351335,0.837774]
sM2=[0.390741,0.728013,0.614486,0.378596]
sMs=[sM1,sM2]
# sM1=[0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596]
# sM2=[0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,]

##DEFINTIONS
d=[];d=os.getcwd()
curSide=["Left","Right","Middle"]
#defintions for FBCA generation
libFBCAGen.CALength=20 #Length of the generated image (for min use 5)
libFBCAGen.CAWidth=20 #Width of the generated image (for min use 4)
libFBCAGen.useImages=0 #checks if you want images This is annoying
libFBCAGen.numOfGens=20 #number of generations
libFBCAGen.numOfStates=2 #number of states (good until 10)
numberOfTimes=10
CAMapInit=[]
borderLambdas=[]
CAMapInit=libFBCAGen.initCA(CAMapInit) 

##START
##Get Lambdas
lambdaLeft=0;lambdaRight=1
lambdaMid=getMid(lambdaLeft,lambdaRight)

##Generate score matrices
sMLeft=genMorphSM(sM1,sM2,lambdaLeft)
sMRight=genMorphSM(sM1,sM2,lambdaRight)
sMMid=genMorphSM(sM1,sM2,lambdaMid)

##Generate L_gs
lgLeft=generateFBCA(sMLeft,curSide[0],d,CAMapInit)
lgRight=generateFBCA(sMRight,curSide[1],d,CAMapInit)
lgMid=generateFBCA(sMMid,curSide[2],d,CAMapInit)

##End point 
endPoint=generateFBCA(sMRight,curSide[1],d,CAMapInit)
lastDifferentLambda=0
direction=0
##Goes left to right 
while (compareLs(lgRight,lgLeft)==0):
    if (compareLs(lgLeft,lgMid)==1):
        ##Get lambdas
        lambdaLeft=lambdaMid
        lambdaMid=getMid(lambdaLeft,lambdaRight)
        ##Generate score matrices
        sMLeft=libFBCAGen.copyList(sMMid)
        sMMid=genMorphSM(sM1,sM2,lambdaMid)
        ##Generate L_gs
        lgLeft=libFBCAGen.copyOver(lgMid)
        lgMid=generateFBCA(sMMid,curSide[2],d,CAMapInit)
        direction+=1
        #print("Go Right")
    else:
        ##Record last different lamdba
        lastDifferentLambda=lambdaMid
        ##Get lambdas
        lambdaRight=lambdaMid
        lambdaMid=getMid(lambdaLeft,lambdaRight)
        ##Generate score matrices
        sMRight=libFBCAGen.copyList(sMMid)
        sMMid=genMorphSM(sM1,sM2,lambdaMid)
        ##Generate L_gs
        lgRight=libFBCAGen.copyOver(lgMid)
        lgMid=generateFBCA(sMMid,curSide[2],d,CAMapInit)
        direction+=1
        #print("Go Left")

    if (direction==numberOfTimes):
        borderLambdas.append(lambdaMid)
        #get lambs
        lambdaLeft=lastDifferentLambda
        lambdaRight=1
        lambdaMid=getMid(lambdaLeft,lambdaRight)
        #get sMs
        sMLeft=genMorphSM(sM1,sM2,lambdaLeft)
        sMRight=genMorphSM(sM1,sM2,lambdaRight)
        sMMid=genMorphSM(sM1,sM2,lambdaMid)
        #get Lgs
        lgLeft=generateFBCA(sMLeft,"Found spot",d,CAMapInit)
        lgRight=generateFBCA(sMRight,"Found spot",d,CAMapInit)
        lgMid=generateFBCA(sMMid,"Found spot",d,CAMapInit)
        #print(f"Left {lambdaLeft} Mid {lambdaMid} Right {lambdaRight}")
        direction=0
finalLambs = [round(x,5) for x in borderLambdas]
for idx1,x in enumerate(finalLambs):
    for idx2,y in enumerate(finalLambs):
        #dont worry about the infinity case
        if (abs(x-y)/min(abs(x),abs(y))<1e-4)and(idx1!=idx2):
            finalLambs.remove(y)
print(finalLambs)
edgeRecord = open(f"morphEdges", "w")
for n in range(len(sMs)):
    if (n%2==0):
        edgeRecord.write(f"{finalLambs}sMs{sMs[n]}sMs{sMs[n+1]}")