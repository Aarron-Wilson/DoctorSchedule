from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    IN_IM = models.BooleanField()
    MONTHS_OF_WARDS_LEFT = models.IntegerField()
    VACATION_MONTH_PREFERENCES = models.CharField(max_length=120)

class VacationChoices(models.TextChoices):
    ZERO = "0", "Zero"
    TWO_PLUS_TWO = "2+2", "Two plus Two"
    FIVE_PLUS_TWO = "5+2", "Five plus Two"

class Section(models.Model):
    name = models.CharField(max_length=120)
    vacation_type = models.CharField(choices=VacationChoices)
    min_visits = models.IntegerField()
    max_visits = models.IntegerField()

class DoctorBlockPreference(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    place = models.IntegerField()

class JobSlot(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    amount = models.IntegerField()
    min_year = models.IntegerField()
    max_year = models.IntegerField()
    only_IM = models.BooleanField()