# Name:  Joshua Fogus
# Last Modified:  February 7, 2021
# Description:  A function which writes passed data to a csv.

import csv


def csv_writer(data, file_path=None):
    """ Accepts an array of data, which should have length 3 and an optional
        file path to which the data should be written. """

    # Default file path
    if file_path is None:
        file_path = "../test_input.csv"

    headers = ["input_item_type", "input_item_category", "input_number_to_generate"]

    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(headers)
        # All data must be strings to be written
        writer.writerow([str(value) for value in data])


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
