for i in range(1900, 2021):
    #divisible by 4 but not 100, or divisible by 400
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i)
