from django.db import models

# Create your models here.
class BookAdvisor(models.Model):
    BookingId=models.BigAutoField
    BookingTime = models.DateTimeField(auto_now=False, auto_now_add=False)
