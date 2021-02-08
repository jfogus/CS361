# Name:  Joshua Fogus
# Last Modified:  February 7, 2021
# Description:  A function which reads csv data from a file.

import csv


def csv_reader(file_path=None):
    """ Receives a path to a csv file and returns an array of
        object with keys matching the headers. """

    # Default file path
    if file_path is None:
        file_path = "../sample_data.csv"

    # This will be the output
    data_arr = []

    with open(file_path, 'r') as csv_file:
        file_reader = csv.reader(csv_file)

        # First row of the csv is headers
        headers = next(file_reader)
        # This will be added to the output
        data_obj = {}

        for line in file_reader:
            for i, key in enumerate(headers):
                # Only specific columns returned
                if key in ["uniq_id", "number_of_reviews", "average_review_rating", "amazon_category_and_sub_category"]:
                    data_obj[key] = format_data(key, line[i])

            data_arr.append(data_obj)

    return data_arr


def format_data(header, content):
    """ Accepts a type of data as a string and content as a string.
        Returns a formatted version of content based on the type. """

    # uniq_id does not need processed and remains a string
    if header == "uniq_id":
        return content

    # Number of reviews comes in as a string and returns as an integer
    if header == "number_of_reviews":
        try:
            return int(content.replace(",", ""))
        except ValueError:
            return content

    # Number of reviews comes in as a string sentence and returns as
    # a simple integer
    if header == "average_review_rating":
        try:
            return float(content.split(" ")[0])
        except ValueError:
            return content

    # Amazon category and sub category comes in as a string separated
    # by > symbols and returns as an array
    if header == "amazon_category_and_sub_category":
        return content.split(" > ")


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
    csv_reader()
