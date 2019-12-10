from npcgen.utils import scrape_class, scrape_race

from django.core.management.base import BaseCommand, CommandError
from npcgen.models import Class_info, Race_info, Ability_Mod


class Command(BaseCommand):
    help = 'greeting'
    output_transaction = True
    def handle(self, *args, **options):
        Class_info.objects.all().delete()
        Race_info.objects.all().delete()
        Ability_Mod.objects.all().delete()
        class_data = scrape_class()
        race_data = scrape_race()
        for key, value in class_data.items():
            x = Class_info()
            x.class_title = key
            x.hit_die = value['hit die']['hit die']
            x.first_level_hits = value['hit die']['hit points 1st level']
            x.hits_after_first = value['hit die']['hit points after 1st']
            x.equip = value['equipment']
            x.save()
        
        
        for key, value in race_data.items():
            a = Ability_Mod()
            r = Race_info()
            r.race_title = key
            r.race_traits = value['char traits']
            r.save()
            a.mod_1 = value['ability improve'][0]
            a.mod_2 = value['ability improve'][1]
            a.save()
            
        return 'hello'
