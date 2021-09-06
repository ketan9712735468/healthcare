from django.contrib import admin

from doctors.models import Specialization, Domain, Doctor, Appointment, Review, LocationDoctor, BusinessWork

admin.site.register(Specialization)
admin.site.register(Domain)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(LocationDoctor)
admin.site.register(BusinessWork)