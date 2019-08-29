#!/usr/bin/python
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

import requests
import json

#Class that defines RESTful API callable
class ThingworxAPI:
    def __init__(self):
        #scanner for rasperrypi to load onto thingworx
        self.thing = input("Please search for a thing: ")
        self.appKey = "<your api key>" #Update the carot brackets to your app key
        self.base_url = "http://<your Thingworx URL>/Thingworx" #Update Thingworx instance to your url
        self.header = {"Content-Type": "application/json"
        ,"appKey": self.appKey
        ,"Accept": "application/json"}

    def thingSearch(self):
        url = self.base_url+"/Things/"+self.thing
        response = requests.get(url, headers=self.header)
        print(response.status_code)
        global code
        code = response.status_code
        if code == 200:
            print("This item is already on Thingworx")
        return code

    def enableThing(self):
        url = self.base_url+"/Things/"+self.thing+"/Services/EnableThing"
        response = requests.post(url, headers=self.header)
        print(response.status_code)

    def restartThing(self):
        url = self.base_url+"/Things/"+self.thing+"/Services/RestartThing"
        response = requests.post(url, headers=self.header)
        print(response.status_code)

    def addThing(self):
        dataName = input("Please give scanned item a display name: ")
        url = self.base_url+"/Resources/EntityServices/Services/CreateThing"
        parameters = {
            "name": self.thing
            ,"thingTemplateName": "ScannedItemTemplate"
            ,"description": "This scanned item is (a) " + dataName
             }
        response = requests.post(url, headers=self.header, params=parameters)
        print(response.status_code)
        print(response.content)
        print(json.dumps(parameters))

    def setProject(self):
        url = self.base_url+"/Things/"+self.thing+"/Services/SetProjectName"
        parameters = {
            "projectName": "IndustryDemo"
        }
        response = requests.post(url, headers=self.header, params=parameters)
        print(response.status_code)

    def addProperties(self):
        url = self.base_url+"/Things/"+self.thing+"/Services/AddPropertyDefinition"
        global propertyName
        propertyName = input("Please give property a name: ")
        ptype = input("Please give a unit type. (I.e. STRING, NUMBER, BOOLEAN etc.): ")
        description = input("Please give a descrption of the property: ")
        parameters = {
        "name": propertyName
        ,"type": ptype.upper()
        ,"description": description
        }
        response = requests.post(url, headers=self.header, params=parameters)
        print(response.status_code)
        print(response.content)
        print(json.dumps(parameters))

    def addValues(self):
        propertyName = input("Which property would you like to change? ")
        url = self.base_url+"/Things/"+self.thing+"/Properties/*"
        value = input("Please give property a value: ")
        parameters = {
        str(propertyName) : str(value),
        }
        response = requests.put(url, headers=self.header, json=parameters)
        print(response.status_code)
        print(response.content)
        print(json.dumps(parameters))

    def services(self):
        serviceName = input("Name of service to execute: ")
        url = self.base_url+'/Things'+self.thing+'/Services/'+serviceName
        response = requests.post(url, headers=self.header)
        print(response.status_code)
        print(response.content)

    def getPropValues(self):
        propertyName = input("Which property would you like to see? ")
        url = self.base_url+"/Things/"+self.thing+"/Properties/"+propertyName
        response = requests.get(url, headers=self.header)
        print(response.status_code)
        print(json.loads(response.content.decode())['rows'][0])


if __name__ == "__main__":
    try:
        thing = ThingworxAPI()
        thing.thingSearch()
        if code != 200:
            thing.addThing()
            thing.enableThing()
            thing.restartThing()
            thing.setProject()
        else:
            addProps = input("Would you like to add properties?: yes/no ")
            if addProps.lower() == "yes":
                thing.addProperties()
            else:
                print("Exiting Program")

            addVals = input("Would you like to add values to properties?: yes/no ")
            if addVals.lower() == "yes":
                thing.addValues()
            else:
                print("Exiting Program")

            executeService = input("Would you like to execute a service?: yes/no ")
            if executeService.lower() == "yes":
                thing.services()
            else:
                print("Exiting Program")
    except KeyboardInterrupt:
        print("Ctrl+C Programing Exiting")
