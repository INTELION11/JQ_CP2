import csv
def view():
    try:  
            with open("Individual_Projects/Counting/docs/the_file.txt", mode="r") as sample:  
                reader = csv.reader(sample, delimiter=',')  
                header = next(reader)
                print(header)  
                for row in reader:
                    print(f"{row}")
    except:  
            print("no csv")  
            return []  
view()
