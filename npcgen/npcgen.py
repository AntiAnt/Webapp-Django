import random
from . import utils

class Npc:
    def get_name(self):
        pass
    def get_level(self):
        pass
    def get_sex(self):
        pass
    def get_npc_class(self):
        pass
    def get_background(self):
        pass
    def get_abilty_scores(self):
        pass
    def get_abilty_mod(self):
        pass
    def get_prof_mod(self):
        pass
    def get_saves(self):
        pass
    def get_skill_scores(self):
        pass
    def get_passive_perception(self):
        pass
    def get_skill_prof(self):
        pass
    def get_languages(self):
        pass
    def get_equipment(self):
        pass
    def get_hit_points(self):
        pass
    def get_hit_dice(self):
        pass
    def get_armor_class(self):
        pass
    def get_initiative(self):
        pass
    def get_speed(self):
        pass
    def get_features(self):
        pass
    def get_traits(self):
        pass
    def get_alignment(self):
        pass
    def get_exp_points(self):
        pass

class NpcGen(Npc):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.race = utils.gen_race()
        self.npc_class = utils.gen_class() 
        self.ability_scores = utils.gen_scores(self.race, 'Barbarian')# need to set the values to each Ability score based on class and race
    
    def get_hit_dice(self):
        hit_die = ''
        class_ = Class_info.objects.all()
        for c in class_:
            if class_.class_title[i] == self.race:
                hit_die = class_.hit_die
        return hit_die


    def get_abilty_mod(self):
        return 

    def get_prof_mod(self):
        return f'Proficiency modifer is {utils.prof_mod(self.level)}'
"""
testing below
"""
x = NpcGen('mike', 1)
print(x.name)
print(x.race)
print(x.npc_class)
print(x.ability_scores)
print(x.get_prof_mod())
print(x.get_hit_dice)