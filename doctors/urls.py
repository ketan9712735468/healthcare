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

    # path('', views.index, name='doctor'),
    path('', views.doctor_list_view, name="doctors"),
    # path('<str:domain_type>/', views.doctor_domain_type, name='doctor_domain'),
    path('sortrating/', views.doctor_sort_by_rating, name='doctor_sort_by_rating'),
    # path('<str:service_doc>/', views.doctor_domain_type, name='doctor_domain'),
    path('<str:service_doc>/', views.doctor_domain_type, name='doctor_domain'),

    path('<str:service_type>-<str:service_doc>-<str:location>/sort_rating/', views.doctor_sort_by_rating, name='doctor_sort_by_rating'),
    path('detail-page/<int:pk>/', views.detaildoc, name="doctor_details"),
    path('detail-page/<int:pk>/apointment', views.get_apointment_data, name='getapointment'),
    path('detail-page/<int:pk>/addreview', views.get_reviws_data, name='addreview'),

    # path('doctors/detail-page/<int:pk>/', views.DoctorDetailView.as_view(),
    #      name="doctor_details"),
    # path('doctors/apointment', views.get_apointment_data, name='getapointment')
    # path('admin/', admin.site.urls),

]

