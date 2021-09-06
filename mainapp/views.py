from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
from . models import Service_type
from doctors.models import Domain, LocationDoctor, Doctor

from doctors.models import Doctor
from serviceapp.models import Service, LocationCompany, DomainService
# from .models import Slider, Faq, Gallery, Service
from django.views.generic import ListView, DetailView, TemplateView

domain_doctor = ['Acupunctor','Alergolog','Androlog','Cardiochirurg','Cardiolog','Cardiolog intervenţionist','Chirurg','Chirurg estetician','Chirurg plastician',
'Cosmetolog',
'Dermatolog',
'Dietolog',
'Nutriționist',
'Ecografist',
'Endocrinolog',
'Endoscopist',
'Fitoterapeut',
'Fizioterapeut',
'Flebolog',
'Gastroenterolog',
'Ginecolog',
'Hematolog',
'Hepatolog',
'Homeopat',
'Imagist',
'Infecționist',
'Internist',
'Kinetoterapeut',
'Logoped',
'Mamolog',
'Medic de familie',
'Narcolog',
'Nefrolog',
'Neurochirurg',
'Neurolog',
'Obstetrician-ginecolog',
'Oftalmolog',
'Oncolog',
'Ortoped-traumatolog',
'Otorinolaringolog (ORL)',
'Pediatru',
'Pneumolog',
'Proctolog',
'Psihiatru',
'Psiholog',
'Psihoterapeut',
'Reabilitolog',
'Reanimatolog-neonatolog',
'Reflexoterapeut',
'Reumatolog',
'Sexolog',
'Specialist în masaj',
'Stomatolog',
'Terapeut manual',
'Triholog',
'Urolog',
'Venerolog',
'Vertebrolog']

servicii = ['ULTRASONOGRAFIE',
'neurosonografia prin fontanelă',
'ecografie glanda tiroidă',
'ecografie abdominală',
'ecografie sistemul urinar',
'ecografie bazinul mic',
'ecografie complexă',
'ULTRASONOGRAFIE2',
'neurosonografia prin fontanelă',
'ecografie glanda tiroidă',
'ecografie abdominală',
'ecografie sistemul urinar',
'ecografie bazinul mic',]

