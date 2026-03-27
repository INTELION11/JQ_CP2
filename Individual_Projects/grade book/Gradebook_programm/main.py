def studenter():

    class student:
        def __init__(self,name,grade_log = []):
            self.name = name
            self.grade_log = grade_log
 
        def avarge_grade(self,grade):
            self.grade_log.append(grade)

        def view_catalog(self):
            for book in self.grade_log:
                print(book)


    class grade:
        def __init__(self,classs,grade):
            self.classs = classs
            self.grade = grade

        def __str__(self):
            return f"{self.classs}: {self.grade}"
        
    lib = student("Provo Library")


    lib.avarge_grade(grade("The way of kings","89"))

    lib.view_catalog()





option = input("\n🎯 MAIN MENU:\n[1] Add New Student\n[2] Add Grade to Student\n[3] View Student Record\n[4] View All Students\n[5] Class Summary\n[6] Exit\n")
if option == "1":
    studenter()
if option == "2":
    


