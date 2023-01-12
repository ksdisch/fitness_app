import requests
from datetime import datetime
import os

# Feature: Log a user-inputted workout to google sheets

# TODO: Connect to google sheets 


# TODO: Create google sheets workbook for user if they do not already have one


# TODO: get user input
# prompt user for type of workout(upper, lower, abdominals, cardio)

# depending on type of workout, bring up different options of workouts to log
    # workout (bicep curls, calf raises, etc.)

    # number of sets

    # number of reps


# TODO: Log the workout in the correct sheet

    # if user does have a sheet for this workout type::
        # add workout data to the end of the sheet
    # if user does not yet have a sheet for this workout type:
        # create the sheet
        # add the workout to the sheet



# Endpoints for using requests.get() for retrieving rows, adding rows, editing rows, and deleting rows in the sheet
# API ENDPOINT: https://dashboard.sheety.co/projects/63b79a7257f21510c95ad1dc/sheets/upper
SHEETY_API_ENDPOINT = 'https://api.sheety.co/90807311e489702f565657d8b7639c28/fitness/'
SHEETY_ENDPOINT = "https://api.sheety.co/90807311e489702f565657d8b7639c28/fitness/upper",
SHEETY_USERNAME = "kdisch"
SHEETY_PASSWORD = "KingLou47"

SHEETY_UPPER_ENDPOINT = "https://api.sheety.co/90807311e489702f565657d8b7639c28/fitness/upper"

# make all of this below user input
workout_date_time = datetime(year=2023, month=1, day=5, hour=13, minute=30)

workout_date = workout_date_time.strftime("%m/%d/%Y")
workout_time = workout_date_time.strftime("%I:%M")

# use this to identify what sheet we are posting to
workout_type = "upper"

exercise = 'Pull-ups'
total_sets = 3
total_reps = 14


print(workout_date_time)

print(workout_date)
print(workout_time)
sheet_inputs = {
    workout_type: {
    'date': workout_date,
    'time': workout_time,
    'exercise': exercise,
    'total sets': str(total_sets),
    'total reps': str(total_reps)
    }
}
print(sheet_inputs)

SHEETY_API_ENDPOINT = f'https://api.sheety.co/90807311e489702f565657d8b7639c28/fitness/upper'

sheet_response = requests.post(
    url=SHEETY_API_ENDPOINT, 
    json=sheet_inputs, 
    auth=(
        SHEETY_USERNAME,
        SHEETY_PASSWORD
    )
)
print(sheet_response.text)

# TODO: 