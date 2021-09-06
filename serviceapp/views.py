from django.db.models import Q
from django.db.models import Avg, Value
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.forms.models import model_to_dict
from mainapp.views import context

from .forms import AppointmentFormService, ReviewsFormService
# from .models import Doctor, Review
from .models import Service, ReviewService, AppointmentService, LocationCompany, DomainService, SpecializationService
from django.views.generic import ListView, DetailView, TemplateView


# def index(request):
#     return render(request, 'doctors/doctor_list_freelance.html')
def service_list_view(request):
    # dictionary for initial data with
    # field names as keys

    # add the dictionary during initialization
    context["page_obj"] = LocationCompany.objects.all()

    return render(request, "serviceapp/service_list_freelance.html", context)

# class ServiceListView(ListView):
#     model = LocationCompany
#     template_name = 'serviceapp/service_list_freelance.html'
#
#
#     paginate_by = 4
#     extra_context = context




def detaildoc(request, pk):
    service = Service.objects.get(pk=pk)
    # print(service.rating)
    review = ReviewService\
        .objects.filter(doctor=service.id)
    # review.


    # print(review)
    # city = get_object_or_404(City, pk=city_id)
    # deals = Deal.objects.filter(city=city)
    content = {"doctor":service, "review":review, "data":context}
    # return render(request, 'doctors/detail_page.html', context)
    return render(request, 'serciceapp/service_detail_page_freelance.html', content)



def serviciu_domain_type(request, service_doc):

    # print(service_type)

    print(service_doc)
    doctors_domain = LocationCompany.objects.filter(domain__slug_domain=service_doc)
    print(doctors_domain)
    # data = context.update(doctors_domain)
    data = context
    data['serviciu_domain'] = doctors_domain
    return render(request, 'serviceapp/service_list_freelance.html', data )








def clinics_menu(request):
    clinics = LocationCompany.objects.filter(Q(clinic_type='Spital') | Q(clinic_type='Centru medical'))
    data = context
    data['clinics'] = clinics
    return render(request, 'serviceapp/service_list_freelance.html', data)
def diagnostic_menu(request):
    diagnostic = LocationCompany.objects.filter(clinic_type='Centru diagnostic')
    data = context
    data['diagnostic_center'] = diagnostic
    return render(request, 'serviceapp/service_list_freelance.html', data)

def loborators_menu(request):
    laborators = LocationCompany.objects.filter(clinic_type='Laborator')
    data = context
    data['laborators'] = laborators
    return render(request, 'serviceapp/service_list_freelance.html', data)

def stomatology_menu(request):
    stomatology = LocationCompany.objects.filter(clinic_type='Stomatologie')
    data = context
    data['stomatology'] = stomatology
    return render(request, 'serviceapp/service_list_freelance.html', data)











# class DoctorDetailView(DetailView):
#     template_name = 'doctors/team-details.html'
#     Model = Doctor
#
#     def get_context_data(self, **kwargs):
#         context = super(DoctorDetailView, self).get_context_data(**kwargs)
#         # context['detail_doc'] = Doctor.objects.filter(pk=self.object.pk)
#         context['detail_doc'] = Doctor.objects.all()
#         context['hui'] = "azaza"
#         print(context['detail_doc'])
#         print("hui")
#         return context

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
        # form = DetailForm(request.POST, request.FILES)
        # if form.is_valid():

def get_apointment_data(request, pk):
    # if request.method =='POST':
    #     name = request.POST
    #     print(name)
    # return redirect('/')
    form = AppointmentFormService()

    if request.method == 'POST':
        # print(request.POST)
        form = AppointmentFormService(request.POST)

        if form.is_valid():
            # print(form)
            form.save()
            return redirect('/serviciu/')


    return render(request,'serviceapp/service_list.html')

def get_reviws_data(request, pk):
    form = ReviewsFormService()
# NEED to USE PRECISE CALK# NEED to USE PRECISE CALK# NEED to USE PRECISE CALK# NEED to USE PRECISE CALK
    if request.method == 'POST':
        # print(request.POST)
        form = ReviewsFormService(request.POST)
        # mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['rate1'] = int(request.POST['rate1'])
        request.POST['rate2'] = int(request.POST['rate2'])
        request.POST['rate3'] = int(request.POST['rate3'])
        request.POST['rate4'] = int(request.POST['rate4'])
        request.POST['final_rate'] = (request.POST['rate1']+request.POST['rate2']+request.POST['rate3']+request.POST['rate4'])/4
        # print(request.POST['doctor'])
        review = ReviewService.objects.filter(doctor=request.POST['doctor']).aggregate(final_rate=Avg('final_rate'))
        print(review)
        print(request.POST['final_rate'])
        obj = Service.objects.get(pk=request.POST['doctor'])
        rating_final = (request.POST['final_rate'] + int(review['final_rate']))/2
        obj.rating = rating_final
        obj.save()
        request.POST['doctor'] = obj
        print(obj.rating)
        # request.POST._mutable = mutable
        # print(review)


        if form.is_valid():
            # print(form)
            form.save()
            return redirect('/doctor/')
        # print(form.errors)

    return render(request,'doctor/detail_page_freelance.html')