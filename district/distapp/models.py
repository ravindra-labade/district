from django.db import models


class District(models.Model):
    district_name = models.CharField(max_length=30)
    number_of_tehsils = models.IntegerField()
    number_of_villages = models.IntegerField()
    district_collector = models.CharField(max_length=30)
    famous_spot = models.CharField(max_length=30)


