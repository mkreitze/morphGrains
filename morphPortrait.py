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

class lGContainer:
    lG=[]
    lambd=0

##FUNCTIONS SPECIFIC TO THIS FILE BELOW
def genMorphSM(sM1,sM2,lamb):
    sMNew=[]
    for i in range(len(sM1)):
        sMNew.append(lamb*sM2[i]+(1-lamb)*sM1[i])
    return(sMNew)



##global inits
# sM1=[0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596]
# sM2=[0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,]
sM1=[0.320205,0.952292,0.351335,0.837774]
sM2=[0.390741,0.728013,0.614486,0.378596]
sMs=[sM1,sM2] 
libFBCAGen.CALength=20 #Length of the generated image (for min use 5)
libFBCAGen.CAWidth=20 #Width of the generated image (for min use 4)
libFBCAGen.useImages=0 #checks if you want images This is annoying
libFBCAGen.numOfGens=20 #number of generations
libFBCAGen.numOfStates=2 #number of states (good until 10)
d=[];d=os.getcwd()+"/"
CAMapInit=[];CAMapInit=libFBCAGen.initCA(CAMapInit) 
morphRes=1000 #How many equally spaced score matrices are generated btwn sM1 and sM2
imageHeight=100 #Height of the generated image 
random.seed(1)  #1 for held
quantifer="Test"

##MAIN 
lGs=[]
behaviours=[]
resolution=float(1/float(morphRes))
for n in range(0,len(sMs)):
    if (n%2==0):
        m=0
        while (m<0.99):
            sMCur=genMorphSM(sMs[n],sMs[n+1],m)
            lGs.append(lGContainer)
            lGs[len(lGs)-1].lG = libFBCAGen.generateFBCA(sMCur,d,CAMapInit,m)
            lGs[len(lGs)-1].lambd = m
            print(f"Generated Lg for Lambda = {m}")
            m+=resolution
        for idx,lgCur in enumerate(lGs):
            temp=[]
            #Takes in the temp stuff
            temp.append(lGContainer);temp[len(temp)-1].lG=lgCur.lG;temp[len(temp)-1].lambd=lgCur.lambd
            for lgNew in lGs:
                if (libGenFBCA.compareLs(lgCur,lgNew)):
                    temp.append(lGContainer);temp[len(temp)-1].lG=lgNew.lG;temp[len(temp)-1].lambd=lgNew.lambd
                lGs.remove(lgNew)
            behaviours.append(temp)
            print(f"Finished {idx} of {len(lgCur.lG)}")
        morphRecord=open(f"morphPortrait record {quantifer}","w")
        morphRecord.write(f"All behaviours in morph of sM1 = {sMs[n]} sM2 = {sMs[n+1]} \n")
        for behaviour in behaviours:
            morphRecord.write(f"Behaviour similar to sM with lambda = {behaviour[0].m} \n")
        for behaviour in behaviours:
            d=f"{d}/{behaviour.m}"
            libFBCAGen.genIm(CAMap,libFBCAGen.numOfGens,d,lambd,1)

print("Finished")

        # imageColourStep=(255*3)/(behaviourNum+1)
        # im= Image.new('RGB', (morphRes+1, 1))
        # for x in range(morphRes):
        #     r=int(imageColourStep*morph[x].behaviourNum)
        #     g=int(imageColourStep*morph[x].behaviourNum)
        #     b=int(imageColourStep*morph[x].behaviourNum)
        #     im.putpixel((x,0),(r,g,b))
        # # directory = os.getcwd()+"/"+str(fileName)+"/"
        # im.save("phaseMorph of "+str(numOfStates)+".png")#+str(sMs[0])+" "+str(sMs[1])+".png")
