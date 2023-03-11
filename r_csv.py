import csv
import os
print(os.getcwd())
os.chdir(r"C:\Users\13203\Documents\excel_files")
print(os.getcwd())

with open("employees.csv","r")as file:
    rows= csv.reader(file)
    header = next(rows)
    total_amount = 0
    for i in rows:
        total_amount += int(i[-1])
    print("The total salary amount is :- ",total_amount)

with open("employees.csv","r")as file:
    rows= csv.DictReader(file)
    for i in rows:
        print(i["pay"])

#write files
with open("neww.csv","w",newline="")as file:
    write = csv.writer(file)
    write.writerow(["name","roomno"])
    write.writerow([])
    write.writerow(["vikas",203])
    write.writerow(["juhitha",203])
os.popen("neww.csv")

with open("date.csv","w",newline="")as file:
    write = csv.DictWriter(file,["dates", "topics"])
    write.writeheader()
    write.writerow({"dates": 28, "topics": "intro"})
    write.writerow({"dates": 29, "topics": "datatypes"})
    write.writerow({"dates": 30, "topics": "revision"})
os.popen("date.csv")
