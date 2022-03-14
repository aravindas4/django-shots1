from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)
    county = models.ForeignKey(Country, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # customer_address = models.CharField(max_length=255)
    # contact_person = models.CharField(max_length=255)
    # email = models.EmailField()
    # phone = models.CharField(max_length=255)

