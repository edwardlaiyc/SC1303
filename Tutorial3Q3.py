def datetime(user_input):
    date_time = user_input.split()
    date = date_time[0].split('/')
    time = date_time[1].split(':')
    day, month, year = date[1], date[0], date[2]
    hour, minute, second = time[0], time[1], time[2]

    if 0 < int(day) < 31 and 0 < int(month) < 12 and 0 < int(year) < 2026 and len(day) == len(month) == 2 and len(year) == 4:
        if 0 < int(minute) < 60 and 0 < int(hour) < 24 and len(hour) == len(minute) == len(second) == 2:
            print(day + "/" + month + "/" + year)
            print(hour + "/" + minute + "/" + second)
            print(month + "/" + year)
            if int(hour) < 12:
                print("Time is AM")
            else:
                print("Time is PM")
        else:
            print("Date is wrong.")
    else:
        print("Time is wrong.")


datetime("01/01/2001 01:01:01")