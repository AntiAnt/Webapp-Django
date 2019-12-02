from django.db import models

# Create your models here.
class Class_info(models.Model):
    class_title = models.CharField(max_length=200)
    first_level_hits = models.CharField(max_length=100)
    hits_after_first = models.CharField(max_length=100)

class Race_info(models.Model):
    race_title = models.CharField(max_length=100)
    ability_score_modifier = models.CharField(max_length=100)
