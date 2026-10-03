#import everything

'''
Your program should compute the following statistics and print the output
for each state:

State name: <STATE>

Average number of new weekly cases for the entire state dataset:
Date with the highest new number of covid cases:
Month and Year, with the highest new number of covid cases:
Month and Year, with highest new number, percentage of population:
'''

# Import everything
import requests
import json
import csv
from datetime import datetime


# API Configuration
DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

# Read State Population Data
state_populations = {}

with open("states.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        state = row[0]
        population = int(row[1])

        state_populations[state] = population

# Go through every state
for state in state_populations:

    # Query CDC API
    params = {
        "$where": (
            f"state='{state}' "
            "AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'"), "$order": "end_date ASC"
    }

    req = requests.get(BASE_URL, params=params)
    state_records = json.loads(req.text)

    # Average Weekly Cases
    new_cases = []

    for record in state_records:
        new_cases.append(float(record["new_cases"]))

    average_cases = round(sum(new_cases) / len(new_cases), 2)

    # Highest Weekly Cases
    largest_record = max(state_records, key=lambda record: float(record["new_cases"]))

    largest_date = (largest_record["end_date"][:10])

    largest_cases = int(float(largest_record["new_cases"]))

    # Highest Month
    monthly_totals = {}

    for record in state_records:
        month = (record["end_date"][:7])
        cases = float(record["new_cases"])

        if month in monthly_totals:
            monthly_totals[month] += cases
        else:
            monthly_totals[month] = cases

    highest_month = max(monthly_totals, key=monthly_totals.get)

    highest_month_cases = int(monthly_totals[highest_month])

    formatted_month = (datetime.strptime(highest_month,"%Y-%m").strftime("%B %Y"))

    # Population Percentage
    population = (state_populations[state])

    percent_population = round(
        (highest_month_cases / population) * 100, 2)

    # Print Output
    print(f"----------------State name: {state}----------------")
    print()
    print("Average number of new weekly cases for the entire state dataset:")
    print(average_cases)
    print()
    print("Date with the highest new number of covid cases:")
    print(f"{largest_date} ({largest_cases})")
    print()
    print("Month and Year, with the highest new number of covid cases:")
    print(f"{formatted_month} ({highest_month_cases})")
    print()
    print("Month and Year, with highest new number, percentage of population:")
    print(f"{percent_population}% (Population: {population})")
    print()
    print("-" * 60)
