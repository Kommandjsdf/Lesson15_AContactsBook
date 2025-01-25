from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='contacts_photo/', blank=True, null=True)

# Create your models here.
