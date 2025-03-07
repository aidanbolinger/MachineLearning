#Aidan Bolinger
#700733392

import numpy as np

#NUMBER 1
#Write a python program that:
#I. Uses a dictionary to store student names as keys and their marks as values.
#II. Implement functions for adding a student, calculating the average, finding the
#highest and lowest marks, and searching for a student’s marks.
#III. Allows the user to perform these operations interactively.
print("Number 1:\n")

#Create dictionary
students = {}

#function to add a student name and marks
def add_student(name, marks):
    students[name] = marks

#function to calculate average
def calcAverage():
    if not students:
        return 0
    return sum(students.values()) / len(students)

#Function to find highest marks
def highestMarks():
    if not students:
        return None
    return max(students.values())

#Function to find lowest marks
def lowestMarks():
    if not students:
        return None
    return min(students.values())

#Function to search for a student's marks
def search(name):
    return students.get(name, "Student not found")

# Interactive menu for user to perform operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Calculate Average Marks")
        print("3. Find Highest Marks")
        print("4. Find Lowest Marks")
        print("5. Search for Student's Marks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            marks = float(input("Enter student's marks: "))
            add_student(name, marks)
            print(f"Student {name} added with marks {marks}.")
        
        elif choice == '2':
            average = calcAverage()
            print(f"The average marks are {average}.")
        
        elif choice == '3':
            highest = highestMarks()
            if highest is not None:
                print(f"The highest marks are {highest}.")
            else:
                print("No students in the list.")
        
        elif choice == '4':
            lowest = lowestMarks()
            if lowest is not None:
                print(f"The lowest marks are {lowest}.")
            else:
                print("No students in the list.")
        
        elif choice == '5':
            name = input("Enter student's name: ")
            marks = search(name)
            print(f"{name}'s marks: {marks}")
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

#Run the interactive menu to test
menu()


#NUMBER 2
#Create a Rectangle class with attributes length and width. Include methods to calculate
#area and perimeter.
print("\nNumber 2:\n")

#Create rectangle class
class Rectangle:

    #Initialize length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #calculate area
    def area(self):
        return self.length * self.width

    #calculate perimeter
    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

#Test the rectangle class
rect = Rectangle(5, 3)
print(f"Area of the rectangle with a length of {rect.length} and a width of {rect.width}: {rect.area()}")
print(f"Perimeter of the rectangle with a length of {rect.length} and a width of {rect.width}: {rect.perimeter()}")

#NUMBER 3
# Define a class Employee with an instance variable salary and a class variable
#company_name. Create multiple objects and show how class variables work.
print("\nNumber 3:\n")

class Employee:
    #Define class variable
    company_name = "Walmart" 

    #Define instance variable
    def __init__(self, salary):
        self.salary = salary

#create multiple employee objects
emp1 = Employee(50000)
emp2 = Employee(60000)
emp3 = Employee(70000)

#Display results
print(f"Employee 1 works at {emp1.company_name} with a salary of {emp1.salary}.")
print(f"Employee 2 works at {emp2.company_name} with a salary of {emp2.salary}.")
print(f"Employee 3 works at {emp3.company_name} with a salary of {emp3.salary}.")

#Change class variable
Employee.company_name = "Target"

#Display altered class variable
print(f"Employee 1 works at {emp1.company_name} with a salary of {emp1.salary}.")


#NUMBER 4
#Create a Vehicle class with a drive() method. Inherit from this class to create a Car class
#and override the drive() method.
print("\nNumber 4:\n")

#Create vehicle class
class Vehicle:
    def drive(self):
        return "The vehicle is driving."

#Create Car class that inherits vehicle class
class Car(Vehicle):
    #Override drive() method
    def drive(self):
        return "The car is driving."

vehicle = Vehicle()
car = Car()
#Display results
print(vehicle.drive())
print(car.drive())

#NUMBER 5
#Create a class BankAccount with a private variable _balance. Implement methods to
#deposit, withdraw, and check the balance using getter and setter methods.
print("\nNumber 5")

#Create BankAccount class
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    # Getter method for balance
    def get_balance(self):
        return self._balance

    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            return True
        return False

#Test and display results
account = BankAccount(100)
print(f"Initial balance: {account.get_balance()}")

account.deposit(50)
print(f"Balance after deposit: {account.get_balance()}")

account.withdraw(30)
print(f"Balance after withdrawal: {account.get_balance()}")

# Trying to set a new balance using the setter method
account.set_balance(200)
print(f"Balance after setting new balance: {account.get_balance()}")


#NUMBER 6
#Given array, extract rows at odd indexed.
#arr = np.array([[3, 5, 7],
 #[2, 6, 8],
 #[1, 9, 4],
 #[0, 2, 3]])
print("\nNumber 6:\n")

# Given array
arr = np.array([[3, 5, 7],
                [2, 6, 8],
                [1, 9, 4],
                [0, 2, 3]])

# Extract rows at odd indexed
odd_indexed_rows = arr[1::2]
print(odd_indexed_rows)


#NUMBER 7
#For the given matrix find column and row indexes.
#arr = np.array([[10, 15, 30],
 #[45, 50, 5],
 #[60, 8, 20]])
print("\nNumber 7:\n")

# Given array
arr = np.array([[10, 15, 30],
                [45, 50, 5],
                [60, 8, 20]])

# Find column and row indexes
row_indexes, col_indexes = np.where(arr)
print("Row indexes:", row_indexes)
print("Column indexes:", col_indexes)


#NUMBER 8
#Swap column three to first column for given array.
#arr = np.array([[1, 2, 3],
 #[4, 5, 6],
 #[7, 8, 9]])
print("\nNumber 8:\n")

# Given array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Swap column three to first column
arr[:, [0, 2]] = arr[:, [2, 0]]
print(arr)


#NUMBER 9
#Pick the overlapped elements.
#arr1 = np.array([1, 2, 3, 4, 5])
#arr2 = np.array([3, 4, 5, 6, 7])
print("\nNumber 9:\n")

# Define the arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

# Find the overlapped elements
overlapped_elements = np.intersect1d(arr1, arr2)
print(f"The overlapped elements are: {overlapped_elements}")


#NUMBER 10
#Remove rows that contain NaN values.
#arr = np.array([[1, 2, np.nan],
 #[4, 5, 6],
 #[np.nan, 8, 9],
 #[10, 11, 12]])
print("\nNumber 10:\n")

# Given array
arr = np.array([[1, 2, np.nan],
                [4, 5, 6],
                [np.nan, 8, 9],
                [10, 11, 12]])

# Remove rows that contain NaN values
cleaned_arr = arr[~np.isnan(arr).any(axis=1)]
print(cleaned_arr)















