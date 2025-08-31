from django.urls import path, include
from . import views

urlpatterns=[
    path('email_validation',views.email_validation, name='email_validation'),
    path('phone_validation',views.phone_validation, name='phone_validation'),
    path('ip_validation',views.ip_validation, name='ip_validation'),
    path('url_validation',views.url_validation, name='url_validation'),
    path('file_validation',views.file_validation, name='file_validation'),
    path('file_behavioral',views.file_behavioral, name='file_behavioral'),
    path('index.html',views.index, name='index'),
    path('about_us.html',views.about_us, name='about_us'),
    path('login.html',views.login, name='login'),
    path('service.html',views.service, name='service'),
    path('modules.html',views.modules, name='modules'),
    path('contact_us.html',views.contact_us, name='contact_us')
]