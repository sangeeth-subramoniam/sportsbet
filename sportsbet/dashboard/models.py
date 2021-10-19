from django.db import models

# Create your models here.
class sportinfo(models.Model):
    sport_name = models.CharField(max_length=30, blank=True)
    sport_desc = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.sport_name


