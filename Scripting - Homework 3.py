"""
Carl Hilliard
Intro to Scripting
Assignment 3
"""

## The car class
class Car():
    def __init__(self, make, yearModel):
        self.__make = make
        self.__yearModel = yearModel
        self.__speed = 0

    ## define a member function that will add 5 to the car's speed when called
    def accelerate(self):
            self.__speed += 5

    ## define a member function that will subtract 5 from the car's speed when called
    def brake(self):
            self.__speed -= 5


        ## the getSpeed member function
    def getSpeed(self):
            return self.__speed

        ## the getMake member function
    def getMake(self):
            return self.__make

        ## the getYear member function
    def getYear(self):
            return self.__yearModel



## create a car object
truck = Car("Ridgeline", "2018")

## call accelerate member function 5 times
for i in range(5):
    truck.accelerate()
    print(getSpeed)

## call brake member function 5 times
for i in range(5):
    truck.brake()
    print(getSpeed)






## PROBLEM 2: The Employee class



class Employee():

    def __init__(self, firstName, lastName, idNumber, department, jobTitle):
        self.firstName = firstName
        self.lastName = lastName

    ## define the full name attribute
        self.fullName = self.firstName + self.lastName

        ## define the email attribute
        self.email = self.firstName.lower() + '.' + self.lastName.lower() + '@company.com'

        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle


## create 3 employee objects
employee1 = Employee('Susan', 'Meyers', '47899', 'Accounting', 'Vice President')
employee2 = Employee('Mark', 'Jones', '39119', 'IT', 'Programmer')
employee3 = Employee('Joy', 'Rogers', '81774', 'Manufacturing', 'Engineer')

print(employee1)
print(employee2)
print(employee3)






## PROBLEM 3



## Define the Student Class
class StudentData():
    def __init__(self, name, c1, c2, c3, c4, c5, c6):
        self.name = name
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6

    ## define the average member function
        def average(self):
            self.average = (self.c1 + self.c2 + self.c3 + self.c4 + self.c5 + self.c6) / 6
            return self.average

## Define the list of students
Students = []
Students.append(StudentData("stu1", 90, 90, 90, 90, 90, 90))
Students.append(StudentData("stu2", 98, 80, 23, 23, 14, 90))
Students.append(StudentData("stu3", 98, 67, 44, 88, 99, 99))
Students.append(StudentData("stu4", 53, 23, 56, 76, 66, 66))
Students.append(StudentData("stu5", 34, 34, 34, 34, 34, 34))
Students.append(StudentData("stu6", 77, 99, 89, 09, 88, 88))
Students.append(StudentData("stu7", 88, 99, 99, 99, 78, 09))
Students.append(StudentData("stu8", 22, 33, 55, 22, 22, 22))
Students.append(StudentData("stu9", 09, 88, 99, 99, 33, 33))
Students.append(StudentData("stu10", 77, 66, 99, 88, 99, 88))
Students.append(StudentData("stu11", 22, 33, 22, 22, 99, 88))
Students.append(StudentData("stu12", 23, 23, 99, 23, 99, 88))
Students.append(StudentData("stu13", 11, 22, 23, 23, 23, 23))
Students.append(StudentData("stu14", 22, 23, 22, 23, 23, 23))
Students.append(StudentData("stu15", 09, 09, 23, 23, 23 ,23))
Students.append(StudentData("stu16", 23, 99, 23, 99, 23, 99))
Students.append(StudentData("stu17", 09, 87, 23, 23, 23, 23))
Students.append(StudentData("stu18", 45, 45, 23, 23, 23, 23))
Students.append(StudentData("stu19", 23, 45, 45, 45, 45, 45))
Students.append(StudentData("stu20", 45, 45, 45, 45, 45, 45))
Students.append(StudentData("stu21", 21, 21, 23, 23, 23, 23))
Students.append(StudentData("stu22", 77, 87, 23, 23, 23, 23))
Students.append(StudentData("stu23", 66, 66, 23, 23, 23, 23))
Students.append(StudentData("stu24", 65, 70, 75, 23, 23, 23))
Students.append(StudentData("stu25", 22, 23, 23, 23, 22, 23))

## Sort the data
Students.sort(key = lambda x: x.average(), reverse = True)



print("Name", "Course 1", "Course 2", "Course 3", "Course 4", "Course 5", "Course 6")
for i in Students:
    print(i.name, i.c1, i.c2, i.c3, i.c4, i.c5, i.c6)


                            













































