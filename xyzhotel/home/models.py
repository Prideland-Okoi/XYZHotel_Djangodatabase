from django.db import models

# Create your models here.
class Bookrecords(models.Model):
    room_number=models.CharField(max_length=50)
    amount = models.CharField(max_length=100)
    occupant_name = models.CharField(max_length=150)
    email= models.CharField(max_length=100)
    occupation = models.CharField(max_length=150)
    days_to_spend= models.CharField(max_length=150)
    start_date= models.CharField(max_length=150)
    end_date= models.CharField(max_length=150)

    class Meta:
        db_table="bookrecord"
