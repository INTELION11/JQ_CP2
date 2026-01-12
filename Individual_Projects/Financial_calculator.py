# JQ 2nd Financial calculator
def is_int(intem):
        try:  
            intem = int(intem)  # must be integer for factorial  
            return intem
        except ValueError:  
            print("Please try again") 

def save_goal():
    goal = input("how much do you want to save up to? ")
    contri_time = input("how often are you contributing? weekly or monthly? ")
    amount = input("how much are you contributing every time? ")
    goal = is_int(goal)
    amount = is_int(amount)
    total_time = goal/amount
    if contri_time == "monthly":
        contri_time = "month(s)"
    if contri_time == "weekly":
        contri_time = "week(s)"
    print(f"it will take you: {total_time} {contri_time} to reach your goal")
    return
def compund_interest():
    start = is_int(input("Starting Amount: "))
    rate = is_int(input("Interest rate: "))
    years = is_int(input("Years saved: "))
    rate =  rate/100
    rate = rate + 1 
    for i in range(1,years):
        start = start*rate
    print(start)
def sales_price():
    start = is_int(input("Starting Amount: "))
    sales = is_int(input("what is the discount rate? "))
    discount = (100 - sales)/100
    finalle = start*discount
    print(finalle)


def run_time():
    action = input("Enter the number so select an option \n1. Savings Time Calculator \n2. Compound Interest Calculator \n3. Budget Allocator \n4. Sale Price Calculator \n5. Tip Calculator\n or 6. Quit\n")
    if action == "1":
        save_goal()
    if action == "2":
        compund_interest()

run_time()

  