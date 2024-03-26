from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank = True)
# Create your models here.
