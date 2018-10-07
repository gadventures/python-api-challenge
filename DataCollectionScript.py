import sys
import requests
import json
import math
import logging

departures_url = 'http://localhost:8000/departures'
file_name = "FilteredDepartures.csv"
departures_csv_title_columns = "Name, Start Date, Finish Date, Category"


def get_endpoint_data(url):
    '''
        Get all the departures on a single page returned when making a get request
        to /departures/ endpoint.
    '''
    # In the event of a malformed response, I raise an error and prevent a superfluous
    # GET request.
    if url == None:
        logging.warning("Nonetype provided as URL for request.")
        raise requests.exceptions.MissingSchema
    response = requests.get(url)
    if not response.ok:
        logging.warning("Error connecting to server.")
        raise requests.exceptions.ConnectionError
    json_data = response.json()
    return json_data


def get_departures_all():
    '''
        Get all the departures returned when making a get request to /departures/
        endpoint
    '''
    list_of_departures = []
    next_url = departures_url
    try:
        departures = get_endpoint_data(next_url)
    except requests.exceptions.RequestException as e:
        logging.exception(e)
        return list_of_departures
    except requests.exceptions.ConnectionError as e:
        logging.exception(e)
        return list_of_departures
    list_of_departures += departures.get("results")
    next_url = departures.get("next")
    page_count = math.ceil(departures.get("count") / 50)
    # Subtract 1 from page_count, since we needed to read a page before
    # beginning the loop.
    for page in range(page_count - 1):
        try:
            departures = get_endpoint_data(next_url)
        except requests.exceptions.RequestException as e:
            logging.exception(e)
            # Errors are handled by continuing the script, processing any data that
            # was returned.
            break
        except requests.exceptions.ConnectionError as e:
            logging.exception(e)
            break
        list_of_departures += departures.get("results")
        next_url = departures.get("next")
    return list_of_departures


def select_filter(list_to_filter, parameter, value):
    '''
        Filters the data in a list of dictionaries by selecting only the dictionaries
        with an parameter whos value matches the specified value.
    '''
    return_list = []
    for item in list_to_filter:
        if item.get(parameter) == value:
            return_list.append(item)
    return return_list


def greater_than_filter(list_to_filter, parameter, value):
    '''
        Filters the data in a list of dictionaries by selecting only the dictionaries
        with an parameter whos value greater than the specified value.
    '''
    return_list = []
    for item in list_to_filter:
        if item.get(parameter) > value:
            return_list.append(item)
    return return_list


def convert_departure_list_to_csv_string(departure_list):
    '''
        Converts a list of departures into a string format ready to be output as
        a csv.
    '''
    output_string = departures_csv_title_columns
    for departure in departure_list:
        output_string += "\n{0}, {1}, {2}, {3}".format(departure.get("name"), departure.get(
            "start_date"), departure.get("finish_date"), departure.get("category"))
    return output_string


if __name__ == "__main__":

    list_of_departures = get_departures_all()
    filtered_list = greater_than_filter(
        list_of_departures, "start_date", "2018-06-01")
    filtered_list = select_filter(
        filtered_list, "category", "Adventurous")
    csv_output_string = convert_departure_list_to_csv_string(filtered_list)
    csv = open(file_name, "w")
    csv.write(csv_output_string)
