from djongo import models

# Create your models here.


class Note(models.Model):
    body=models.CharField(max_length=500,blank=True,null=True,verbose_name="Add A Note Below")
