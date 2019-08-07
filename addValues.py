import scanToThingworx as scan

if __name__ == "__main__":
    try:
        newThing = scan.ThingworxAPI()
        while True:
            newThing.addValues() #Continuously add values to different properties
    except KeyboardInterrupt:
        print("Ctrl-C Closing Program")
