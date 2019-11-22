from django.urls import path
from . import views

urlpatterns = [    
    path('upload/',views.add_entry,name='uploads'),
]
