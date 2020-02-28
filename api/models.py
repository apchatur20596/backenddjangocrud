from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.IntegerField()
    location = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email_id = models.EmailField(max_length=100, unique=True)
    joining_date = models.DateField(auto_now_add=True)
    last_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

