

print(" Welcome to Age Calculator ".center(100, "*"))

age = input("Enter your Age: ").strip()

if age.isdigit():
    age = int(age)
    unit = input("Choose the Unit [Months, Weeks, Days, Hours, Minutes, Seconds, All]: ").strip().lower()
    

    months  = age * 12
    weeks   = age * 52
    days    = age * 365
    hours   = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    
    if unit in ["months", "month", "mo"]:
        print(f"Your age in months is: {months:,}")

    elif unit in ["weeks", "week", "we"]:
        print(f"Your age in weeks is: {weeks:,}")

    elif unit in ["days", "day", "da"]:
        print(f"Your age in days is: {days:,}")

    elif unit in ["hours", "hour", "ho"]: 
        print(f"Your age in hours is: {hours:,}") 

    elif unit in ["minutes", "minute", "mi"]:
        print(f"Your age in minutes is: {minutes:,}")

    elif unit in ["seconds", "second", "se"]:
        print(f"Your age in seconds is: {seconds:,}")

    elif unit in ["all", "al"]:
        print(f"Full Statistics for {age} years:")
        print(f"- Months  : {months:,}")
        print(f"- Weeks   : {weeks:,}")
        print(f"- Days    : {days:,}")
        print(f"- Hours   : {hours:,}")
        print(f"- Minutes : {minutes:,}")
        print(f"- Seconds : {seconds:,}")
    else:
        print("Invalid unit! Please try again.")
else:
    print("Please enter a valid number for age.")