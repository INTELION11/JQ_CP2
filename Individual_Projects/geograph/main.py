# JQ 2nd Clasess
# example 1

class circle:
    def __init__(self, name, radius):
        self.name = name.capitalize() 
        self.radius = radius.title()
class square:
    def __init__(self, name,leinght,width):
        self.name = name.capitalize() 
        self.leignth = leinght.title()
        self.width = width.title()

def maker(option):
    option = input("what do you want to create? a 1.Circle\n2.Square\n3.Rectangle\n4.Triangle\n")
    if option == "circle":
        radi = input("what is the raidius")
        name = input("what is the name of the circle")
        name = circle(name,radi)
        
        
        

print("=====================================")
print("📐 GEOMETRY CALCULATOR 📐           ")
print("=====================================")
print("                                     ")
print("Welcome to the Shape Calculator!     ")
print("                                     ")



while True:
    print("=====================================")
    print("🔷 MAIN MENU 🔷                     ")
    print("=====================================")
    print(f"Current Shapes: 0 created")
    print(f"📊 SHAPE LIBRARY:\n┌─────────────────────────────────────┐\n│ No shapes created yet               │\n│ Create your first shape below!      │\n└─────────────────────────────────────┘")
    option = input("🎯 ACTIONS:\n[1] Create New Shape\n[2] View All Shapes\n[3] Select Shape\n[4] Compare Shapes\n[5] Sort Shapes\n[6] Formula Guide\n[7] Quit\nEnter your choice (1-7):\n")
    if option == 1:
        maker(option)