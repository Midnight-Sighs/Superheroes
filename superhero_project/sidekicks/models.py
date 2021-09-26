from django.db import models

# Create your models here.
class Sidekick(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    sidekick_to = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    description = models.CharField(max_length=750)

    def __str__(self):
        return self.name