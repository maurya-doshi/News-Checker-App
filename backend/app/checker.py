import argparse
from datetime import datetime
import json
import re
import requests
import time

'''
    Class URL

    Global variables:
        1. s_time - Stores the start time of checking.
        2. check_time - Stores the ISO time of checking.

    Instance variables:
        1. link - Stores the link that was passed.
        2. is_true - A boolean value to represent the truth value of a claim raised in the url.
            default - False
        3. truth_percentage - A floating point value to represent the truth value of a claim raised in the url out of 100.
            default - 0.0

    Setter-Getter pair:
        1. link() - Ensure the integrity of the news link from the user.
        2. is_true() - Ensure that the default value of is_true is False.
        3. truth_percentage() - Ensure the value of truth_percentage lies between 0 to 100(inclusive).

    Methods:
        1. __init__(self, link) - Constructor of the URL class. Initializes the value of link, is_true and truth_percentage.
        2. __str__(self, link) - Prints the truth value both in terms of a boolean and a floating point value.
        3. news_json() - Read the contents present in the link into a JSON format.
'''

class URL:
    s_time = time.time()
    check_time = datetime.now()

    def __init__(self, link):
        self.link = link
        self.is_true = False
        self.truth_percentage = 0.0

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        '''
            Link validation
            1. Ensure that a non-empty string is read as the input.
            2. Ensure that the link comes from either Reddit or X.

            Exceptions:
                1. ValueError:
                    a. Empty input as link input.
                    b. If link from an other site other than Reddit or X.
        '''

        # Ensure a non-empty string is read as a link.
        if not link:
            raise ValueError("Empty string. No link found!")

        # TODO - Implement a regular expression that validates user input.

        self._link = link


    @property
    def is_true(self):
        return self._is_true

    @is_true.setter
    def is_true(self, is_true):
        # Ensure it's harder to change the boolean value is_true to "True" by default.
        if is_true:
            raise ValueError("Default value is False!")

        self._is_true = is_true

    @property
    def truth_percentage(self):
        return self._truth_percentage

    @truth_percentage.setter
    def truth_percentage(self, truth_percentage):
        # Ensure truth_percentage lies between 0 to 100.
        if not (0 <= truth_percentage <= 100):
            raise ValueError("Truth percentage can only lie in-between 0 to 100(inclusive)!")

        self._truth_percentage = truth_percentage


    # Print the status of check.
    def __str__(self):
        return f"Check at: {self.check_time}\nThe claim at: {self._link}, is most likely {self._is_true}.\nProbability of truth: {self._truth_percentage}.\n\nTime spent on analysis: {time.time()-self.s_time} s"


    def news_json(self):
        # TODO - send a get request using the requests module and print the output in JSON format.
        ...


def main():
    # Command line arguments.
    parser = argparse.ArgumentParser(prog = "checker.py", description = "A python program to probabilistically determine the truth value of a claim raised in a link on platforms like Reddit/X.", epilog = "Source @ github.com/maurya-doshi/News-Checker-App\nContributors:\n1.KaoKsn\n2.Maurya Doshi")

    parser.add_argument("link") # Positional argument: link to the claim.

    # Flags
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-s", "--silent", action="store_true")
    parser.add_argument("-V", "--version", action="store_true")

    # Parsing the command line arguments.
    args = parser.parse_args()

    # Create a news_engine object.
    news_engine = URL(args.link)

    # Read the contents of the link in JSON format.
    news_engine.news_json()

    return 0;


if __name__ == "__main__":
    main()
