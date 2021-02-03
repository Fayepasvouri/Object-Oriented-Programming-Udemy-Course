class Square:
    def __init__(self, side):
        self.side=side 
    
    def __add__(squareOne, squareTwo): # the add method helps the program to execute the math calculation that otherwise would not be possibe. 
        return ((4 * squareOne.side) + (4 * squareTwo.side))
    
squareOne = Square(3)
squareTwo = Square (4)
print("Sum of sides of both squares is:", squareOne + squareTwo) # --> now the add between the two is possible
