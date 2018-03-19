"""
Solution for gadventures/python-api-challenge

This module fetches departures data from an api server,
filters by date and category, and then writes the filtered values
to a csv file.

Submitted by: Tyler Hunt
Email: trphunt@tylerhunt.solutions
Date: March 2018
"""
from datetime import datetime
import csv
import requests

######## Fetch Data ########

URL = 'http://localhost:8000/departures'
HEADERS = {"Accept": "application/json"}

def fetch_departures(output_list, url, headers):
    """
    Recursively loads pages of departures into list
    until `next_url` is None.
    """
    response = requests.get(url, headers)
    if response.status_code == 200:
        data = response.json()
        for result in data['results']:
            output_list.append(result)

        next_url = data['next']
        if next_url is None:
            return None
        else:
            fetch_departures(output_list, next_url, headers)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, url))
        return None
    return output_list

DEPARTURES = fetch_departures([], URL, HEADERS)


####### Filter Data #######

def filter_departures(departures, pivot_date, category):
    """
    Return departures with `start_date` later than `pivot_date`
    and matching the given `category`.
    """
    output = []
    for departure in departures:
        start_date = datetime.strptime(departure['start_date'], '%Y-%m-%d')
        cat = departure['category']
        if start_date > pivot_date and cat == category:
            output.append(departure)
    return output

FILTERED_DEPARTURES = filter_departures(DEPARTURES, datetime(2018, 6, 1), 'Adventurous')


####### Write to CSV #######

def write_departures_to_csv(departures):
    """
    Write departures to csv file with title-cased headers.
    """
    with open('filtered_departures.csv', 'w') as csvfile:
        fieldnames = departures[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        headers = [x.title().replace('_', ' ') for x in list(fieldnames)]
        writer.writer.writerow(headers)
        for departure in departures:
            writer.writerow(departure)

write_departures_to_csv(FILTERED_DEPARTURES)
