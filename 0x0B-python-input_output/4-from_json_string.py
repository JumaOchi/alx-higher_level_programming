#!/usr/bin/python3

'''string from json to string'''

import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
