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
# from doctorservice.mainapp import views

urlpatterns = [

    # path('', views.index, name='main'),
    # path('', views.HomeView.as_view(), name='main'),
    path('', views.homeview, name='main'),
    path('search/', views.choose_city, name='choose_city'),
    # path('search/<str:service_type>/<str:service_doc>/<str:location>/', views.deals_by_city, name='deals_by_city'), rabocia
    # path('<str:service_type>/<str:service_serv>/<str:location>-list', views.deals_by_city_serv, name='deals_by_city_serv'),
    path('<str:service_type>/<str:service_doc>/<str:location>-list', views.deals_by_city, name='deals_by_city'),

    # path('serviceapp/', views.ServiceListView.as_view(), name="serviceapp"),
    # path('serviceapp/<int:pk>/', views.ServiceDetailView.as_view(),
    #      name="service_details"),
    # path('doctors/', views.DoctorListView.as_view(), name="doctors"),
    # path('doctors/<int:pk>/', views.DoctorDetailView.as_view(),
    #      name="doctor_details"),
    # path('faqs/', views.FaqListView.as_view(), name="faqs"),
    # path('gallery/', views.GalleryListView.as_view(), name="gallery"),
    # path('contact/', views.ContactView.as_view(), name="contact")
]
