from django.forms import ModelForm
from doctors.models import Appointment, Review


class AppointmentForm(ModelForm):

    class Meta:
       model = Appointment
       fields = '__all__'


class ReviewsForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
