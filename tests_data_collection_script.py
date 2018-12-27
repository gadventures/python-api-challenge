import unittest
import data_collection_script as dc


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


if __name__ == '__main__':
    unittest.main()