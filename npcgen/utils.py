
import requests
import random
from . import char_dict 

from npcgen.models import Class_info, Race_info
from requests_html import HTMLSession 



def find_hit_die(r):
    hit_p = r.html.find('p', first=False)
    for i in range(len(hit_p)):
        if hit_p[i].text.startswith('Hit Dice'):
            hit_die = hit_p[i]
            hit_die = hit_die.text.split('\n')
            hit_points_first = hit_die[1].split(':')[1].strip() 
            hit_points_after = hit_die[2].split(':')[1].strip()
            hit_die = hit_die[0][10:15].replace(' ','')
            hit_die = hit_die.replace('p','')
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
    for i in range(len(prof)):
        if prof[i].text.startswith('Armor'):
            data = prof[i].text.split('\n')
            for p in range(len(data)):
                pair = data[p].split(':')
                key = pair[0]
                value = pair[1]
                prof_data[key] = value
            return prof_data

def find_equip(r):
    eq = r.html.find('ul', first=False)
    data = []
    eq_data = []
    for i in range(len(eq)):
        if eq[i].text.startswith('(a)'):
            data = eq[i].text.split('\n')
            for e in range(len(data)):
                data[e] = data[e].replace('(a)', '')
                data[e] = data[e].replace('(b)', '')
                data[e] = data[e].replace('(c)', '')
                data[e] = data[e].replace('  ',' ')
                eq_data.append(data[e])
    return eq_data

def find_features(r):
    """
    return a dictionary values = feats keys = level and one nested
    dictionary containting level: css id for feat description
    """
    feat_id = []
    features = {}
    level = r.html.find('tr', first=False)

    for i in range(1,21):# just going to strip the level and feats for that level
        ref = level[i].find('a')
        for a in range(len(ref)):
            feat_id.append(ref[a]) # adding to a list of css ids
        lvl_data = level[i].text.split('\n')
        features[lvl_data[0]] = lvl_data[2]
    return features, feat_id

def scrape_class():
    """
    ok so casters ar missing lvl 20 feats(bard, cleric, druid, paladin, ranger, sorcerer, & wizard)
    weirdly not Warlocks. Also it seems the feats for rogue and monk classes are wrong.
    """
    session = HTMLSession()
    resp = session.get('https://www.dndbeyond.com/classes')
    title = resp.html.find('.listing-card__title', first=False)
    classes = {}
    if len(title) == 0:
        return 'ERROR could not get titles'
    for i in range(12):
        r = session.get(f'http://www.dndbeyond.com/classes/{title[i].text}')
        hit_die = find_hit_die(r) #returns a dictionary
        proficiencies = find_prof(r) #dictionary as well
        equip = find_equip(r) #rerurns a list
        feats = find_features(r) #returns  2 ditionaries 
        dnd_class = {
            'hit die' : hit_die, # dictionary
            'proficiencies': proficiencies, #dictionary
            'equipment': equip, #list
            'features': feats[0]
        }
        
        classes[title[i].text] = dnd_class
    return classes    # nested dictionary for each dnd class
        

#print(scrape_class())

def scrape_race():
    session = HTMLSession()
    r = session.get('https://www.dndbeyond.com/races')
    title = r.html.find('.listing-card__title', first=False)
    stat = r.html.find('.characters-statblock', first=False)
    ability_improve = []
    char_traits = []
    race = []
    races = {}
    
    for i in range(9):
        scores = []
        traits = []
        new_list = stat[i].text.replace(' ','')
        new_list = new_list.split('\n', 1)
        new_list = new_list[1:]
        new_list = new_list[0].split(',')
        for a in range(len(new_list)):
            if new_list[a][0] == '+' or new_list[a][0] =='-':
                scores.append(new_list[a])
            else:
                traits.append(new_list[a])
        races[title[i].text] = {
            'ability improve': scores,
            'char traits': traits
        }
   
    return races

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
    abilities = char_dict.classes[npc_class]['scores'] 
    for i in range(1,7):
        die = []
        for d in range(1,5):
            d = random.randint(1,6)
            die.append(d)
        die.sort(reverse=True)
        i = sum(die[:-1])
        scores.append(i)
    scores.sort(reverse=True)  
    for a in range(len(scores)):
        ability_scores.update({abilities[a]: scores[a]})
    
    #find ability score improvements and add them to the proper score
    # using the first 3 letters of the abitily search through the list and 
    # add or subtract the correct number. example data '+2 Strength' 
    #add 2 to the Str value
    
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

