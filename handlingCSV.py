import os
import csv
a = os.getcwd()
print(a)
os.chdir(r"C:\Users\13203\Documents\excel_files")
a = os.getcwd()
print(a)
'''
print("-----------------------------------------------------------------------")
with open("employees.csv","r") as file:
    rows = csv.reader(file)
    for i in rows:
        print(i)

with open("employees.csv") as file:
    rows = csv.reader(file)
    header = next(rows)
    total_pay = 0
    for i in rows:
        total_pay += int(i[-1])
    print(total_pay)

with open("vaccination_data.csv") as file:
    rows = csv.reader(file)
    for i in rows:
        print(i[0]," "*10,i[-7])

with open("vaccination_data.csv") as file:
    rows = csv.reader(file)
    for i in rows:
        if i[0] == "India":
            print(i)

with open("vaccination_data.csv") as file:
    rows = csv.reader(file)
    header = next(rows)
    t = []
    total = 0
    for i in rows:
        if i[5] != '':
            t.append(i[5])
    for j in t:
        total += int(j)
    print("total vaccinations done by the countries till now are : ",total)

with open("vaccination_data.csv") as file:
    rows = csv.DictReader(file)
    for i in rows:
        print(i)

'''
with open("room.csv","w",newline="") as file:
    write = csv.writer(file)
    write.writerows([("name","major","room","address"),(),
                     ("vikas","IA","203 ","near university"),
                     ("juhitha", "IA", "203 ", "near university"),
                     ("vernika", "cse", "203 ", "near university"),
                     ("meenakshi", "IA", "203 ", "near university"),
                     ("akshay","IA", "101 ","AT University")])

with open("IaCourses.csv","w",newline="") as file:
    w = csv.DictWriter(file,["sno","courseid","name"])
    w.writeheader()
    w.writerow({"sno": "1", "courseid": "606", "name":"security and cryptography"})
    w.writerow({"sno": "2", "courseid": "643", "name": "database security"})
    w.writerow({"sno": "3", "courseid": "612", "name": "intusion p&d"})
    w.writerow({"sno": "4", "courseid": "673", "name": "risk managment"})
    w.writerow({"sno": "5", "courseid": "681", "name": "digital forensics"})
