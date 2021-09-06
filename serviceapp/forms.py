from django.forms import ModelForm
from doctors.models import Appointment, Review


class AppointmentFormService(ModelForm):

    class Meta:
       model = Appointment
       fields = '__all__'


class ReviewsFormService(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
