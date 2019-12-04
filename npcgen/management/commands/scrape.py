from npcgen.utils import scrape_class

from django.core.management.base import BaseCommand, CommandError
from npcgen.models import Class_info, Race_info


class Command(BaseCommand):
    help = 'greeting'
    output_transaction = True
    def handle(self, *args, **options):
        Class_info.objects.all().delete()
        class_data = scrape_class()
        race_data = scrape_race()
        for key, value in class_data.items():
            x = Class_info()
            a = Ability_mod()
            x.class_title = key
            x.hit_die = value['hit die']['hit die']
            x.first_level_hits = value['hit die']['hit points 1st level']
            x.hits_after_first = value['hit die']['hit points after 1st']
            x.equip = value['equipment']
            x.save()
        
        """
        iterate through race data to save the data to the npcgen db
        """
        race_list = race_data[0]
        ability_improve = race_data[1]
        race_traits = race_data[2]

        
        return 'hello'
