import random

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

def gen_scores():
    scores = []
    for i in range(1,7):
        die = []
        for d in range(1,5):
            d = random.randint(1,6)
            die.append(d)
        die.sort(reverse=True)
        i = sum(die[:-1])
        scores.append(i)
        print(scores)
    scores.sort(reverse=True)    
    return scores       
