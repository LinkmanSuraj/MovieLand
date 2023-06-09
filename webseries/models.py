from django.db import models

# Create your models here.
from django.db import models

class webcards(models.Model):
    w_photo=models.FileField(upload_to='webmedia/',max_length=700,null=True,default=None)
    w_title=models.CharField(max_length=100)
    w_descript=models.CharField(max_length=1000)
    w_update=models.CharField(max_length=50)
    w_link=models.CharField(max_length=300,default=None)
