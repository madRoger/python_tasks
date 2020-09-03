'''
Given a list of points, an interger k, and a point p,
find the k closest points to p.
'''
class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def closest_points(points, k, p):
    dists = []
    for pnt in points:
        dists.append((((p.x - pnt.x)**2 + (p.y - pnt.y)**2)**0.5, pnt))
        
    dists.sort(key=lambda t: t[0])
    return [point for _, point in dists][:k]

if __name__ ==     '__main__':
    points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]
    print(closest_points(points, 1, Point(0, 2)))
    
