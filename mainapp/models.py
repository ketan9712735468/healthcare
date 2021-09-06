from django.db import models
from django.utils.text import slugify


class Service_type(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)

    


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service_type, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


















# Create your models here.
# class Slider(models.Model):
#     caption = models.CharField(max_length=150)
#     slogan = models.CharField(max_length=120)
#     image = models.ImageField(upload_to='sliders/')
#
#     def __str__(self):
#         return self.caption[:20]
#
#     class Meta:
#         verbose_name_plural = 'Slider'


# class Service(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     items = models.ManyToManyField(to='Item',)
#     thumbnail = models.ImageField(upload_to='serviceapp/')
#     cover = models.ImageField(upload_to='serviceapp/')
#     image1 = models.ImageField(upload_to='serviceapp/', blank=True, null=True)
#     image2 = models.ImageField(upload_to='serviceapp/', blank=True, null=True)
#
#     def __str__(self):
#         return self.title


# class Item(models.Model):
#     title = title = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.title


# class Doctor(models.Model):
#     name = models.CharField(max_length=120)
#     speciality = models.CharField(max_length=120)
#     picture = models.ImageField(upload_to="doctors/")
#     details = models.TextField()
#     experience = models.TextField()
#     expertize = models.ManyToManyField(to='Expertize', related_name='doctors')
#     twitter = models.CharField(max_length=120, blank=True, null=True)
#     facebook = models.CharField(max_length=120, blank=True, null=True)
#     instagram = models.CharField(max_length=120, blank=True, null=True)
#
#     def __str__(self):
#         return self.name


# class Expertize(models.Model):
#     name = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.name


# class Faq(models.Model):
#     question = models.CharField(max_length=120)
#     answer = models.TextField()
#
#     def __str__(self):
#         return self.question


# class Gallery(models.Model):
#     title = models.CharField(max_length=120)
#     image = models.ImageField(upload_to="gallery/")
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name_plural = "Galleries"