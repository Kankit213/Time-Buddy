print("="*30)
print("    WELCOME TO")
print("    Time_Buddy Project.")
print("="*30)

name = str(input("enter your name : "))
print("welcome!",name)
print("have a nice day!")

from datetime import datetime
def handle_situation(situation):

    now = datetime.now()
    hour = now.hour
    minutes = now.minute
    seconds = now.second

    match situation:

        case "morning":
            if hour <= 6 or hour < 7:
                print("good morning!\nHave a nice day")
            else:
                print("It's not morning right now.")

        case "afternoon":
            if hour <= 12 or hour < 18:
                print("good afternoon ! \ni hope your day greatful!")
            else:
                print("It's not afternoon right now.")

        case "evening":
            if hour <= 18 or hour <20:
                print("good evening! \nMay your afternoon be failed with peace,positivity and happiness.")
            else:
                print("It's not evening right now")

        case "night":
            if hour >= 20 and hour < 22 :
                print("good night! \nThe night is young , make your time meaningful.")
            else:
                print("It's not night right now")

        case "sleep":
            print("Sleep mode activated.")
            if hour >= 23 and hour < 6:
                print("Rest well and recharge yourself for tomarrow.")
            else:
                print("It's not sleeping time right now")

        case "time":
            print(f"Current time = {hour:02d}:{minutes:02d}:{seconds:02d}")
            print("Time is precious make every second count.")

        case _:
            print("Hmm! Something went wrong. Check your input.")

# While loop (function ke niche)

while True:

    x = input("\nEnter situation:(morning/afternoon/evening/night/sleep/time/exit): ").strip().lower()

    if x == "exit":
        print("Program closed.")
        print("Thanks you for using Time Buddy ")
        break

    handle_situation(x)

     
    