from django.db import models

# Create your models here.
class Contact(models.Model):
    photo = models.ImageField(upload_to='contacts_photo/', default='icon.jpg', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    # object = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"