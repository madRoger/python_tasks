'''
Given two congruent circles a and b of radius r, return the area of their
intersection rounded down to the nearest integer.

Code Limit: Less than 128 characters.

Example

For c1 = [0, 0], c2 = [7, 0] and r = 5,
the output should be 14
'''
from math import*;circleIntersection=lambda a,b,r:[x-sin(x) for x in [acos(min(hypot(a[0]-b[0],a[1]-b[1])/2/r,1))*2]][0]*r*r//1

 
if __name__ == '__main__':
    print(circleIntersection([0, 0], [7, 0], 5))

    
