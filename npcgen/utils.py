import random

import char_dict

def gen_race():
    races = [
        'Dragonborn', 'Dwarf', 'Elf',
        'Gnome', 'Half-Elf', 'Halfling',
        'Half-Orc', 'Human', 'Tiefling'
        ]
    index = random.randint(0, len(races)-1)
    return races[index]

def gen_class():
    classes = ['Barbarian', 'Bard', 'Cleric', 
                'Druid', 'Fighter', 'Monk', 
                'Paladin', 'Ranger', 'Rogue']
    index = random.randint(0,len(classes)-1)
    return classes[index]

def gen_scores(race, npc_class):
    scores = []
    ability_scores ={}
    abilities = char_dict.races['Barbarian']['scores'] 
    for i in range(1,7):
        die = []
        for d in range(1,5):
            d = random.randint(1,6)
            die.append(d)
        die.sort(reverse=True)
        i = sum(die[:-1])
        scores.append(i)
    scores.sort(reverse=True)  
    for a in range(len(scores)-1):
        ability_scores.update({abilities[a]: scores[a]})

    return  ability_scores  

def prof_mod(level):
    if level < 5 and level > 0:
        return '+2'
    if level < 9:
        return '+3'
    if level < 13:
        return '+4'
    if level < 17:
        return '+5'
    if level > 17 and level < 21:
        return '+6'
    else:
        return 'Level needs to be between 1 and 20'
