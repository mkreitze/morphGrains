#Generates a 'phase portrait' for a linear moprh of two score matrices
#This is done by checking for weak behavioural equivalence by directly comparing L_gs 
#done in python because the phase portrait work is done in python

#imports of libraries
from PIL import Image
import random
import math
import os 
import numpy
import libFBCAGen

##DATA STRUCTURES BELOW ##
class lGContainer:
    lG=[]
    lambd=0
    xSpot=0

##Global Varbs
libFBCAGen.useImages=0 #Dont make it 1
libFBCAGen.finalImage=0 
libFBCAGen.CALength=20 #20 is good
libFBCAGen.CAWidth=20 #20 is good
libFBCAGen.numOfStates=2
# sM1=[0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596]
# sM2=[0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,]
sM1=[0.320205,0.952292,0.351335,0.837774]
sM2=[0.390741,0.728013,0.614486,0.378596]
sMs=[sM1,sM2] # Matrices we are morphing between
CAMapInit=[];CAMapInit=libFBCAGen.initCA(CAMapInit) #initalize a common L_0
d=[];d=os.getcwd()+"/"
random.seed(4)  #1 for held

##Important varbs
morphRes=1000 #How many equally spaced score matrices are generated btwn sM1 and sM2
imageHeight=100 #Height of the generated image 
quantifer="Two at 1000 rand(4)"
lGs=[]
behaviours=[]

## MAIN ##
for n in range(0,len(sMs)): #Incase we have multiple matrices we want to morph between
    if (n%2==0):
        m=0
        for x in numpy.arange(0,1+1e-8,float(1/morphRes)): #In this loop we generate all the L_gs for the morph
            sMCur = libFBCAGen.genMorphSM(sMs[n],sMs[n+1],x) #gets score matrix
            lGs.append(lGContainer())
            lGs[len(lGs)-1].lG = libFBCAGen.generateFBCA(sMCur,d,CAMapInit,x) #gets the L_g
            lGs[len(lGs)-1].lambd = x #Remembers the lambda used
            lGs[len(lGs)-1].xSpot = m #Remembers the lambda used
            print(f"Generated Lg for Lambda = {x}")
            m+=1
        ignoreList=[]
        for idx,lgCur in enumerate(lGs): #Sorts each L_g into behaviour groups
            temp=[] #This will hold all the similar L_gs
            ignore=0
            for val in ignoreList: #Makes sure I shouldnt ignore it 
                if val == idx:
                    ignore=1
            if ignore == 0:
                for idx2,lgNew in enumerate(lGs): #Walk through the rest
                    if (libFBCAGen.compareLs(lgCur,lgNew) == 1): #If similar, add to the list
                        temp.append(lgNew)
                        ignoreList.append(idx2) #Remove the similar one
                temp.append(lgCur)
                ignoreList.append(idx) 
                behaviours.append(temp) #Add this behaviour class to the behaviours list
            print(f"Finished {idx} of {len(lGs)}") #Makes it easier on the eyes
        morphRecord=open(f"morphPortrait record {quantifer}","w")
        morphRecord.write(f"All behaviours in morph of sMs{sMs[n]}sMs{sMs[n+1]} \n")
        for behaviour in behaviours:
            morphRecord.write(f"Behaviour similar to sM with lambda = {behaviour[0].lambd} \n")
        for behaviour in behaviours:
            if (libFBCAGen.useImages == 1):
                myEyes=str(round(behaviour[0].lambd,5))
                libFBCAGen.genIm(behaviour[0].lG,libFBCAGen.numOfGens,d,f"{quantifer} {myEyes}")
print("Generating Image")

imageColourStep=(255*3)/(len(behaviours)-1)
im= Image.new('RGB', ((morphRes+1),imageHeight), 1)
for idx,behaviour in enumerate(behaviours):
    colourVal=int(idx*imageColourStep)
    if (colourVal-255<0):
        r = colourVal
        g=0
        b=0
    else:
        r=255
        colourVal-=255
        if (colourVal-255<0):
            g = colourVal
            b=0
        else:
            g=255
            colourVal-=255
            if (colourVal-255<0):
                b = colourVal
            else:
                b=255
    for thing in behaviour:
        for y in range(0,(imageHeight)):
            im.putpixel((thing.xSpot,y),(r,g,b))
im.save(f"phaseMorph of {quantifer}.png")
