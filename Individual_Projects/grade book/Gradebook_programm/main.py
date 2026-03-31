# main.py    
# main loop, menu runs until user exits, uses GradeBook, Student, and helpers    
  
from gradebook import GradeBook    
from helper import get_int, get_grade    
  
def main():    
    gb = GradeBook()    
    while True:    
        print("\n=====================================")    
        print("📚 SIMPLE GRADE BOOK 📚")    
        print("=====================================")    
        print("\n🎯 MAIN MENU:")    
        print("[1] Add New Student")    
        print("[2] Add Grade to Student")    
        print("[3] View Student Record")    
        print("[4] View All Students")    
        print("[5] Class Summary")    
        print("[6] Class Statistics")    
        print("[7] Exit")    
        choice = input("\nEnter your choice (1-7): ").strip()    
        if choice == "1":    
            print("\n➕ ADD NEW STUDENT ➕")    
            name = input("A what's the student's name? ").strip()    
            sid = input("And their ID number? ").strip()    
            grade_level = input("What grade are they in (9th, 10th, 11th, 12th)? ").strip()    
            if gb.find_student_by_id(sid):    
                print("Hey! That student ID is already taken.")    
            else:    
                from student_class import Student   # import Student here incase of loops  
                student = Student(name, sid, grade_level)    
                gb.add_student(student)    
                print("\n✅ student added!")    
                print(f"   Name: {name}")    
                print(f"   ID: {sid}")    
                print(f"   Grades: None yet")    
        #definition: if user picks 1, ask for new student info, check for dupe id, if not, make and add student, print happy message  
  
        elif choice == "2":    
            if not gb.students:    
                print("Add some students first")    
                continue    
            print("\n📝 ADD GRADE 📝")    
            print("Current Students:")    
            for s in gb.students:    
                print(f"- {s.name} (ID: {s.student_id})")    
            sid = input("Type the student ID to add a grade to: ").strip()    
            student = gb.find_student_by_id(sid)    
            if not student:    
                print("Couldn't find a student with that ID.")    
            else:    
                grade = get_grade("Enter their grade (0-100): ")    
                student.add_grade(grade)    
                gb.save_students_to_csv()  # Optional: update student list in case you want to sync    
                print("\n✅ Grade added")    
                print(f"   {student.name} now has {len(student.grades)} grade(s)")    
                avg = student.average()    
                print(f"   Current average: {avg:.1f} ({student.letter_grade()})")    
        #definition: if user picks 2, show all students, pick by id, if found add a grade, else print error  
  
        elif choice == "3":    
            sid = input("Type the student ID to see their record: ").strip()    
            student = gb.find_student_by_id(sid)    
            if not student:    
                print("No student with that ID.")    
            else:    
                student.view_record()  
        #definition: if user picks 3, ask for id, find student, print their record or error if not found  
  
        elif choice == "4":    
            gb.view_all_students()  
        #definition: if user picks 4, print all students with info in a table  
  
        elif choice == "5":    
            gb.class_summary()  
        #definition: if user picks 5, print class avergae and letter grade  
  
        elif choice == "6":    
            gb.class_statistics()  
        #definition: if user picks 6, print avergae, hi and low for class  
  
        elif choice == "7":    
                
            break  
        #definition: if user picks 7, exit the loop and stop program  
  
        else:    
            print("That's not an option. Try again.")  
        #definition: if user types anything else, tell em it's not a real choice  
  
#definition main()  
# runs the gradebook menu forever until user picks exit  
  
if __name__ == "__main__":    
    main()  
#definition: run the main function if this file is started  
