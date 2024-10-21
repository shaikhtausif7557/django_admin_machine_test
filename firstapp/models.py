from django.db import models

# Create your models here.
class client(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    def __str__(self):
        return self.name

class User(models.Model):
    userName = models.CharField(max_length=255 , unique= True)
    email = models.EmailField(unique=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.userName
    


class projects(models.Model):
    pname = models.CharField(max_length=255)
    client = models.ForeignKey(client , related_name= 'projects' , on_delete=models.CASCADE)
    users = models.ManyToManyField(User , related_name='projects')


    def __str__(self):
        return self.pname
    
