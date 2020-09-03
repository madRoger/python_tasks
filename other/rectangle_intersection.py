'''
Given two rectangles, find the area of intersection.
'''
class Rectangle():
    
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


def intersection_area(r1, r2):
    if (r2.min_x >= r1.max_x or
        r1.min_x >= r2.max_x or
        r2.min_y >= r1.max_y or
        r1.min_y >= r2.max_y):
        return 0
    
    areaX = min(r1.max_x, r2.max_x) - max(r1.min_x, r2.min_x)
    areaY = min(r1.max_y, r2.max_y) - max(r1.min_y, r2.min_y)
    return areaX * areaY


if __name__ == '__main__':
    rect1 = Rectangle(0, 0, 3, 2)
    rect2 = Rectangle(-1, 0, 3, 3)
    print(intersection_area(rect1, rect2))

