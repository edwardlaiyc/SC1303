#Get user input for integer 1-86400
user_input = int(input("Give an integer from 1 - 86400: "))

#1 hour = 3600 seconds (60 * 60)
#The quotient of the division is the current hour --> int() to truncate
current_hour = int(user_input / (60 * 60))

#Find remaining number of seconds, divide it by 60, the quotient is the current minute
current_minute = int((user_input - current_hour * 60 * 60) / 60)

#remaining number of seconds --> current_second
current_second = user_input - current_hour * 60 * 60 - current_minute * 60

#output current time
print("The current time is: ", current_hour, " hours",
    current_minute, " minutes", current_second, " seconds")