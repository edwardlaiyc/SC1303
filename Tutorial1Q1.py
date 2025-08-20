def time_output(time):
    current_hour = time // 3600
    current_minute = (time % 3600) // 60
    current_second = (time % 3600) % 60
    print("The current time is:", current_hour, "hours",
          current_minute, "minutes", current_second, "seconds")
