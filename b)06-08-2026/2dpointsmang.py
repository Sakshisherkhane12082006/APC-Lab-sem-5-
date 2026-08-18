import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def farthest_point(points):
    return max(points, key=lambda p: distance((0, 0), p))

points = [(2, 3), (5, 6), (1, 1), (8, 2)]

p1 = (2, 3)
p2 = (5, 6)

print("Distance:", distance(p1, p2))
print("Farthest Point from Origin:", farthest_point(points))