import datetime as dt
import os

import requests

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

NUTRI_HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

now = dt.datetime.now()
now = dt.datetime.strftime(now, "%d/%m/%Y %H:%M:%S").split()
now = {'date': now[0], 'time': now[1]}

nutri_parameters = {
    "query": "ran 3 miles",  # Add workout
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 170,
    "age": 28
}

# Access Nutritionix API
nutri_response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=NUTRI_HEADERS, json=nutri_parameters)
nutri_response = nutri_response.json()
nutri_response = nutri_response['exercises'][0]

new_workout = {
    'workout':
        {
            "date": now['date'],
            "time": now['time'],
            "exercise": nutri_response['name'],
            "duration": nutri_response['duration_min'],
            "calories": nutri_response['nf_calories']}
}

# Using Sheety API

# sheety_response = requests.get(url=sheety_endpoint, headers=sheety_headers)  # Get data from Google Sheets

# Add new data to google sheet

sheety_add = requests.post(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS, json=new_workout)

# ADDITIONAL SHEETY REQUESTS

# Edit row by putting row at the end of the endpoint

# sheety_edit = requests.put(url=f"{SHEETY_ENDPOINT}/2", headers=SHEETY_HEADERS, json=new_workout)

# Delete row by putting row at the end of the endpoint

# sheety_del = requests.delete(url=f"{SHEETY_ENDPOINT}/2", headers=SHEETY_HEADERS, json=new_workout)
