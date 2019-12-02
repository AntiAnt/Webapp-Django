from npcgen.utils import scrape_class

from django.core.management.base import BaseCommand, CommandError
from npcgen.models import Class_info, Race_info


class Command(BaseCommand):
    help = 'greeting'
    output_transaction = True
    def handle(self, *args, **options):
        Class_info.objects.all().delete()
        class_data = scrape_class()
        for key, value in class_data.items():
            x = Class_info()
            x.class_title = key
            x.first_level_hits = value['hit die']['hit points 1st level']
            x.hits_after_first = value['hit die']['hit points after 1st']
            x.save()
        return 'hello'
