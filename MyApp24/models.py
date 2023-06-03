from django.db import models

class Sign_Up(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username + ' | ' + self.Password


class Inventory(models.Model):
    Product = models.CharField(max_length=120, default='', blank=True, null=True)
    Typ = (('New', 'New'), ('Used', 'Used'))
    Cat = (('Phones', 'Phones'), ('Gadgets', 'Gadgets'))
    Ven = (('China', 'China'), ('Dubai', 'Dubai'))
    Type = models.CharField(max_length=50, default='', blank=True, null=True, choices=Typ)
    Category = models.CharField(max_length=50, default='', blank=True, null=True, choices=Cat)
    Quantity = models.IntegerField(default='', blank=True, null=True)
    Vendor = models.CharField(max_length=120, default='', blank=True, null=True, choices=Ven)
    Date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    Comments = models.TextField(max_length=1000, default='', blank=True, null=True)
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    


    def __str__(self):
        return self.Product + ' | ' + self.Category


    
    