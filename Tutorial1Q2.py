#import math for acos, degrees, radians functions
import math

#length of sides
a = 3
b = 7
c = 9

#cos C = (a^2 + b^2 - c^2) / 2ab
#math.acos function gives angle in radians
#math.degrees function converts radians to degrees
def find_angle(a, b, c):
    cosine_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    return math.degrees(cosine_C)
angle_C = find_angle(a, b, c)
angle_B = find_angle(a, c, b)
angle_A = find_angle(b, c, a)

#print out the angles
print("Angle A is:", angle_A, ", Angle B is:", angle_B, ", Angle C is:", angle_C)
print("The 3 angles add up to", angle_A + angle_B + angle_C)