class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}
    
    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")
    
    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print(f"{self.name} has no graded assignments.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} (ID: {student.student_id}) to the course {self.course_name}.")
    
    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found in course {self.course_name}.")
    
    def display_all_students_grades(self):
        if self.students:
            print(f"Grades for all students in {self.course_name}:")
            for student in self.students:
                student.display_grades()
        else:
            print("No students enrolled in this course.")

instructor = Instructor("Dr. Sam", "Python Course")

student1 = Student("Lorna", "L001")
student2 = Student("Nicole", "N002")

print("---- Course Management System ----")
instructor.add_student(student1)
instructor.add_student(student2)

instructor.assign_grade("S001", "Assignment 1", 85)
instructor.assign_grade("S001", "Assignment 2", 90)
instructor.assign_grade("S002", "Assignment 1", 78)

instructor.display_all_students_grades()
