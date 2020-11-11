# Linear morphs of FBCAs and associated analysis
A linear morph (first described in doi: 10.1007/978-3-030-14687-0_2 ) is a method to explore the space FBCA (Fashion Based Cellular Automata (first documented in 
doi: 10.1109/CIG.2015.7317958.) exist in.

To start, a linear morph is the convex set described by all the score matrices attained by the following equation:
![convexEquation](http://www.sciweavers.org/upload/Tex2Img_1605067020/render.png)

In previous work, these linear morphs were described through specalized FBCAs. These FBCAs vary their score matrix spatially in the horizontal direction, meaning each column of pixels takes the exact same score matrix. The number of pixels in a picture represents the number of divisions taken in the interval [0,1] for lambda. The number of pixels each column is from the left most pixel, is the number of equally spaced divisions on the interval, therefore giving each column its value of lambda. For example this ![linear morph](https://imgur.com/a/hNqqZAM) has 
