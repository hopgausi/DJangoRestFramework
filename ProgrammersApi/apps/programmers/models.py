from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField()

    def __str__(self):
        return self.name


class Programmer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    languages = models.ManyToManyField(Language)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'    



