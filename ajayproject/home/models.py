from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.TextField()
    massage=models.TextField()

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    checkin = models.DateField()
    checkout = models.DateField()
    room_type = models.CharField(max_length=50)
    notes = models.TextField(blank=True)