serviciu_domen = [
'Ultrasonografie',
'Ultrasonografie obstetrică',
'Ultrasonografia musculoscheletară',
'Mamografie',
'Radiografie',
'Tomografie computerizată',
'Electrocardiografie (ECG)',
'Ecocardiografie',
'Monitorizare cardiologică Holter',
'Elastografia',
'Electroencefalografia (EEG)',
'Sonodopplerografia',
'Investigații endoscopie de diagnostic',
'Densitometria osoasă',
'Angiografie prin TC',
'Bronhoscopie virtuală',
'Diagnostic de laborator',
'Înregistrarea investigației pe fotografie',
'Înregistrarea investigației pe CD',]
context = {"service_type": ["Doctor", "Serviciu"], "service_doc": domain_doctor,
           "service_serv": servicii, "service_domain": serviciu_domen, "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca', 'Rîșcani', 'Telecentru']}


def homeview(request):
    # context = {"service_type":["doctor","service"], "service_doc":["brodeaga", "ibati"], "service_serv":["glea", "iomaio"], "location":["glea", "iomaio"]}
    return render(request, 'mainapp/base_new.html', context)


def choose_city(request):
    # print(request.POST['service_type'])
    # print(request.POST['service_type'])
    # print(request.POST.get('service_doc'))
    # print(request.POST['service_serv'])

    if request.POST.get('service_doc'):
        service_type = slugify(request.POST['service_type'])
        service_doc = slugify(request.POST['service_doc'])
        location = slugify(request.POST['location'])
        return redirect('deals_by_city', permanent=True, service_type=service_type, service_doc=service_doc, location=location)
    else:
        service_type = slugify(request.POST['service_type'])
        service_serv = slugify(request.POST['service_serv'])
        print(service_serv)
        print("ds")
        location = slugify(request.POST['location'])
        return redirect('deals_by_city_serv', permanent=True, service_type=service_type, service_serv=service_serv, location=location)


def deals_by_city(request, service_type=None, location=None, service_serv=None, service_doc=None):
    print(service_serv)
    print(service_type)
    if service_type == 'doctor':
        print(service_serv)
        print(location)
        print(service_doc)
        # city = get_object_or_404(City, pk=city_id)
        # deals = Deal.objects.filter(city=city)
        page_obj = Doctor.objects.filter(service_type__slug=service_type, domain__slug=service_doc, location__slug=location)
        print(page_obj)
        # print(dir(request.environ))
        # full_context = context
        # full_context.update(page_obj)


        # print(page_obj)
        return render(request, 'doctors/doctor_list_freelance.html', context={'page_obj':page_obj, "service_type": ["Doctor", "Serviciu"], "service_doc": domain_doctor,
               "service_serv": servicii, "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca', 'Rîșcani', 'Telecentru']})
    else:
        print(request.POST)
        print(service_type)
        print(service_serv)
        # service_type = None
        # service_serv = None
        # location = None
        # page_obj = Service.objects.filter(name="service_2")
        # second = DomainService.objects.prefeth_related()
        # page_obj = LocationCompany.objects.filter(service_type__slug=service_type, domain__slug=service_serv)
                                         # city__slug=location)
                                         # city__slug=location, sector__slug=location)
        print(service_serv)
        page_obj = LocationCompany.objects.filter(
            Q(slug_city=location) | Q(sector='some sector'),
            domain__slug_domain=service_serv,
            # or query for city or sector
        ).distinct()
        print(page_obj)
        return render(request, 'serviceapp/service_list_freelance.html',
                      context={'page_obj': page_obj, "service_type": ["Doctor", "Serviciu"],
                               "service_doc": domain_doctor,
                               "service_serv": servicii,
                               "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca',
                                            'Rîșcani', 'Telecentru']})



def deals_by_city_serv(request, service_type=None, location=None, service_serv=None, service_doc=None):
    print(service_serv)
    if service_type == 'doctor':
        print(service_serv)
        # city = get_object_or_404(City, pk=city_id)
        # deals = Deal.objects.filter(city=city)
        page_obj = Doctor.objects.filter(service_type__slug=service_type,domain__slug=service_doc,location__slug=location).values()
        # print(dir(request.environ))
        # full_context = context
        # full_context.update(page_obj)
        # print(page_obj)

        return render(request, 'doctors/doctor_list_freelance.html', context={'page_obj':page_obj, "service_type": ["Doctor", "Serviciu"], "service_doc": domain_doctor,
               "service_serv": servicii, "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca', 'Rîșcani', 'Telecentru']})
    else:
        print(request.POST)
        print(service_type)
        print(service_serv)
        print(location)
        # service_type = None
        # service_serv = None
        # location = None
        # page_obj = Service.objects.filter(name="service_2")
        # second = DomainService.objects.prefeth_related()
        # page_obj = LocationCompany.objects.filter(service_type__slug=service_type, domain__slug=service_serv)
                                         # city__slug=location)
                                         # city__slug=location, sector__slug=location)
        sectoare = ['botanica', 'telecentru', 'buiucani', 'centru', 'ciocana', 'rascani']
        domenii = ['ultrasonografie']

        if location in sectoare:
            if service_serv in domenii:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_sector=location) | Q(slug_city=location),
                    domain__slug_domain=service_serv,
                ).distinct()
            else:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_sector=location) | Q(slug_city=location),
                    services__name=service_serv,
                ).distinct()
        else:
            if service_serv in domenii:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_city=location) | Q(sector='some sector'),
                    domain__slug_domain=service_serv,
                    # or query for city or sector
                ).distinct()
            else:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_city=location) | Q(sector='some sector'),
                    services__name=service_serv,
                    # or query for city or sector
                ).distinct()

        data = context
        data['page_obj'] = page_obj
        return render(request, 'serviceapp/service_list_freelance.html', context=context)
                      # {'page_obj': page_obj, "service_type": ["Doctor", "Serviciu"],
                      #          "service_doc": domain_doctor,
                      #          "service_serv": servicii,
                      #          "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca',
                      #                       'Rîșcani', 'Telecentru']})






# class HomeView(ListView):
#     template_name = 'base_list.html'
#     queryset = Service.objects.all()
#     context_object_name = 'serviceapp'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['sliders'] = Slider.objects.all()
#         context['experts'] = Doctor.objects.all()
#         return context
#
# #
# class ServiceListView(ListView):
#     queryset = Service.objects.all()
#     template_name = "serviceapp/serviceapp.html"
#
#
# class ServiceDetailView(DetailView):
#     queryset = Service.objects.all()
#     template_name = "serviceapp/service_details.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["serviceapp"] = Service.objects.all()
#         return context


# class DoctorListView(ListView):
#     template_name = 'serviceapp/team.html'
#     queryset = Doctor.objects.all()
#     paginate_by = 8


# class DoctorDetailView(DetailView):
#     template_name = 'serviceapp/team-details.html'
#     queryset = Doctor.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["doctors"] = Doctor.objects.all()
#         return context


# class FaqListView(ListView):
#     template_name = 'serviceapp/faqs.html'
#     queryset = Faq.objects.all()
#
#
# class GalleryListView(ListView):
#     template_name = 'serviceapp/gallery.html'
#     queryset = Gallery.objects.all()
#     paginate_by = 9
#
#
# class ContactView(TemplateView):
#     template_name = "serviceapp/contact.html"
#
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         if subject == '':
#             subject = "Heartcare Contact"
#
#         if name and message and email and phone:
#             send_mail(
#                 subject+"-"+phone,
#                 message,
#                 email,
#                 ['expelmahmud@gmail.com'],
#                 fail_silently=False,
#             )
#             messages.success(request, " Email hasbeen sent successfully...")
#
#         return redirect('contact')
