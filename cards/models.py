from django.db import models

class movieCards(models.Model):
    photo=models.FileField(upload_to='cardmedia/',max_length=400,null=True,default=None)
    title=models.CharField(max_length=100)
    descript=models.CharField(max_length=1000)
    update=models.CharField(max_length=50)
    link=models.CharField(max_length=300,default=None)
 
    
