#Mini Project Assignment: Daily Calorie Tracker CLI

#------------------------------------------------------------------------------------------------------

# Course            : Programming for Problem Solving using Python
# Assignment Title  : Building a Calorie Tracking Console App
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
# Submission Date   : 10 November 2025
#____________________________________________________________________________________________________


import datetime                                                 # for saving date and time when writing to a file


# --- Task 1: Setup and Introduction---

print("Welocme to your Daily Calorie Tracker")
print()
print("This is a Python-based Command Line Interface tool. \nThis tool has various use-cases. \nThe basic function is to log meals and keep track of total calories consumed, and compare against a personal daily limit, and even save session logs for future tracking.")
print()


# --- Task 2: Input & Data Collection ---

meals = []                                                      # empty list to store meal names
calories = []                                                   # empty list to store calories of each meal

num_meals = int(input("How many meals did you have today? "))   # user enters number of meals
print()

for i in range(num_meals):                                     # loop runs that many times to take meal details
    meal = input(f"Enter name of meal #{i+1}: ")               # input meal name
    cal = float(input(f"Enter calories for {meal}: "))         # input calorie count
    meals.append(meal)                                         # add meal to list
    calories.append(cal)                                       # add calories to list



# --- Task 3: Calorie Calculations ---

total_cal = sum(calories)                                      # calculates the sum of calories
avg_cal = total_cal / len(calories)                            # calculates average calories per meal

daily_limit = float(input("\nEnter your daily calorie limit: "))  # inputs the daily calorie limit of the user
print()

print("\n----- YOUR CALORIE SUMMARY -----\n")
print(f"Total Calories: {total_cal}")                          # displays total
print(f"Average Calories per Meal: {avg_cal: }")               # displays average



# --- Task 4: Exceed Limit Warning System ---

if total_cal > daily_limit:                                    # checks if user has exceeded daily limit or not
    print("Warning! You exceeded your daily calorie limit!")
elif total_cal == daily_limit:
    print("Whew! Your calorie intake for today is exactly your daily limit.")
else:
    print("Great! You are within your daily limit.")


# --- Task 5: Neatly Formatted Output ---

print("\nMeal Name\tCalories")                                
print("-" * 25)                                               
for i in range(len(meals)):                                   # prints the details of all meals
    print(f"{meals[i]}\t\t{calories[i]}")
print("-" * 25)
print(f"Total:\t\t{total_cal}")
print(f"Average:\t{avg_cal:.2f}")


# --- Task 6: Bonus - Save to File ---
save = input("\nDo you want to save this session to a file? (yes/no): ").lower()
if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w", encoding="utf-8") as file:       # specifies character encoding
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]}: {calories[i]} calories\n")
        file.write("\n")
        file.write(f"Total: {total_cal}\n")
        file.write(f"Average: {avg_cal:.2f}\n")
        file.write(f"Daily Limit: {daily_limit}\n")
        if total_cal > daily_limit:
            file.write("Status: Exceeded daily limit \n")
        else:
            file.write("Status: Within daily limit \n")
        file.write("\n")
    print(f"Session saved to {filename}")
else :
    print("Session was not saved as per instructions.")



#_________________________________End of Program________________________________________________ 