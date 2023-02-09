from django.db import models

# creating model for creating table inside the database.
class emp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    Date_of_Join = models.DateField()
    