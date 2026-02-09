# JQ 1st
'''with open("Notes/sample.txt","a") as file:
    file.write("Joe\n")
    file.write("Israel\n")
    file.write("Zee\n")

print("run finished")'''
"""content = []
with open("Notes/sample.txt","r+") as file:
    for line in file:
        content.append(line.strip())
    index = content.index("Tia")
    content[index] = "torii"

    file.truncate(0)

    for name in content:
        file.write(name + "\n")
print("code ends")"""

import csv
users = [{'username':"cosmic_voyager",'favorite color':"blue"},
         {'username':"cosmic_vomyager",'favorite color':"blue"}]
with open("Notes/test.csv","r+", newline ='') as csvfile:
    fieldnames = ['username','favorite color']
    writter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writter.writeheader()
   # writter.writerow(fieldnames)
    writter.writerows(users)
