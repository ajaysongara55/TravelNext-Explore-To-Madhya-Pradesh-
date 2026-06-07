from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.TextField()
    massage=models.TextField()

class hotel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    checkin=models.TextField()
    checkout=models.TextField()
    room=models.TextField()
    notes=models.TextField()

def _str_(self)->str:
        return self.name

