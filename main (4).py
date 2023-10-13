class Student:

    def _init_(self, name, roll_number, cgpa):

        self.name = name

        self.roll_number = roll_number

        self.cgpa = cgpa



def sort_students(student_list):

    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)

    return sorted_students



# Example usage:

student1 = Student("Hari", "A123", 7.8)

student2 = Student("srikanth", "A124", 8.9)

student3 = Student("saumya", "A125", 9.1)

student4 = Student("Mahidhar", "A126", 9.9)



students = [student1, student2, student3, student4]



sorted_students = sort_students(students)



# Print the sorted list of students by CGPA in descending order

for student in sorted_students:

    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")