import datetime

#Task
# Defining what day it is today using the datetime module
today = datetime.datetime.now()  # Declare current date and time as variable today
name = input("What is your name?")
age = input("How old are you?")
birth_year = today.year - int(age)  # calculates user birth year by subtracting current year
print(f"OMG {name}, you are {age} years old so you were born in {birth_year}")

# Second part
birth_day = input("what day were you born (please use digits)")
birth_month = input("what month were you born (please use digits)")
if int(birth_month) < today.month:  # if birth month has passed
    print("Sorry I missed your birthday")
elif int(birth_month) == today.month:  # if its the current birth month it checks the day
    if int(birth_day) < today.day:  # if birth day hasn't passed
        print("Yay I haven't missed your birthday!")
    elif int(birth_day) == today.day: # if it is current birth day
        print("happy birthday")
    else:
        print("Sorry I missed our birthday") # if birthday has passed
else:
    print("Yay I didn't miss your birthday!") # if birth month hasnt passed

# extra - NOT DONE
now = datetime.datetime.now()
birthday = input("What is your birthday(dd/mm/yyyy)")
hours = birthday - now
print(hours)

