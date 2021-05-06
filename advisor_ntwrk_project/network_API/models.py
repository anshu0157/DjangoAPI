from django.db import models

# Create your models here.
class Advisor(models.Model):
    def nameFile(instance,filename):
        return '/'.join(['ProfilePics',str(instance.name),filename])

    id=models.BigAutoField
    name= models.CharField(max_length=60);
    photo= models.ImageField(upload_to=nameFile, default="") 
    def __str__(self):
        return self.name

# class User(models.Model):
#     id=models.BigAutoField
#     FullName=models.CharField(max_length=250)
#     Email=models.EmailField(max_length=200, unique=True)
#     def __str__(self):
#         return self.FullName
    
