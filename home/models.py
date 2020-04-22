from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    
    def __str__(self):
        return ' Message From ' + self.name + ' - ' + self.email

    

        
    
class signUp(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    fname = models.CharField(max_length=12)
    lname = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=12)

    def __str__(self):
        return ' SignUp From ' + self.username + ' - ' + self.email
