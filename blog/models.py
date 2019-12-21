from django.db import models

# Create your models here.
class POST(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=120)
    timeStamp = models.DateTimeField(blank=True)

    
    def __str__(self):
        return self.title + ' by ' + self.author
