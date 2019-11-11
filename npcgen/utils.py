import random

from requests_html import HTMLSession 

import char_dict
def find_hit_die(r):
    hit_p = r.html.find('p', first=False)
    for i in range(len(hit_p)-1):
        if hit_p[i].text.startswith('Hit Dice'):
            hit_die = hit_p[i]
            hit_die = hit_die.text.split('\n')
            hit_points_first = hit_die[1].split(':')[1].strip() 
            hit_points_after = hit_die[2].split(':')[1].strip()
            hit_die = hit_die[0][10:15].replace(' ','')
            hits = {
                'hit die': hit_die,
                'hit points 1st level': hit_points_first,
                'hit points after 1st': hit_points_after
            }
    return hits

def find_prof(r):
    prof = r.html.find('p', first=False)
    data = []
    prof_data = {}
    for i in range(len(prof)-1):
        if prof[i].text.startswith('Armor'):
            data = prof[i].text.split('\n')
            for p in range(len(data)-1):
                key = data[p].split(':')[:1]
                value = data[p].split(':')[1:]
                prof_data[key[i]] = value[i]
    return prof_data

def scrape_class():
    session = HTMLSession()
    resp = session.get('http://www.dndbeyond.com/classes')
    title = resp.html.find('.listing-card__title', first=False)
    for i in range(1):
        r = session.get(f'http://www.dndbeyond.com/classes/{title[i].text}')
        hit_die = find_hit_die(r)
        proficiencies = find_prof(r)
        print(proficiencies)        
        

print(scrape_class())

def scrape_race():
    session = HTMLSession()
    r = session.get('https://www.dndbeyond.com/races')
    title = r.html.find('.listing-card__title', first=False)
    stat = r.html.find('.characters-statblock', first=False)
    ability_improve = []
    char_traits = []
    race = []
    
    
    for i in range(9):
        scores = []
        traits = []
        race.append(title[i].text)
        new_list = stat[i].text.replace(' ','')
        new_list = new_list.split('\n', 1)
        new_list = new_list[1:]
        new_list = new_list[0].split(',')
        for a in range(len(new_list) - 1):
            if new_list[a][0] == '+' or new_list[a][0] =='-':
                scores.append(new_list[a])
            else:
                traits.append(new_list[a])
        ability_improve.append(scores)
        char_traits.append(traits)
    return race, ability_improve, char_trait

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
    abilities = char_dict.classes[race]['scores'] 
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

