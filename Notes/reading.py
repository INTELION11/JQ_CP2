import csv
try:
    with open("Notes/sample.txt","r") as file:
        content = []
        for line in file:
            content.append(line.strip())
except:
    print("can't find that file")
else:
    for line in content:
        print(f"hello {line}")


try:
    with open("Notes/Class CSV sample - Sheet1.csv",mode = "r") as sample:
        reader = csv.reader(sample,delimiter=',')
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1]
                }
            )
except:
    print("cant find csp")
else:
    for user in users:
        print(user)