
from django.db.models import Avg, Value
from django.db.models.functions import Lower, datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.template.defaultfilters import lower
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.forms.models import model_to_dict
from mainapp.views import context

from .forms import AppointmentForm, ReviewsForm
from .models import Doctor, Review, Domain
from django.views.generic import ListView, DetailView, TemplateView
from mainapp.views import domain_doctor, servicii


# def index(request):
#     return render(request, 'mainapp/base_list.html')

def doctor_list_view(request):
    # dictionary for initial data with
    # field names as keys

    # add the dictionary during initialization
    context["page_obj"] = Doctor.objects.all()

    return render(request, "doctors/doctor_list_freelance.html", context)

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctor_list_freelance.html'
    # test = Review.objects.all().aggregate(suma=Avg('rate1'), suma2=Avg('rate2'), suma3=Avg('rate3'), suma4=Avg('rate4'))
    # all = Review.objects.all()
    # print(test)
    # print(test.get('suma'))
    # queryset = Doctor.objects.all()
    # print(queryset)
    # domains = Domain.objects.domain.all()
    # paginate_by = 25
    # extra_context = {"service_type": ["doctor", "service"], "service_doc": ["brodeaga", "ibati"],
    #                  "service_serv": ["glea", "iomaio"], "location": ["glea", "iomaio"]}
    # extra_context = context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['doctors'] = Doctor.objects.all()
    #     print(context)
    #     return context
    # class Meta:
    #     ordering = '-id'

def doctor_sort_by_rating(request, service_type='Doctor', location=None, service_doc=None):
    if service_type == 'Doctor':
        if location == None and service_doc == None:
            # page_obj = Doctor.objects.filter(service_type__slug=service_type, domain__slug=service_doc,
            page_obj = Doctor.objects.all().order_by(Lower('first_name'))
                                             # location__slug=location).values().order_by('-first_name', 'last_name')
            print(page_obj)
            data = context
            data['page_obj'] = page_obj
            return render(request, 'doctors/doctor_list_freelance.html', context=data)
        else:
            if service_type == 'Doctor':
                page_obj = Doctor.objects.filter(service_type__slug=service_type, domain__slug=service_doc,
                                                 location__slug=location).values().order_by(Lower('first_name'))

                data = context
                data['page_obj'] = page_obj
                return render(request, 'doctors/doctor_list_freelance.html', context=data)


def doctor_domain_type(request, service_doc):

    # print(service_type)
    service_doc = lower(service_doc)
    print(service_doc)
    doctors_domain = Doctor.objects.filter(domain__slug=service_doc)
    print(doctors_domain)
    # data = context.update(doctors_domain)
    data = context
    review = Doctor.objects.filter(domain__slug=service_doc).prefetch_related('review_set').count()
    data['page_obj'] = doctors_domain
    data['reviews'] = review
    print(review)
    return render(request, 'doctors/doctor_list_freelance.html', data )

def detaildoc(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    print(doctor.rating)
    review = Review.objects.filter(doctor=doctor.id)
    data = context
    data['obj'] = doctor
    data['review'] = review
    # data = {'data':data}
    # print(data)
    # print(review)
    # city = get_object_or_404(City, pk=city_id)
    # deals = Deal.objects.filter(city=city)
    content = data
    # return render(request, 'doctors/detail_page.html', context)
    return render(request, 'doctors/detail_page_freelance.html', content)



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
    form = AppointmentForm()

    if request.method == 'POST':
        print(request.POST)
        form = AppointmentForm(request.POST)

        if form.is_valid():
            print(form)
            form.save()
            return redirect('/doctor/')


    return render(request,'doctor/detail_page_freelance.html')

def get_reviws_data(request, pk):
    form = ReviewsForm()
# NEED to USE PRECISE CALK# NEED to USE PRECISE CALK# NEED to USE PRECISE CALK# NEED to USE PRECISE CALK
    if request.method == 'POST':
        print(request.POST)
        form = ReviewsForm(request.POST)
        # mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['rate1'] = int(request.POST['rate1'])
        request.POST['rate2'] = int(request.POST['rate2'])
        request.POST['rate3'] = int(request.POST['rate3'])
        request.POST['rate4'] = int(request.POST['rate4'])
        request.POST['final_rate'] = (request.POST['rate1']+request.POST['rate2']+request.POST['rate3']+request.POST['rate4'])/4
        # print(request.POST['doctor'])
        review = Review.objects.filter(doctor=request.POST['doctor']).aggregate(final_rate=Avg('final_rate'))
        print(review)
        print(request.POST['final_rate'])
        # obj = Doctor.objects.get(pk=request.POST['doctor'])
        obj = Doctor.objects.get(pk=request.POST['doctor'])
        if not review['final_rate']:
            now = datetime.datetime.now()
            difference = now.year - obj.experience_year.year
            print(f'diference {difference}')
            if difference > 10:
                review['final_rate'] = 4
            else:
                review['final_rate'] = 3


        print(review['final_rate'])
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
        print(form.errors)

    return render(request,'doctors/detail_page_freelance.html')