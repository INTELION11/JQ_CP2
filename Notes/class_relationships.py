#Inheritance (is A)

#parent class
class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Vroom, Vroom!")

#clid class
#composition
class engine:
    def __init__(self,model):
        self.model = model
        def __str__(self):
            return self.model
class car(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.engine = engine("v8")
        self.model = model
class boat(vehicle):
    def move(self):
        print("sail!")
class plane(vehicle):
     def move(self):
        print("Fly!")
    

car = car("Ford","Mustang")
boat = boat("Ibiza","Touring 20")
plane = plane("Boeing","737")

for x in (car,boat,plane):
    print(x.brand)
    print(x.model)
    x.move()
print(car.engine)

# aggregate classes (has A)
class library:
    def __init__(self,name,catalog = []):
        self.name = name
        self.catalog = catalog

    def add_book(self,book):
        self.catalog.append(book)
    def remove_book(self,book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("not here")

    def view_catalog(self):
        for book in self.catalog:
            print(book)


class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
lib = library("Provo Library")


lib.add_book(book("The way of kings","By brandon sanderson"))
lib.add_book(book("The hobit","J.R.R Tolkien"))
lib.add_book(book("Harry Potter","JK Rowling"))

lib.view_catalog()



