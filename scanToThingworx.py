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
        self.scan = input("Please scan an item: ")
        self.appKey = "bbe9861f-b5dc-442b-9bd7-c90eddb834a8" #will make the appkey a variable when I obtain it
        self.base_url = "http://13.68.204.219/Thingworx" #Will need to be changed on each vm startup
        self.header = {"Content-Type": "application/json"
        ,"appKey": self.appKey
        ,"Accept": "application/json"}

    def thingSearch(self):
        url = self.base_url+"/Things/"+self.scan
        response = requests.get(url, headers=self.header)
        print(response.status_code)
        global code
        code = response.status_code
        if code == 200:
            print("This item is already on Thingworx")
        return code

    def enableThing(self):
        url = self.base_url+"/Things/"+self.scan+"/Services/EnableThing"
        response = requests.post(url, headers=self.header)
        print(response.status_code)

    def restartThing(self):
        url = self.base_url+"/Things/"+self.scan+"/Services/RestartThing"
        response = requests.post(url, headers=self.header)
        print(response.status_code)

    def addThing(self):
        dataName = input("Please give scanned item a display name: ")
        url = self.base_url+"/Resources/EntityServices/Services/CreateThing"
        parameters = {
            "name": self.scan
            ,"thingTemplateName": "ScannedItemTemplate"
            ,"description": "This scanned item is (a) " + dataName
             }
        response = requests.post(url, headers=self.header, params=parameters)
        print(response.status_code)
        print(response.content)
        print(json.dumps(parameters))

    def setProject(self):
        url = self.base_url+"/Things/"+self.scan+"/Services/SetProjectName"
        parameters = {
            "projectName": "Scanner"
        }
        response = requests.post(url, headers=self.header, params=parameters)
        print(response.status_code)

    def addProperties(self):
        url = self.base_url+"/Things/"+self.scan+"/Services/AddPropertyDefinition"
        global propertyName
        propertyName = input("Please give property a name: ")
        ptype = input("Please give a unit type in all CAPS. (I.e. STRING, NUMBER, BOOLEAN etc.): ")
        description = input("Please give a descrption of the property: ")
        parameters = {
        "name": propertyName
        ,"type": ptype
        ,"description": description
        }
        response = requests.post(url, headers=self.header, params=parameters)
        print(response.status_code)
        print(response.content)
        print(json.dumps(parameters))

    def addValues(self):
        propertyName = input("Which property would you like to change? ")
        url = self.base_url+"/Things/"+self.scan+"/Properties/*"
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
        url = self.base_url+'/Things'+self.scan+'/Services/'+serviceName
        response = requests.post(url, headers=self.header)
        print(response.status_code)
        print(response.content)


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
            addProps = input("Would you like to add properties?: Yes/No ")
            if addProps == "Yes":
                thing.addProperties()
            else:
                print("Exiting Program")

            addVals = input("Would you like to add values to properties?: Yes/No ")
            if addVals == "Yes":
                thing.addValues()
            else:
                print("Exiting Program")

            executeService = input("Would you like to execute a service?: Yes/No ")
            if executeService == "Yes":
                thing.services()
            else:
                print("Exiting Program")
    except KeyboardInterrupt:
        print("Ctrl+C Programing Exiting")
