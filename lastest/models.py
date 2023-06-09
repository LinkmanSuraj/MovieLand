from django.db import models

# Create your models here.
class latestCards(models.Model):
    l_photo=models.FileField(upload_to='cardmedia/',max_length=400,null=True,default=None)
    l_title=models.CharField(max_length=100)
    l_descript=models.CharField(max_length=1000)
    l_update=models.CharField(max_length=50)
    l_link=models.CharField(max_length=100,default=None)
