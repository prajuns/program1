from django.db import models
# Create your models here.
class Bird(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='photos')
    desc=models.TextField()