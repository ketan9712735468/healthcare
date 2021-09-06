"""doctorservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django import views
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    # path('', views.index, name='doctor'),
    # path('all', views.index),
    path('', views.service_list_view),
    # path('all', views.ServiceListView.as_view()),
    path('clinici/', views.clinics_menu, name="clinics"),
    path('diagnostic/', views.diagnostic_menu, name="diagnostic"),
    path('laboratoare/', views.loborators_menu, name="labs"),
    path('stomatologii/', views.stomatology_menu, name="stomatology"),
    path('<str:service_doc>/', views.serviciu_domain_type, name='serviciu_domain'),
    path('detail-page/<int:pk>/', views.detaildoc, name="serviciu_details"),
    # path('detail-page/<int:pk>/apointment', views.get_apointment_data, name='getapointment'),
    # path('detail-page/<int:pk>/addreview', views.get_reviws_data, name='addreview'),

    # path('doctors/detail-page/<int:pk>/', views.DoctorDetailView.as_view(),
    #      name="doctor_details"),
    # path('doctors/apointment', views.get_apointment_data, name='getapointment')
    # path('admin/', admin.site.urls),

]
