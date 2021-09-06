from datetime import datetime, timedelta
from django.utils import timezone
import pytz
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models




from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#manager for our custom model
class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class
        https://stackoverflow.com/questions/37308246/django-how-to-save-my-hashed-password
        save without hash
    """
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username :
            raise ValueError("Users must have an Username")
        user  = self.model(
                email=self.normalize_email(email),
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    PROFILE = (
        ('Doctor', 'Doctor'),
        ('Company', 'Company'),
        ('Pacient', 'Pacient'),
        )
    profile_type = models.CharField(max_length=7, choices=PROFILE, default=PROFILE[0])
    birthday = models.IntegerField(verbose_name="Ziua de nastere", null=True, blank=True)
    phone = models.IntegerField(verbose_name="Telefon", null=True, blank=True, unique=True)
    user_about = models.TextField(verbose_name="Despre tine", null=True, blank=True)
    email = models.TextField(verbose_name="Email", unique=True, null=True)
    username = models.TextField(verbose_name="Username")
    # user_patronymic = models.CharField(verbose_name='Patronimic', max_length=150, null=True, blank=True)
    company_name = models.CharField("Numele Companiei", max_length=150, null=True, blank=True)
    company_about = models.TextField(verbose_name='Despre Companie', null=True, blank=True)
    company_main_business = models.CharField("Domeniu", max_length=150, null=True, blank=True)
    company_since = models.DateTimeField(verbose_name='Fondarea', null=True, blank=True)
    file = models.FileField(verbose_name='Foto', upload_to='avatars', blank=True)
    is_partner = models.BooleanField(verbose_name='Partener', blank=True, default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label ):
        return True

# class MyUser(AbstractUser):
#     DOCTOR = 2
#     HOSPITAL = 3
#     ROLE_CHOICES = (
#         (DOCTOR, 'Doctor'),
#         (HOSPITAL, 'Hospital'),
#     )
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
#
#     def __str__(self):
#         return self.username

    # activation_key = models.CharField(max_length=128, blank=True)
    # activation_key_expires = models.DateTimeField(
    #     verbose_name='Актуальность ключа',
    #     default=(timezone.now() + timedelta(hours=48))
    # )

    # def is_activation_key_expired(self):
    #     if datetime.now(pytz.timezone(settings.TIME_ZONE)) <= self.activation_key_expires:
    #         return False
    #     else:
    #         return True