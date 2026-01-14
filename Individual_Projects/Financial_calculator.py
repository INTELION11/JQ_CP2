# JQ 2nd Financial calculator    
  
def is_int(intem):    
    # try to turn input into float for money  
    try:    
        intem = float(intem)  # allow decimals for money    
        return intem    
    except ValueError:    
        # if not number, ask again  
        print("Please try again")    
        return is_int(input("Enter a number: "))    
    
def save_goal():    
    # ask user for savings goal    
    goal = is_int(input("how much do you want to save up to? "))    
    # ask how often they save    
    contri_time = input("how often are you contributing? weekly or monthly? ")    
    # ask how much each time    
    amount = is_int(input("how much are you contributing every time? "))    
    # calculate how many times needed    
    total_time = goal / amount    
    # if monthly, set label    
    if contri_time == "monthly":    
        contri_time = "month(s)"    
    # if weekly, set label    
    elif contri_time == "weekly":    
        contri_time = "week(s)"    
    # else generic label    
    else:    
        contri_time = "period(s)"    
    # print result    
    print(f"it will take you: {int(total_time)} {contri_time} to reach your goal")    
    return    
    
def compund_interest():    
    # ask for starting amount    
    start = is_int(input("Starting Amount: "))    
    # ask for interest rate    
    rate = is_int(input("Interest rate (percent): "))    
    # ask for years    
    years = is_int(input("Years saved: "))    
    # turn rate to decimal    
    rate = rate / 100    
    # for each year, add interest    
    for i in range(int(years)):    
        start = start * (1 + rate)    
    # print end amount    
    print(f"At the end of {int(years)} years you will have  ${start:.2f}")    
    
def budget_allocator():    
    # ask for number of categories    
    cats = is_int(input("How many budget categories do you have? "))    
    categories = []    
    percentages = []    
    # get category names    
    for i in range(int(cats)):    
        cat = input(f"Category {i+1}: ")    
        categories.append(cat)    
    # ask for income    
    income = is_int(input("What is your monthly income? "))    
    
    # inner function to calculate allocation    
    def alloc(pct):    
        # allocates percent of income to category  
        return income * pct / 100    
    
    # ask for percent for each category    
    for cat in categories:    
        pct = is_int(input(f"What percent is your {cat}? "))    
        percentages.append(pct)    
    
    # print how much for each category    
    for i in range(int(cats)):    
        amount = alloc(percentages[i])    
        print(f"{categories[i]} is  ${amount:.2f}")    
    
def sales_price():    
    # ask for price    
    start = is_int(input("How much does the item originally cost? "))    
    # ask for discount percent    
    sales = is_int(input("What percent is the discount? "))    
    # calculate discount    
    discount = (100 - sales) / 100    
    # calculate new price    
    finalle = start * discount    
    # print new price    
    print(f"The item now costs  ${finalle:.2f}")    
    
def tip_calculator():    
    # ask for bill    
    bill = is_int(input("How much is the bill? "))    
    # ask for tip percent    
    tip_percent = is_int(input("What percent of a tip are you giving? "))    
    # calculate tip    
    tip = bill * tip_percent / 100    
    # calculate total    
    total = bill + tip    
    # print tip and total    
    print(f"The tip amount is  ${tip:.2f} and your total is  ${total:.2f}")    
    
def run_time():    
    # main menu loop  
    while True:    
        action = input(    
            "Enter the number to select an option\n 1. Savings Time Calculator\n 2. Compound Interest Calculator\n 3. Budget Allocator\n 4. Sale Price Calculator\n 5. Tip Calculator\n 6. Quit\n")    
        # run savings    
        if action == "1":    
            save_goal()    
        # run compound interest    
        elif action == "2":    
            compund_interest()    
        # run budget    
        elif action == "3":    
            budget_allocator()    
        # run sale    
        elif action == "4":    
            sales_price()    
        # run tip    
        elif action == "5":    
            tip_calculator()    
        # quit    
        elif action == "6":    
            print("Goodbye!")    
            break    
        # wrong input    
        else:    
            print("Try again.")    
    
run_time()    
