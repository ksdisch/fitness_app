import requests
from datetime import datetime
import os

# Sheets API Documentation: https://developers.google.com/sheets/api/reference/rest

# Feature: Log a user-inputted workout to google sheets

# Append to this list as user inputs exercise. This will be a list of lists. Each list within is the data for a specific exercise
# performed during the workout. Will be used with append method
workout_data = []

# TODO: Prompt user to enter a workout (give options for now, eventually could be a dropdown menu)
# make this a dropdown menu or something else to make this easier 

# date and time of workout
workout_date = f'Workout date: {input("Date you exercised (MM-DD-YYYY): ")}'
time_start = f'Start Time: {input("Time your workout began: ")}'
time_end = f'End Time: {input("Time your workout concluded: ")}'


# MAKE A FUNCTION TO GET ALL WORKOUT DETAILS (all of the code below for gathering the details before logging it in the sheet)
workout_type = f'{input("What type of workout did you complete? (upper body, lower body, core, flexibility, or cardio) ")}'.lower()

# Strength training prompts:
if workout_type == 'upper body' or workout_type == 'lower' or workout_type == 'core': # for strength training we ask for sets and reps versus running we will ask for time and distance
#     HEADERS TO SEPARATE EACH WORKOUT
    workout_data.append([workout_date, workout_type, time_start, time_end, "Exercise"])
    
    exercise_count = int(input('How many different exercises did you complete during this workout?'))    
    for i in range(exercise_count):        
    #     Have them input these details for now, can make it a drop down menu later
        exercise_data = ['', '', '', '']
        exercise_data.append(input("Enter exercise: "))
        num_sets = int(input("Enter the number of sets you completed for this exercise: "))
        for j in range(num_sets):
#             get reps and weight for each set and add it to workout_data list
#             reps
            set_reps = int(input(f"Set {j + 1} reps: "))
            exercise_data.append(set_reps)
        
#             weight
            set_weight = input(f"Set {j + 1} weight: ")
    
            if set_weight == "body":
                exercise_data.append(set_weight)
            else:
                try:
                    exercise_data.append(int(input(f"Set {j + 1} weight: ")))
                except:
                    exercise_data.append(input(f"Set {j + 1} weight: "))  # for bodyweight exercises
            j += 1
        workout_data.append(exercise_data)

# # Cardio prompts
# elif workout_type == 'cardio':


# elif workout_type == 'flexibility'


# TODO: Connect to google sheets 


# TODO: Create google sheets workbook for user if they do not already have one





# TODO: Log the workout in the correct sheet

    # if user does have a sheet for this workout type::
        # add workout data to the end of the sheet
    # if user does not yet have a sheet for this workout type:
        # create the sheet
        # add the workout to the sheet
