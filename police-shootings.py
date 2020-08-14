import csv

path = "C:/Users/ajz22/Documents/Summer2020/case-study/fatal-police-shooting-data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) #File Header

unarmed_victims = {}
unarmed_victim_count = 0


'''
header = [Id, Name, Date, Manner of death, Armed, Age, Gender, 
       Race, City, State, Sign of Menral Illness, Flee, Body Camera]

Q1) How many unarmed shootings victims are there in the data set?

Answer: 
'''

for row in reader:

    name = row[1]
    age = row[5]
    date = row[2]
    armed = row[4]
    race = row[7]
    state = row[9]

    print(row)

    if(armed == "unarmed"):
        victim = dict({"name":name, "age": age, "date": date, "armed": armed, "race": race, "state": state})
        unarmed_victims.update(victim)
    

#for victim in unarmed_victims.values():
    #print(victim)

unarmed_victim_count = len(unarmed_victims)
print(f"Total unarmed victims: {unarmed_victim_count}")