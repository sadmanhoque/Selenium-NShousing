from geopy.geocoders import Nominatim
import time
from pprint import pprint

def coordinateFinder (address):
    # instantiate a new Nominatim client
    app = Nominatim(user_agent="tutorial")

    # get location raw data
    location = app.geocode("6 A. Y. JACKSON COURT BEDFORD NS CA B4A 4B4").raw
    # print raw data
    return(location["lat"] + ',' + location["lon"])

def removeSpace(string):
    return string.replace(" ", "")

#function to remove empty lines
def removeLine(text):
    lines = text.split('\n')
    non_empty_lines = filter(lambda line: line.strip() != '', lines)
    return '\n'.join(non_empty_lines)

#function to save content to a file
def fileWriter(fileName, content):
    file1 = open(fileName, "w")
    file1.write(content)
    file1.close()