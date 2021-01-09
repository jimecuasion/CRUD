from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name