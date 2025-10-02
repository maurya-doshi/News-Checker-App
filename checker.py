import argparse
from datetime import datetime
import json
import re
import requests

'''
    Class URL

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
    def __init__(self, link)
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
            raise ValueError("Default value is False!")

        self._truth_percentage = truth_percentage


    # Print the working url.
    def __str__:
        return f"Check at: {s_time}\nThe claim at: {self._url}, is most likely {self.is_true}.\nProbability of truth: {self.truth_percentage}.\n\nTime spent on analysis: {self._optime}"

    def news_json(self):
        # TODO - send a get request using the requests module and print the output in JSON format.
        ...

def main(argc, argv):
    # Create a news_engine object.
    news_engine = URL(argv[1])
    
    # Read the contents of the link in JSON format.
    news_engine.json()

    return 0;


if __name__ == "__main__":
    main()
