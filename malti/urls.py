from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('index.html',views.index, name='index'),
    path('about_us.html',views.about_us, name='about_us'),
    path('login.html',views.login, name='login'),
    path('service.html',views.service, name='service'),
    path('modules.html',views.modules, name='modules'),
    path('contact_us.html',views.contact_us, name='contact_us'),
    path('contactus', views.contactus, name='contactus')
]