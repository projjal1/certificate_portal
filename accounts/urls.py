from django.urls import path
from . import views

urlpatterns = [    
    path('signin/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('purge/',views.purge,name='purge')
]
