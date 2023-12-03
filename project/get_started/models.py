from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Country(models.Model): #for specific country requirements, not mandatory if client specifies only region-to check
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(max_length=100, unique=True) #to have a unique email address per user
    company = models.CharField(max_length=100, blank=True) #can be blank - not be provided-TBC
    country_of_benchmark = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    region_of_benchmark = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.name}, {self.last_name} {self.company}"