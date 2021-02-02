# Polymorphism
# Overriding

class Employee:
    def setNumberOfWorkingHours(self):  # the word set in front, sets the overriding technique plausible
        self.numberOfWorkingHours = 40

    def displayNumberOfWokringHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45
     
    def resetNumberOfWorkingHours(self):
        super().numberOfWorkingHours() # reset method -- super function to override. 


employee = Employee()
employee.setNumberOfWorkingHours()
print("Num of working hours are", end=" ")
employee.displayNumberOfWokringHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Num of working hours are", end=" ")
trainee.displayNumberOfWokringHours()
