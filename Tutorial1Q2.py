#import math for acos, degrees, radians functions
import math

#length of sides
a = 3
b = 7
c = 9

#cos C = (a^2 + b^2 - c^2) / 2ab
#math.acos function gives angle in radians
#math.degrees function converts radians to degrees
cosine_C = (a**2 + b**2 - c**2) / (2 * a * b)
radian_C = math.acos(cosine_C)
degree_C = math.degrees(radian_C)

#repeat for angles B, A
cosine_B = (a**2 + c**2 - b**2) / (2 * a * c)
radian_B = math.acos(cosine_B)
degree_B = math.degrees(radian_B)

cosine_A = (b**2 + c**2 - a**2) / (2 * b * c)
radian_A = math.acos(cosine_A)
degree_A = math.degrees(radian_A)

#print out the angles
print("Angle A is: ", degree_A, ", Angle B is: ", degree_B, ", Angle C is: ", degree_C)