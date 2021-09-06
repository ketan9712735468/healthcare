from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from authapp.models import MyUser
from django.urls import reverse
from serviceapp.models import Service
from mainapp.models import Service_type
from django.template.defaultfilters import slugify


from django.db import models


class Specialization(models.Model):
    specialization = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return f"{self.specialization}"

class Domain(models.Model):
    domain = models.CharField(max_length=30)
    title = models.CharField(max_length=200, blank=True)
    short_description = models.CharField(max_length=500, blank=True)
    long_description = models.CharField(max_length=1000, blank=True)
    specialization = models.ManyToManyField(Specialization, blank=True)

    slug = models.SlugField(max_length=30)
    # sectors =

    def save(self, *args, **kwargs):
        self.slug = slugify(self.domain)
        super(Domain, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.domain}"


# class SectorLocationDoctor(models.Model):
#     location1 = models.CharField(max_length=30)
#     slug1 = models.SlugField(max_length=30)
    # sectors =

class LocationDoctor(models.Model):
    location = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    # sectors =

    def save(self, *args, **kwargs):
        self.slug = slugify(self.location)
        super(LocationDoctor, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.location} and {self.slug}"

class BusinessWork(models.Model):
    WEEKDAYS = [
        (1, ("Monday")),
        (2, ("Tuesday")),
        (3, ("Wednesday")),
        (4, ("Thursday")),
        (5, ("Friday")),
        (6, ("Saturday")),
        (7, ("Sunday")),
    ]

    weekday = models.IntegerField(
        choices=WEEKDAYS)
    from_hour = models.TimeField(null=True, blank=True)
    to_hour = models.TimeField(null=True, blank=True)
    weekend = models.CharField(max_length=30, null=True, blank=True)
    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __str__(self):
        return f"{self.weekday} from {self.from_hour} to {self.to_hour}"

class Procedure(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)



class Doctor(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    domain = models.ManyToManyField(Domain, blank=True)
    study_category = models.CharField(max_length=200, blank=True, null=True)
    study = models.TextField(max_length=1000, blank=True, null=True)
    course = models.TextField(max_length=1000,blank=True, null=True)
    experience_year = models.DateTimeField(auto_now_add= True, blank=True, null=True)
    publications = models.TextField(max_length=500, blank=True, null=True)
    experience_timeline = models.TextField(max_length=500, blank=True, null=True)
    award_scholarship = models.TextField(max_length=1000, blank=True, null=True)
    member_medical_association = models.CharField(max_length=500, blank=True, null=True)
    google_maps_link = models.CharField(max_length=500, blank=True, null=True)
    service_type = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    ## location = models.ManyToManyField(LocationDoctor, related_name='doc_location')
    location = models.ForeignKey(LocationDoctor, on_delete=models.SET_NULL, related_name='doc_location', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    children_visit = models.BooleanField(blank=True, null=True)
    description_service_consultation = models.CharField(max_length=500, blank=True, null=True)
    offer_services = models.ManyToManyField(Service, blank=True)
    offer_services_text = models.CharField(max_length=500, blank=True, null=True)
    home_visit = models.BooleanField(blank=True, null=True)
    online_consultation = models.BooleanField(blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    recomandation = models.BooleanField(blank=True, null=True)
    weekday = models.ManyToManyField(BusinessWork)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    specialization = models.ManyToManyField(Specialization, blank=True)
    clinica_text = models.CharField(max_length=100, blank=True, null=True)
    procedures = models.ManyToManyField(Procedure, blank=True)

    # WEEKDAYS = [
    #     (1, ("Monday")),
    #     (2, ("Tuesday")),
    #     (3, ("Wednesday")),
    #     (4, ("Thursday")),
    #     (5, ("Friday")),
    #     (6, ("Saturday")),
    #     (7, ("Sunday")),
    # ]
    # weekday = models.IntegerField(
    #     choices=WEEKDAYS)
    # from_hour = models.TimeField()
    # to_hour = models.TimeField()
    # class Meta:
    #     ordering = ('weekday', 'from_hour')
    #     unique_together = ('weekday', 'from_hour', 'to_hour')
    # https://stackoverflow.com/questions/12422332/django-opening-time-formset exemple
    # def __unicode__(self):
    #     return u'%s: %s - %s' % (self.get_weekday_display(),
    #                              self.from_hour, self.to_hour)
    def __str__(self):
        return f"{self.first_name} and {self.last_name}"

    def get_absolute_url(self):
        return reverse('doctor_details', kwargs={'pk': self.pk})


class Appointment(models.Model):
    doctor = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True, blank=True)
    otherinfo = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
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
    final_rate = models.FloatField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    doctor = models.ForeignKey(Doctor, max_length=50, on_delete=models.CASCADE)
