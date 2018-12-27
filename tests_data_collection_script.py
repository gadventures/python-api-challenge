import unittest
import data_collection_script as dc
from datetime import datetime
from unittest.mock import Mock
from unittest.mock import patch
import json
import requests_testing


class TestCollectionScript(unittest.TestCase):

    def test_title_case_single_word(self):
        assert(dc.convert_to_title_case("single") ==
               "Single")

    def test_title_case_two_words(self):
        assert(dc.convert_to_title_case("double_word") ==
               "Double Word")

    def test_title_case_multiple_words(self):
        assert(dc.convert_to_title_case(
               "multiple_word-with-different_punctuation") ==
               "Multiple Word With Different Punctuation")

    def test_filter_valid_date_and_category(self):
        input_data = [{
            "name": "New Zealand Safari",
            "start_date": "2018-04-03",
            "finish_date": "2018-04-13",
            "category": "Marine"
        }, {
            "name": "New Zealand Encompassed",
            "start_date": "2018-06-02",
            "finish_date": "2018-06-10",
            "category": "Adventurous"
        }, {
            "name": "Australia Encompassed",
            "start_date": "2018-06-02",
            "finish_date": "2018-06-10",
            "category": "Marine"
        }]

        out_df = dc.filter_departures(input_data)
        assert(len(out_df) == 1)
        assert(out_df.iloc[0, 0] == input_data[1]['category'])
        assert(out_df.iloc[0, 1] == input_data[1]['finish_date'])
        assert(out_df.iloc[0, 2] == input_data[1]['name'])
        assert(out_df.iloc[0, 3] ==
               datetime.strptime(input_data[1]['start_date'], '%Y-%m-%d'))

    def test_filter_invalid_category(self):
        input_data = [{
            "name": "New Zealand Safari",
            "start_date": "2018-04-03",
            "finish_date": "2018-04-13",
            "category": "Marine"
        }, {
            "name": "New Zealand Encompassed",
            "start_date": "2018-06-02",
            "finish_date": "2018-06-10",
            "category": "Random"
        }, {
            "name": "Australia Encompassed",
            "start_date": "2018-06-02",
            "finish_date": "2018-06-10",
            "category": "Marine"
        }]

        out_df = dc.filter_departures(input_data)
        assert(len(out_df) == 0)

    @requests_testing.activate
    def tests_get_departures_single_get(self):
        mock_data = {
            "count": 150,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": "New Zealand Safari",
                    "start_date": "2018-04-03",
                    "finish_date": "2018-04-13",
                    "category": "Marine"
                },
                {
                    "name": "New Zealand Encompassed",
                    "start_date": "2018-08-31",
                    "finish_date": "2018-09-10",
                    "category": "Adventurous"
                }]
        }

        requests_testing.add(
            request={'url': 'http://127.0.0.1:8000/departures/'},
            response={'body': json.dumps(mock_data)}
        )

        response = dc.get_departures()
        assert(response == mock_data['results'])

    @requests_testing.activate
    def tests_get_departures_get_with_next_data(self):
        mock_data = {
            "count": 150,
            "next": "http://127.0.0.1:8000/departures/?limit=50&offset=50",
            "previous": None,
            "results": [
                {
                    "name": "New Zealand Safari",
                    "start_date": "2018-04-03",
                    "finish_date": "2018-04-13",
                    "category": "Marine"
                },
                {
                    "name": "New Zealand Encompassed",
                    "start_date": "2018-08-31",
                    "finish_date": "2018-09-10",
                    "category": "Adventurous"
                }]
        }

        mock_data_next = {
            "count": 150,
            "next": None,
            "previous": None,
            "results": [{
                    "name": "Brazil Adventure",
                    "start_date": "2018-04-03",
                    "finish_date": "2018-04-13",
                    "category": "Classic"
                },
                {
                    "name": "Vietnam Encompassed",
                    "start_date": "2018-04-03",
                    "finish_date": "2018-04-13",
                    "category": "Marine"
                }]
        }

        requests_testing.add(
            request={'url': 'http://127.0.0.1:8000/departures/'},
            response={'body': json.dumps(mock_data)}
        )
        requests_testing.add(
            request={'url':
                     'http://127.0.0.1:8000/departures/?limit=50&offset=50'},
            response={'body': json.dumps(mock_data_next)}
        )

        # mock_get.return_value.content = json.dumps(mock_data)

        response = dc.get_departures()
        assert(response == mock_data['results'] + mock_data_next['results'])

if __name__ == '__main__':
    unittest.main()