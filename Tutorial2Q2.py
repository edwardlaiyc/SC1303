import random

current_sum = count = 0

#if sum == 1000, can continue adding one more number
while current_sum <= 1000:

    #generate i-th number first
    current_number = random.randint(1, 20)
    count += 1

    #101th number generated will break the loop
    if count > 100:
        print("Stopping early, More than 100 numbers generated")
        print("Sum: ", current_sum, "count: ", count)
        break

    #only first 100 numbers will added to the sum
    current_sum += current_number

#if used as we don't want to print this when count>100, sum<=1000
if current_sum > 1000:
    print("Stopping as sum > 1000")
    print("Sum: ", current_sum, "count: ", count)