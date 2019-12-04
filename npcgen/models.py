from django.db import models

# Create your models here.
class Ability_Mod(models.Model):
    race_title = models.CharField(max_length=50, default='null')
    mod_1 = models.CharField(max_length=50, default='null')
    mod_2 = models.CharField(max_length=50, default='null') 

class Class_info(models.Model):
    class_title = models.CharField(max_length=200, default='null')
    first_level_hits = models.CharField(max_length=100, default='null')
    hits_after_first = models.CharField(max_length=100, default='null')
    hit_die = models.CharField(max_length=10, default='null')
    equip = models.CharField(max_length=200, default='null')
    armor_prof = models.CharField(max_length=200, default='null')   
    weapon_prof  = models.CharField(max_length=200, default='null')
    tool_prof = models.CharField(max_length=200, default='null')
    saves_prof = models.CharField(max_length=200, default='null')
    skill_prof = models.CharField(max_length=200, default='null')
    features = models.CharField(max_length=500, default='null') # perhaps wrong field type this will be a list. 

class Race_info(models.Model):
    race_title = models.CharField(max_length=100, default='null')
    ability_score_modifier = models.ForeignKey('Ability_Mod', on_delete=models.CASCADE)
    race_traits = models.CharField(max_length=200, default='null')
