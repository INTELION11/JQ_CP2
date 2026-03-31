# gradebook.py  
# GradeBook class - keeps trak of all studnts in the class, saves and loads them from file  
  
import csv  
import os  
from student_class import Student  # import Student class for making studnts  
  
# make docs folder and students file path, so stuff goes in the right place  
DOCS_FOLDER = "Individual_Projects/grade book/docs"  
STUDENT_FILE = os.path.join(DOCS_FOLDER, "students.csv")  
  
# GradeBook is like the big box that holds all the studnts  
class GradeBook:  
    def __init__(self):  
        # list of studnts, keeps trak of everyone in class  
        self.students = []  
        self.load_students_from_csv()  
  
    #definition __init__(self)  
    # make empty list for students  
    # try to load any old students from csv file  
  
    def add_student(self, student):  
        self.students.append(student)  
        self.save_students_to_csv()  
  
    #definition add_student(self, student)  
    # put student in list  
    # save the new list to file  
  
    def save_students_to_csv(self):  
        with open(STUDENT_FILE, "w", newline='') as f:  
            writer = csv.writer(f)  
            for s in self.students:  
                writer.writerow([s.name, s.student_id, s.grade_level])  
  
    #definition save_students_to_csv(self)  
    # write all student info (name, id, levle) to students.csv  
  
    def load_students_from_csv(self):  
        if not os.path.exists(STUDENT_FILE):  
            # if no file, just do nothing (first time)  
            return  
        with open(STUDENT_FILE, "r") as f:  
            reader = csv.reader(f)  
            for row in reader:  
                # each row is name, id, levle  
                if len(row) == 3:  
                    name, student_id, grade_level = row  
                    # make a Student and put in list  
                    self.students.append(Student(name, student_id, grade_level))  
  
    #definition load_students_from_csv(self)  
    # open students.csv if it exists  
    # for each row, make a Student and add to list  
  
    def find_student_by_id(self, student_id):  
        # look at every studnt in list till you find right one  
        for s in self.students:  
            if s.student_id == student_id:  
                return s  
        # if you dont find em, return None (nothin)  
        return None  
  
    #definition find_student_by_id(self, student_id)  
    # search list for student with matching id  
    # return that student or None  
  
    def find_student_by_name(self, name):  
        for s in self.students:  
            if s.name.lower() == name.lower():  
                return s  
        return None  
  
    #definition find_student_by_name(self, name)  
    # search list for student with matching name (not case sensetive)  
    # return student or None  
  
    def view_all_students(self):  
        print("\n👥 ALL STUDENTS 👥")  
        print("ID     | Name               | Level | Avg   | Grade")  
        print("---------------------------------------------------")  
        for s in self.students:  
            avg = s.average()  
            avg_str = f"{avg:.1f}" if avg is not None else "N/A"  
            # make it look nice and lined up  
            print(f"{s.student_id:<6} | {s.name:<18} | {s.grade_level:<5} | {avg_str:<5} | {s.letter_grade():<5}")  
        print(f"\nTotal students in the system: {len(self.students)}")  
  
    #definition view_all_students(self)  
    # print table of all students with id, name, level, average, and letter grade  
  
    def class_summary(self):  
        print("\n📚 CLASS SUMMARY 📚")  
        all_grades = []  
        for s in self.students:  
            all_grades.extend(s.grades)  
        if not all_grades:  
            print("Nobody's got grades yet!")  
            return  
        class_avg = sum(all_grades) / len(all_grades)  
        print(f"Total students: {len(self.students)}")  
        print(f"Class average: {class_avg:.2f}")  
        print(f"Letter grade for the class: {self.letter_grade(class_avg)}")  
  
    #definition class_summary(self)  
    # gather all grades from all students  
    # calculate and print the class average  
    # print the class letter grade  
  
    def letter_grade(self, avg):  
        if avg is None:  
            return "N/A"  
        if avg >= 90:  
            return "A"  
        elif avg >= 80:  
            return "B"  
        elif avg >= 70:  
            return "C"  
        elif avg >= 60:  
            return "D"  
        else:  
            return "F"  
  
    #definition letter_grade(self, avg)  
    # take an average, return the letter grade (A, B, C, D, or F)  
  
    def class_statistics(self):  
        print("\n📊 CLASS STATISTICS 📊")  
        all_grades = []  
        for s in self.students:  
            all_grades.extend(s.grades)  
        if not all_grades:  
            print("No grades in the class yet!")  
            return  
        class_avg = sum(all_grades) / len(all_grades)  
        print(f"Total students: {len(self.students)}")  
        print(f"Class average: {class_avg:.2f} ({self.letter_grade(class_avg)})")  
        print(f"Highest grade anyone has: {max(all_grades)}")  
        print(f"Lowest grade anyone has: {min(all_grades)}")  
  
    #definition class_statistics(self)  
    # gather all grades, print class average, highest, and lowest  
