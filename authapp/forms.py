import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import MyUser


# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.help_text = None


class ApplicantRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('profile_type', 'phone', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        # self.fields.pop('password1')
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = None
            # del self.fields['password2']
            # self.fields['password1'].help_text = "azaza"
            # self.fields['username'].help_text = None


    def save(self, **kwargs):
        user = super(ApplicantRegistrationForm, self).save()

        user.is_active = False
        # salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        # user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class CompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'company_name', 'password1', 'password2', 'email',
                  'company_main_business', 'company_since', 'company_about', 'file')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = None

    def save(self, **kwargs):
        user = super(CompanyRegistrationForm, self).save()

        user.is_active = False
        # salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        # user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user