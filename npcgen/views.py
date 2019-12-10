from .npcgen import NpcGen
from django.shortcuts import render
from django.http import HttpResponse
from npcgen.models import Class_info, Race_info


# Create your views here.
def index(requests):
    x = NpcGen('Buster',1)
    hit_die = []
    names = []
    for c in Class_info.objects.all():
        names.append(c.class_title)
        hit_die.append(c.hit_die)

    all_names = ' '.join(names)
    all_hit_die = ' '.join(hit_die)
    mod_query = Race_info.objects.get(race_title=x.race)
    return HttpResponse(f"hi this will be the random npc generator\n\n {all_names,all_hit_die, x.race,x.npc_class, x.name, x.get_hit_dice(), mod_query.ability_score_modifier.mod_1}")