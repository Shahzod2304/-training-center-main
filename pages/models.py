from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=300)
    summary = models.CharField(max_length=250)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title