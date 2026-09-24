#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    #Retrieves events from GitHub url and returns them as a list of dictionaries
    response = requests.get(url).text
    return json.loads(response)

def print_events(events, n=5):
    #Prints the first n events in the form type :: repo
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    #Prints the GitHub user and the URL of the events, and runs the retrieve_events and print_events functions
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)

if __name__ == '__main__':
    main()