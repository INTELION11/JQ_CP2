import csv

try:
    with open("Notes/Movies list - Sheet1.csv",mode = "r") as sample:
        reader = csv.reader(sample,delimiter=',')
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1],
                    header[2]: line[2],
                    header[3]: line[3],
                    header[4]: line[4],
                    header[5]: line[5]
                }
            )
except:
    print("cant find csp")
else:
    on = True
    while on is True:
        action = input(" 1 Search / Recommendations \n 2 Print Full Movie List \n 3 Exit\n").strip().lower()
        if action == "2" or action == "print":
            for user in users:
                print(user)
        elif action == "3" or action == "exit":
            on = False
        elif action == "1" or action == "search" or action == "recommendations":
            do = input("Choose filters to apply (enter numbers separated by commas, e.g., 1,3): \n1 Genre \n2 Director \n3 Actor \n4 Length (min/max)\n").split(",")
            if do == "1":
                genre = input("what genre?")
            listt =  users.find(genre)
            