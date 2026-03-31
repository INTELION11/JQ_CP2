# student.py    
# make a Student, stores info and can add grades, save and load them from files    
# keeps trak of name, id, levle, and grades for each studnt    
import csv    
import os    
    
docs_folder = "Individual_Projects/grade book/docs"    
    
# make shure the docs folder exists    
os.makedirs(docs_folder, exist_ok=True)    
    
class Student:    
    def __init__(self, name, student_id, grade_level):    
        # each student has name, id, levle, and grades list (from file)    
        self.name = name    
        self.student_id = student_id    
        self.grade_level = grade_level    
        self.grades = self.load_grades_from_csv()    
    #definition __init__(self, name, student_id, grade_level)  
    # start a student with name, id, grade level, and their grades from file if any  
  
    def add_grade(self, grade):    
        self.grades.append(grade)    
        self.save_grades_to_csv()    
    #definition add_grade(self, grade)  
    # put the new grade in the list, save the list to csv file  
  
    def average(self):    
        if not self.grades:    
            return None    
        return sum(self.grades) / len(self.grades)    
    #definition average(self)  
    # if grades list is empty return None, else return the avrage  
  
    def letter_grade(self):    
        avg = self.average()    
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
    #definition letter_grade(self)  
    # get the avrage, return A B C D or F for that avrage  
  
    def academic_standing(self):    
        avg = self.average()    
        if avg is None:    
            return "No grades yet"    
        if avg >= 90:    
            return "Honor Roll"    
        elif avg >= 80:    
            return "Good Standing"    
        else:    
            return "Needs Improvement"  
    #definition academic_standing(self)  
    # say if the studnt is honor roll, good, or needs work based on avrage  
  
    def save_grades_to_csv(self):    
        filename = os.path.join(docs_folder, f"grades_{self.student_id}.csv")    
        with open(filename, "w", newline='') as f:    
            writer = csv.writer(f)    
            for g in self.grades:    
                writer.writerow([g])    
    #definition save_grades_to_csv(self)  
    # saves all grades for this studnt to a csv file just for them  
  
    def load_grades_from_csv(self):    
        filename = os.path.join(docs_folder, f"grades_{self.student_id}.csv")    
        grades = []    
        if os.path.exists(filename):    
            with open(filename, "r") as f:    
                reader = csv.reader(f)    
                for row in reader:    
                    if row:    
                        try:    
                            grades.append(float(row[0]))    
                        except:    
                            pass    
        return grades    
    #definition load_grades_from_csv(self)  
    # opens the csv file for this studnt, loads all grades into a list, returns it  
  
    def view_record(self):    
        print(f"\n--- Here's {self.name}'s record ---")    
        print(f"Name: {self.name}")    
        print(f"ID: {self.student_id}")    
        print(f"Grade Level: {self.grade_level}")    
        if not self.grades:    
            print("No grades yet for this student!")    
        else:    
            print("Grades:", ", ".join(str(g) for g in self.grades))    
            print(f"Average: {self.average():.2f} ({self.letter_grade()})")    
            print(f"Academic Standing: {self.academic_standing()}")    
    #definition view_record(self)  
    # prints out all the info for this studnt, including grades, avrage, and standing  
