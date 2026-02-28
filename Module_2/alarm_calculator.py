#Ask user to enter current time in 24 hours format.
current_time = int(input("Enter current time (0-23) in hours: "))

#Ask user how many hours to wait before the alarm rings.
wait_hours = int(input("Enter number of hours to wait: "))

#Check if the current time entered is valid. Between 0-23.
if current_time < 0 or current_time > 23:
    print("Current time must be between 0 and 23.")
#Check if waiting hour is not negative
elif wait_hours < 0:
    print("Waiting hours cannot be negative.")
else:
    #Add current time and waiting hours to get total hours passed.
    total_hours = current_time + wait_hours

    #24 hours clock resets after every 24 hours. Modulus gives the remainder after division.
    alarm_time = total_hours % 24

    print("--------------------------------")
    print(f"Current Time: {current_time}")
    print(f"Hours to Wait: {wait_hours}")
    print("--------------------------------")
    print(f"Alarm will go off at: {alarm_time}")
    print("--------------------------------")
