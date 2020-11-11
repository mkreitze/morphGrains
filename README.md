# Linear morphs of FBCAs and associated analysis
A linear morph (first described in doi: 10.1007/978-3-030-14687-0_2 ) is a method to explore the space FBCA exist in.Fashion Based Cellular Automata were (first documented in 
doi: 10.1109/CIG.2015.7317958.). 

To start, a linear morph is the convex set described by all the score matrices (score matrices dictate how different states interact with one another) attained by the following equation:

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

![morph portrait](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Two%20at%201000.png) 

With this comparison, a better understanding of why morph portraits are used can be seen. Each iso-behavioural region is shown distinctly. While similar as both the linear morph and the morph portrait showcase similar numbers of behaviours but the span of the behaviours are slightly different. This anomaly can be understood through a variation of the inital random parameter that generates the first inital set of states (known as L_0). Varying L_0 leads to the following different morph portraits. 

![morph portrait2](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Two%20at%201000%20rand(2).png) 

![morph portrait3](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Two%20at%201000%20rand(3).png) 

![morph portrait4](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Two%20at%201000%20rand(4).png)

To even better visualize the iso-behavioural regions of each morph, the behaviours found by each behavioural region can be shown. For example, take the previous morph portrait. Below is the behaviours (along with their final level-maps). It should be noted that the final two behaviours are _incredibly_ similar. Only off by four pixels. I believe this leads to the moving iso-behavioural regions.


![gif1](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.0/0.0.gif)
![map1](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.0/0.0%2020.png)
![gif2](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.062/0.062.gif)
![map2](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.062/0.062%2020.png)
![gif3](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.14100000000000001/0.14100000000000001.gif)
![map3](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.14100000000000001/0.14100000000000001%2020.png)
![gif4](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.397/0.397.gif)
![map4](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.397/0.397%2020.png)
![gif6](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.47700000000000004/0.47700000000000004.gif)
![map6](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.47700000000000004/0.47700000000000004%2020.png)
![gif7](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.528/0.528.gif)
![map7](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.528/0.528%2020.png)
![gif7](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.838/0.838.gif)
![map7](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.838/0.838%2020.png)
![gif8](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.864/0.864.gif)
![map8](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/behaviour%20visualization%20pf%20phaseMorph%20Two%20at%201000%20rand(4)/0.864/0.864%2020.png)

A slight issue with the morphPortrait method is the time it takes to actually generate these portraits. For a 1000 resolution (that is 1000 pixel columns) it takes about a 40 seconds. This is not efficient as the iso-behavioural regions are relatively large. To combat this a regula falsi method was used. Regula falsi attempts to guess the value by taking half steps with some basic logic. As an example, regula falsi with five steps attempting to find a point on the following number line would look as follows:
![regula](https://github.com/mkreitze/morphGrains/blob/master/regula%20falsi%20simple%20image.png) 

The generated regula falsi method generates behaviour records which looks as follows:

[0.06201, 0.14078, 0.39576, 0.47667, 0.52728, 0.83782, 0.86391]sMs[0.320205, 0.952292, 0.351335, 0.837774]sMs[0.390741, 0.728013, 0.614486, 0.378596]

The first list shows the lambdas of thought edges, the final two lists are the two score matrices used in the morph. To generate images 'around' the edge, a small delta is perturbed around both points. For simplicity, just one of these deltas is shown. With only one exception, all edges are found successfully. 

![edge0](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/0/0.gif)
![edgeG0](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/0/0.png)
![edge1](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/1/1.gif)
![edgeG1](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/1/1.png)
![edge2](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/2/2.gif)
![edgeG2](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/2/2.png)
![edge3](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/3/3.gif)
![edgeG3](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/3/3.png)
![edge4](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/4/4.gif)
![edgeG4](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/4/4.png)
![edge5](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/5/5.gif)
![edgeG5](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/5/5.png)
![edge6](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/6/6.gif)
![edgeG6](https://github.com/mkreitze/morphGrains/blob/master/edge%20method%20example/visExample/6/6.png)

# Trying to use this with more complex examples

Consider taking those two previous score matrices, using the crisscrossing method (a method which allows the intrinsict qualities of two level-maps to be combined into a new level-map using a higher state FBCA, detailed in https://atrium.lib.uoguelph.ca/xmlui/handle/10214/21316) and generating linear morphs. What would be seen? What behaviours would be crossed. As shown below, a morph portrait between these 4x4 score matrices yields an insane number of iso-behavioural regions. This is seen by the gradient of colour across the morph portrait. It should be noted that the seeming spectral lines are due to the random seed chosen. 

![morph4dim](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20Four%20FIXED.png)

Thus the quantification of these iso-behavioural regions is too difficult for current methods (especially regular falsi as every column of pixels must now be found using 10 times the operations). This may be due to how crisscrossing generates its matrices and remains to be seen. For comparison, the first morph portrait was made using two random 4x4 score matrices.

![morph4dim](https://github.com/mkreitze/morphGrains/blob/master/morph%20portraits%20example/phaseMorph%20of%20twoFourDimWeird.png)

# still to do, check how this works with the crisscrossing and add crisscrossing to the library
# My manual crisscrossing probably messed it all up
