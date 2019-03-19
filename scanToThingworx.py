#!/usr/bin/python
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

import requests
import json

#scanner for rasperrypi to load onto thingworx
<<<<<<< HEAD
data = input("Please scan an item: ")
base_url = "https://<ip_address>/Thingworx"


def thingSearch(data):
    print("Item number: " + data)
    #url = "https://pp-1901291615ip.devportal.ptc.io/Thingworx/Things/" + data
    url = '{}/Things'+data.format(base_url)
=======
data = raw_input("Please scan an item: ")
base_url = "https://pp-1901291615ip.devportal.ptc.io" #Will need to be changed on each vm startup
appkey = "" #will make the appkey a variable when I obtain it

def thingSearch(data):
    print("Item number: " + data)
    url = "{}/Thingworx/Things/"+data.format(base_url)
>>>>>>> e28f4bd82791b16f03e45407739aed3fe71e991d
    header = {"Content-Type": "application/json"
              ,"appKey": "f1a0b8da-0c90-4a51-a26e-584d3bf9e6e8" #Will need a new appKey
	      ,"Accept": "application/json"
              }

    response = requests.get(url, headers=header)
    print(response.status_code)
    global code
    code = response.status_code
    if code == 200:
        print("This item is already on Thingworx")
    return code

def enableThing(data):
<<<<<<< HEAD
    #url = "https://pp-1901291615ip.devportal.ptc.io/Thingworx/Things/"+data+"/Services/EnableThing"
    url = '{}/Things'+data+'/Services/EnableThing'.format(base_url)
=======
    url = "{}/Thingworx/Things/"+data+"/Services/EnableThing".format(base_url)
>>>>>>> e28f4bd82791b16f03e45407739aed3fe71e991d
    header = {"Content-Type": "application/json"
              ,"appKey": "f1a0b8da-0c90-4a51-a26e-584d3bf9e6e8"
              }
    response = requests.post(url, headers=header)
    print(response.status_code)

def restartThing(data):
<<<<<<< HEAD
    #url = "https://pp-1901291615ip.devportal.ptc.io/Thingworx/Things/"+data+"/Services/RestartThing"
    url = '{}/Things/'+data+'/Services/RestartThing'.format(base_url)
=======
    url = "{}/Thingworx/Things/"+data+"/Services/RestartThing".format(base_url)
>>>>>>> e28f4bd82791b16f03e45407739aed3fe71e991d
    header = {"Content-Type": "application/json"
              ,"appKey": "f1a0b8da-0c90-4a51-a26e-584d3bf9e6e8"
              }
    response = requests.post(url, headers=header)
    print(response.status_code)

def addThing(data):
<<<<<<< HEAD
    dataName = input("Please give scanned item a display name: ")
    #url = "https://pp-1901291615ip.devportal.ptc.io/Thingworx/Resources/EntityServices/Services/CreateThing"
    add_url = "/Resources/EntityServices/Services/CreateThing"
    url = '{}{}'.format(base_url, add_url)
=======
    dataName = raw_input("Please give scanned item a display name: ")
    url = "{}/Thingworx/Resources/EntityServices/Services/CreateThing".format(base_url)
>>>>>>> e28f4bd82791b16f03e45407739aed3fe71e991d
    header = {
        "Content-Type": "application/json"
        ,"appKey": "f1a0b8da-0c90-4a51-a26e-584d3bf9e6e8"
        }

    parameters = {
        "name": data
        ,"thingTemplateName": "GenericThing"
        ,"description": "This scanned item is (a) " + dataName
    }
    response = requests.post(url, headers=header, params=parameters)
    print(response.status_code)
    print(response.content)
    print(json.dumps(parameters))

def addProperties(data):
<<<<<<< HEAD
    #url = "https://pp-1901291615ip.devportal.ptc.io/Thingworx/Things/"+data+"/Services/AddPropertyDefinition"
    url = '{}'+data+'/Services/AddPropertyDefinition'.format(base_url)
=======
    url = "{}/Thingworx/Things/"+data+"/Services/AddPropertyDefinition".format(base_url)
>>>>>>> e28f4bd82791b16f03e45407739aed3fe71e991d
    header = {"Content-Type": "application/json"
              ,"appKey": "f1a0b8da-0c90-4a51-a26e-584d3bf9e6e8"
              }
    global propertyName
    propertyName = input("Please give property a name: ")
    ptype = input("Please give a unit type in all CAPS. (I.e. STRING, NUMBER, BOOLEAN etc.): ")
    description = input("Please give a descrption of the property: ")
    parameters = {
        "name": propertyName
        ,"type": ptype
        ,"description": description
        }
    response = requests.post(url, headers=header, params=parameters)
    print(response.status_code)
    print(response.content)
    print(json.dumps(parameters))

def addValues(data):
<<<<<<< HEAD
    propertyName = input("Which property would you like to change? ")
    #url = "https://pp-1901291615ip.devportal.ptc.io/Thingworx/Things/"+data+"/Properties/*"
    url = '{}/Things'+data+'/Properties/*'
=======
    propertyName = raw_input("Which property would you like to change? ")
    url = "{}/Thingworx/Things/"+data+"/Properties/*".format(base_url)
>>>>>>> e28f4bd82791b16f03e45407739aed3fe71e991d
    header = {"Content-Type": "application/json"
              ,"appKey": "f1a0b8da-0c90-4a51-a26e-584d3bf9e6e8"
              }
    value = input("Please give property a value: ")
    parameters = {
        str(propertyName) : str(value),
        }
    response = requests.put(url, headers=header, params=parameters)
    print(response.status_code)
    print(response.content)
    print(json.dumps(parameters))

<<<<<<< HEAD
try:
    thingSearch(data)
    if code != 200:
        addThing(data)
        enableThing(data)
        restartThing(data)
    else:
        addProps = input("Would you like to add properties?: Yes/No ")
        if addProps == "Yes":
            addProperties(data)
        else:
            print("Exiting Program")
        addVals = input("Would you like to add values to properties?: Yes/No ")
        if addVals == "Yes":
            addValues(data)
        else:
            print("Exiting Program")

except KeyboardInterrupt:
    print("Ctrl+C Programing Exiting")
=======
if __name__ == "__main__":
    try:
        thingSearch(data)
        if code != 200:
            addThing(data)
            enableThing(data)
            restartThing(data)
        else:
            addProps = raw_input("Would you like to add properties?: Yes/No ")
            if addProps == "Yes":
                addProperties(data)
            else:
                print("Exiting Program")
            addVals = raw_input("Would you like to add values to properties?: Yes/No ")
            if addVals == "Yes":
                addValues(data)
            else:
                print("Exiting Program")

    except KeyboardInterrupt:
        print("Ctrl+C Programing Exiting")
>>>>>>> e28f4bd82791b16f03e45407739aed3fe71e991d
