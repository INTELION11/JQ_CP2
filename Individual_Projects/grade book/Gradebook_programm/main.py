def studenter():

    class student:
        def __init__(self,name,id,grade_log = []):
            self.name = name
            self.grade_log = grade_log
            self.id = id
 
        def avarge_grade(self,grade):
            self.grade_log.append(grade)

        def view_catalog(self):
            for book in self.grade_log:
                print(book)
            print(self.name)


    class grade:
        def __init__(self,classs,grade):
            self.classs = classs
            self.grade = grade

        def __str__(self):
            return f"{self.classs}: {self.grade}"
        
    lib = student("jack of arc",1890)


    lib.avarge_grade(grade("mathclass","89"))


    universe = True
    while universe == True:
        option = input("\n🎯 MAIN MENU:\n[1] Add New Student\n[2] Add Grade to Student\n[3] View Student Record\n[4] View All Students\n[5] Class Summary\n[6] Exit\n")
        if option == "1":
            opt = input("What ")
            studenter()
        elif option == "2":
            add_grade()
        elif option == "5":
            lib.view_catalog()
        elif option == "6":
            universe = False
        
        
studenter()
    