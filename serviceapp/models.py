from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from authapp.models import MyUser
from mainapp.models import Service_type
from django.template.defaultfilters import slugify


from django.db import models


class SpecializationService(models.Model):
    specialization = models.CharField(max_length=90, blank=True, null=True)
    

    def __str__(self):
        return f"{self.specialization}"


class Service(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    # google_maps_link = models.CharField(max_length=500, blank=True, null=True)
    service_type = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    # location = models.ManyToManyField(LocationDoctor, related_name='doc_location')
    # location = models.ManyToManyField(LocationCompany, related_name='service_company_location')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    # children = models.BooleanField(blank=True, null=True)
    description_service = models.CharField(max_length=500, blank=True, null=True)
    # home_visit = models.BooleanField(blank=True, null=True)
    # online_consultation = models.BooleanField(blank=True, null=True)
    # rating = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

        # return f"{self.first_name} and {self.last_name}"

    def get_absolute_url(self):
        return reverse('doctor_details', kwargs={'pk': self.pk})

class DomainService(models.Model):
    # serviceapp = models.ManyToManyField(Service, blank=True)
    domain = models.CharField(max_length=30)
    services = models.ManyToManyField(Service, blank=True)
    title = models.CharField(max_length=200, blank=True)
    short_description = models.CharField(max_length=500, blank=True)
    long_description = models.CharField(max_length=1000, blank=True)
    specialization = models.ForeignKey(SpecializationService, on_delete=models.SET_NULL, blank=True, null=True)
    slug_domain = models.SlugField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug_domain)
        super(DomainService, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.domain}"


class LocationCompany(models.Model):
    CLINIC_TYPE = [
        ('Spital', 'Spital'),
        ('Centru medical', 'Centru medical'),
        ('Centru diagnostic', 'Centru diagnostic'),
        ('Laborator', 'Laborator'),
        ('Stomatologie', 'Stomatologie'),
        ('Medicină estetică', 'Medicină estetică'),
        ('Clinică FIV', 'Clinică FIV'),

    ]
    clinic_type = models.CharField(
        max_length=20,
        choices=CLINIC_TYPE,
        default='Centru medical',
    )
    company = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    doctors = models.ManyToManyField(MyUser, blank=True, related_name='company_doctors')
    domain = models.ManyToManyField(DomainService, blank=True)
    city = models.CharField(max_length=30)
    sector = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    google_maps_link = models.CharField(max_length=500, blank=True, null=True)
    slug_city = models.SlugField(max_length=30)
    slug_sector = models.SlugField(max_length=30)




    def save(self, *args, **kwargs):
        self.slug = slugify(self.city)
        self.slug_sector = slugify(self.sector)
        super(LocationCompany, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.city} and {self.slug_city} {self.domain}"






# class CompanyProfile(models.Model):
#
#
#
#     location = models.ManyToManyField(LocationCompany, related_name='company_location', null=True)
#

class AppointmentService(models.Model):
    doctor = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True, blank=True)
    otherinfo = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ReviewService(models.Model):
    rate1 = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate2 = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate3 = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rate4 = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    phone = models.CharField(max_length=12)
    comment = models.CharField(max_length=200)
    final_rate = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    doctor = models.ForeignKey(LocationCompany, max_length=50, on_delete=models.CASCADE)
