from django.shortcuts import render
from django.http import HttpResponse
from npcgen.models import Class_info

# Create your views here.
def index(requests):
    names = []
    for c in Class_info.objects.all():
        names.append(c.class_title)

    all_names = ' '.join(names)
    return HttpResponse(f"hi this will be the random npc generator\n\n {all_names}")