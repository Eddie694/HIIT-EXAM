from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    messageus = models.TextField(max_length=250)

    def __Str__(self):
        return self.name + ' ' + self.subject 