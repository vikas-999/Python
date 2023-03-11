#for loops
#wap to check how many words are there in a given sentance
a = input("enter a string : ")
count = 1
for i in a:
    if i.isspace() == True:
        count+=1
print("there are",count," words in the given sentence")
        
