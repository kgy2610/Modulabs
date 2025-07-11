# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('person/', views.person_query, name='person_query'),
]