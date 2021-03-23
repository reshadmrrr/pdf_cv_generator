from django.contrib import admin
from django.urls import path
from .views import accept, resume

urlpatterns = [
    path('', accept, name='accept'),
    path('<int:id>/', resume, name='resume'),
]