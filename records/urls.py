from django.urls import path
from . import views

urlpatterns = [    
    path('get_certificate/',views.fetch,name='fetch'),
    path('certify/',views.certificate_gen,name='cert_gen'),
]
