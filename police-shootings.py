import csv

with open('fatal-police-shooting-data.csv', 'r') as data_set:

    reader = csv.reader(data_set)
    total_victims = 0
    under_age_victims = 0
    under_age_victims_list = []
    unarmed_victims = 0
    unarmed_victims_list = []

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

        '''
        Validates age of victim and adds to list if underage
        '''
        if(age != ''):
            age = int(age)
            if(age < 18):
                under_age_victims += 1
                victim = dict({"name": name, "age": age, "date": date,
                               "armed": armed, "race": race, "state": state})
                under_age_victims_list.append(victim)
        if(armed == 'unarmed' or armed == "toy weapon"):
            unarmed_victims += 1
            unarmed_victim = dict({"name": name, "age": age, "date": date,
                                   "armed": armed, "race": race, "state": state})
            unarmed_victims_list.append(unarmed_victim)
        total_victims += 1

    print(f'Total victims: {total_victims}')
    print(f'Underage victims: {under_age_victims}')
    print(f'Unarmed victims: {unarmed_victims}')

    unarmed_victim_percentage = (unarmed_victims / total_victims) * 100
    unarmed_victim_percentage = round(unarmed_victim_percentage,2)
    print(f'Unarmed victims percentage: {unarmed_victim_percentage}%')
