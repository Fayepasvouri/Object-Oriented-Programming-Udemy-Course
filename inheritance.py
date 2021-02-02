# Inheritance
# This is a multiple inheritance example

class OperatingSystem:
    multitasking=True
    name="Mac OS"

class Apple:
    website="www.apple.com"
    name="Apple"

class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This website is a multi tasking system. Visit {} for more details".format(self.website))
            print(self.name)

macBook= MacBook()

# Multilevel Inheritance 

class MusicalInstruments: # Parent
    numberOfMajorKeys=12

class StringInstruments(MusicalInstruments):
    typeOfWood="Tonewood"

class Guitar(StringInstruments): # Child
    def __init__(self):
        self.numberOfStrings=6
        print(self.numberOfStrings, self.numberOfMajorKeys, self.typeOfWood)

guitar= Guitar()
