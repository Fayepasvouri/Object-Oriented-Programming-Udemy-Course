# Access Specifiers
#Public
#Protected
#Private

class Car:
    numberOfwheels=4
    _color="Black"  # This is a protected attritube displayed by a single underscore
    _yearOfManufacturer=2017
    print(self._color, self._yearOfManufacturer)

class BMW(Car):
    def __init__(self):
        print(self._color, self._yearOfManufacturer)

bmw=BMW()
