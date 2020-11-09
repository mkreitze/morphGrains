import libFBCAGen
import os 
sM1=[0.320205,0.952292,0.351335,0.837774]
libFBCAGen.CALength=20 #Length of the generated image (for min use 5)
libFBCAGen.CAWidth=20 #Width of the generated image (for min use 4)
libFBCAGen.useImages=1 #checks if you want images This is annoying
libFBCAGen.numOfGens=20 #number of generations
libFBCAGen.numOfStates=2 #number of states (good until 10)
d=[];d=os.getcwd()+"/"
CAMapInit=[];CAMapInit=libFBCAGen.initCA(CAMapInit)
libFBCAGen.generateFBCA(sM1,d,CAMapInit,"zimzomb")