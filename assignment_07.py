#--------------------------------------------------------------#
# Title: Assignment05
# DESC: This assignment demonstrates using constants, variables,
#        operators, formatting, and files
# and calculations
# Change Log: (Who, When, What)
# Ryan, 5/28/2024, Created Script
#--------------------------------------------------------------#


import json

MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

FILE_NAME: str = "Enrollments.json"
menu_choice: str = ""
students: list = []

class FileProcessor:
    
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, 'r') as file:

                loaded_student_data = json.load(file)
                for student in loaded_student_data:
                    loaded_student = Student(first_name = student["First_Name"], last_name = student["Last_Name"], course = student["Course"])
                    student_data.append(loaded_student)
                
                print("File loaded")
        except FileNotFoundError as e:
            IO.output_error_messages("The text/json file could not be found when running this script", e)
        except ValueError as e:
            IO.output_error_messages("There are corruption issues in the file", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            list_of_students: list = []
            for student in student_data:
                student_json: dict = {"First_Name": student.first_name, "Last_Name": student.last_name, "Course": student.course}
                list_of_students.append(student_json)
    
            file = open(file_name, "w")
            json.dump(list_of_students, file)
            print(f"The student list was saved in {FILE_NAME}")
            file.close()
        except TypeError as e:
            IO.output_error_messages("The data may not be in a valid format", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message)
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        print(menu)
    
   
    @staticmethod
    def input_menu_choice():
        try:
            user_choice = input("Please select an option: ")
            if user_choice not in ("1","2","3","4"):
                raise Exception("Please select only 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages("Unknown Error.",e.__str__())
        return user_choice

    
    @staticmethod
    def output_student_courses(student_data: list):
        print("The current list of students is:")
        print("Name \t\tLast Name \tCourse")
        for student in student_data:
            print(f"{student.first_name} \t\t {student.last_name} \t\t{student.course}")

   
    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers or symbols")
            
            student_last_name = input("Please enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The first name and last name should not contain numbers or symbols")
            
            course_name = input("Please enter the course name: ")

            new_student = Student(first_name=student_first_name, last_name=student_last_name, course= course_name)

            student_data.append(new_student)
            print(f"{new_student.first_name} {new_student.last_name} in {new_student.course} has been added.")            
        except ValueError as e:
            IO.output_error_messages("There is a incorrect value.", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        return student_data

class Person:

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("There are numbers or symbols in the first name!")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("There are numbers or symbols in the first name!")
        
    def __str__(self):
        return f"{self.first_name},{self.last_name}"

class Student(Person):

    def __init__(self, first_name: str, last_name: str, course: str):
        super().__init__(first_name = first_name, last_name= last_name)
        self.course = course
    
    @property
    def course(self):
        return self.__course
    
    @course.setter
    def course(self, value: str):
        self.__course = value

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course}"

if __name__ == "__main__":

    students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)

    while True:
        IO.output_menu(MENU)
        
        menu_choice = IO.input_menu_choice()

        match menu_choice:
            case "1":
                students = IO.input_student_data(student_data = students)
            case "2":
                IO.output_student_courses(student_data = students)
            case "3":
                FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
            case "4":
                print("The program has ended.")
                exit()
