import ThingworxClass as scan

if __name__ == "__main__":
    try:
        newThing = scan.ThingworxAPI()
        while True: #Continuously get different property values
            newThing.getPropValues()
    except KeyboardInterrupt:
        print("Ctrl-C Closing Program")
