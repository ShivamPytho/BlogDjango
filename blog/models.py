from django.db import models

# Create your models here.
class POST(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    timeStamp = models.DateTimeField(blank=True)

    
    def __str__(self):
        return sno
