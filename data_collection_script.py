import pandas as pd
import re
import requests
import json
import datetime

API_URL = 'http://127.0.0.1:8000/departures/'

CSV_FILENAME = "adventurous_departures.csv"


def get_api_content(url):
    response = requests.get(url)
    return response.content


def get_departures():
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


def filter_departures(in_data):
    df = pd.DataFrame.from_dict(in_data)
    df['start_date'] = df['start_date'].astype('datetime64[ns]')
    df = df[['name', 'start_date', 'finish_date', 'category']]
    filtered_df = df[(df.start_date > datetime.datetime(2018, 6, 1)) &
                     (df.category == "Adventurous")]

    return filtered_df


def write_csv(data_frame):
    data_frame.rename(columns={
            'name': 'Name',
            'start_date': 'Start Date',
            'finish_date': 'Finish Date',
            'category': 'Category'},
        inplace=True)

    data_frame.to_csv(CSV_FILENAME, index=False)


def main():
    apidata = get_departures()
    filtered_data = filter_departures(apidata)
    write_csv(filtered_data)

if __name__ == '__main__':
    main()
