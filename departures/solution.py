import requests
from datetime import datetime
import csv

url = "http://localhost:8000/departures"
headers = {"Accept": "application/json"}

### https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '_main_':


    ### First, we need to collect all departures referenced from the API:

    def getDepartures(departures_list, url, headers):
        response = requests.get(url, headers)
        ### List of HTTP status codes: https://www.restapitutorial.com/httpstatuscodes.html
        if response.status_code == 200:
            data = response.json()
            for outcome in data["results"]:
                departures_list.append(outcome)

            next_url = data["next"]
            if next_url is None:
                return None
            else:
                getDepartures(departures_list, next_url, headers)

        else:
            data = response.status_code
            format_string = "The following error occurred: %s"
            print(format_string % data)

        return departures_list

    departures = getDepartures([], url, headers)


    ### Next, we need to filter down the data to only include departures
    ### with a start_date after June 1st, 2018, and category = "adventurous":

    def filterDepartures(departures, date, category):
        filtered_departures_list = []
        for departure in departures:
            ### https://www.programiz.com/python-programming/datetime/strptime
            start_date = datetime.strptime(departure["start_date"], "%Y-%m-%d")
            style_category = departure["category"]
            if start_date > date and style_category == category:
                filtered_departures_list.append(departure)
        return filtered_departures_list

    filtered_departures = filterDepartures(departures, datetime(2018, 6, 1), "Adventurous")


    ### Finally, we need to create a CSV:

    def createCsv(departures):

        with open("filtered_departures.csv", mode="w") as file:
            fieldnames = ["name", "start_date", "finish_date", "category"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for departure in departures:
                writer.writerow(departure)

    createCsv(filtered_departures)
