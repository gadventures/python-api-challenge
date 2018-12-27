import pandas as pd
import re
import requests
import json
import datetime

API_URL = 'http://127.0.0.1:8000/departures/'

CSV_FILENAME = "adventurous_departures.csv"


def get_api_content(url):
    """
    Returns the content of the given URL.
    """
    response = requests.get(url)
    return response.content


def get_departures():
    """
    Returns the 'departures' data from the URL, based
    on the provided information of parsing the JSON data.
    """
    results = []
    json_data = get_api_content(API_URL)

    apidata = json.loads(json_data)
    results.extend(apidata['results'])

    next_data = apidata.get('next')

    while next_data:
        apidata = json.loads(get_api_content(apidata['next']))
        next_data = apidata.get('next')
        results.extend(apidata['results'])

    return results


def convert_to_title_case(input_string):
    """
    Returns the given string in title case formatting.
    """
    temp = re.sub(r'_|-', " ", input_string)
    return temp.title()


def filter_departures(in_data):
    """
    Filters the given data with the desired filters using Pandas.
    Returns a dataframe for writing to CSV
    """
    df = pd.DataFrame.from_dict(in_data)
    df['start_date'] = df['start_date'].astype('datetime64[ns]')
    filtered_df = df[(df.start_date > datetime.datetime(2018, 6, 1)) &
                     (df.category == "Adventurous")]

    return filtered_df


def write_csv(data_frame, csv_name=CSV_FILENAME):
    """
    Writes the given data frame into a CSV file with the given name.
    """
    data_frame.rename(columns=convert_to_title_case, inplace=True)
    data_frame.to_csv(csv_name, index=False)


def main():
    """
    The main function of the script.
    Calls all required functions to complete the task
    of getting API data, filtering it and writing it to
    a CSV file.
    """
    apidata = get_departures()
    filtered_data = filter_departures(apidata)
    write_csv(filtered_data)

if __name__ == '__main__':
    main()
