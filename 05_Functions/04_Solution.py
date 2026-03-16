import math
def circle_stats(radius):
    area=math.pi*radius*radius
    cir=2*math.pi*radius
    return area,cir

print(circle_stats(5))
    