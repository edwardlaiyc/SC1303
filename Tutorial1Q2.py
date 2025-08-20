#import math for acos, degrees, radians functions
import math

#length of sides
a = 3
b = 7
c = 9

#cos C = (a^2 + b^2 - c^2) / 2ab
#math.acos function gives angle in radians
#math.degrees function converts radians to degrees
def find(a, b, c):
    cosine_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    return math.degrees(cosine_C)
C = find(a, b, c)
B = find(a, c, b)
A = find(b, c, a)

#print out the angles
print("Angle A is:", A, ", Angle B is:", B, ", Angle C is:", C)
print("The 3 angles add up to", A + B + C)