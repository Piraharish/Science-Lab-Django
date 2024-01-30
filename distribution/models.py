from django.db import models

# Create your models here.
class dis_register(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.PositiveBigIntegerField()
    dateofbirth = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class distributor_form(models.Model):
    name = models.CharField(max_length=200)
    contactno = models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    dateofbirth =models.CharField(max_length=200)
    city =models.CharField(max_length=200, null=True)
    organisation = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    education = models.CharField(max_length=200, null=True)
    year_of_experience = models.PositiveIntegerField(null=True)
    approve=models.BooleanField(default=False)
