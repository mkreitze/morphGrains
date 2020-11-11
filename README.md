# Linear morphs of FBCAs and associated analysis
A linear morph (first described in doi: 10.1007/978-3-030-14687-0_2 ) is a method to explore the space FBCA (Fashion Based Cellular Automata (first documented in 
doi: 10.1109/CIG.2015.7317958.) exist in.

To start, a linear morph is the convex set described by all the score matrices attained by the following equation:
![convexEquation](http://www.sciweavers.org/upload/Tex2Img_1605067020/render.png)

In previous work, these linear morphs were described through specalized FBCAs. These FBCAs vary their score matrix spatially in the horizontal direction, meaning each column of pixels takes the exact same score matrix. The number of pixels in a picture represents the number of divisions taken in the interval [0,1] for lambda. The number of pixels each column is from the left most pixel, is the number of equally spaced divisions on the interval, therefore giving each column its value of lambda. 
For example:

![linear morph](https://github.com/mkreitze/morphGrains/blob/master/linearMorph.PNG) 

shows both score matrices used, as well as the lambda varying on the interval. In this example 1000 equally spaced divisions as each column of pixels. Due to this representation, when a few columns of divisions produce the same behaviour (that being the final map generated after an FBCA is done) they produce areas of congruent behaviours. These have been named _iso-behavioural grains_.  

The problem with this method is two fold:
  -Behaviours with a very small number of columns may not be noticeable (espeically if similar to their neighbours). 
  -There is no easy way to record each iso-behavioural grains

To rectify this, the concept of a morph portrait was developed. 

A morph portrait is similar to a phase portrait for FBCAs (as described in https://atrium.lib.uoguelph.ca/xmlui/handle/10214/21316). A morph portrait first generates each score matrix as normal. It then generates the level-maps (known as L_gs) using these score matrices in FBCAs with all other parameters constant. Each L_g is then directly compared to every other and is sorted into iso-behavioural grains. Each iso-behavioural grain is then recorded as a textfile called a behaviour record. Finally the image is made where each column of pixels is coloured depending on what iso-behavioural grain it is in. 

For reference, the previous linear morph is shown below as a morph portrait. 

![morph portrait](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Two%20at%201000%20rand(1).png) 

With this comparison, a better understanding of why morph portraits are used can be seen. Each iso-behavioural region is shown distinctly. While similar as both the linear morph and the morph portrait showcase similar numbers of behaviours but the span of the behaviours are slightly different. This anomaly can be understood through a variation of the inital random parameter that generates the first inital set of states (known as L_0). Varying L_0 leads to the following different morph portraits. 

![morph portrait](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Two%20at%201000%20rand(2).png) 

![morph portrait](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Two%20at%201000%20rand(3).png) 
