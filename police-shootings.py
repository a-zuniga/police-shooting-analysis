import csv

with open('fatal-police-shooting-data.csv', 'r') as data_set:

    reader = csv.reader(data_set)
    total_victims = 0
    under_age_victims = 0
    under_age_victims_list = []

    '''
    header = [Id, Name, Date, Manner of death, Armed, Age, Gender, 
        Race, City, State, Sign of Menral Illness, Flee, Body Camera]
    '''
    header = next(reader)

    for row in reader:

        name = row[1]
        age = row[5]
        date = row[2]
        armed = row[4]
        race = row[7]
        state = row[9]

        if(age != ''):
            age = int(age)
            if(age <18):
                under_age_victims += 1
                victim = dict({"name": name, "age": age, "date": date,
                            "armed": armed, "race": race, "state": state})
                under_age_victims_list.append(victim)
        total_victims += 1
    
    for victim in range(len(under_age_victims_list)):
        print(under_age_victims_list[victim])
    print(f'Total victims: {total_victims}')
    print(f'Underage victims: {under_age_victims}')
