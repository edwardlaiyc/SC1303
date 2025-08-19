#list to store leap years
leap_years = []

#test every year
for i in range(1900, 2021):
    #divisible by 4 by not 100
    if i % 4 == 0 and i % 100 != 0:
        leap_years.append(i)
    #divisible by 400
    elif i % 400 == 0:
        leap_years.append(i)
print(leap_years)
