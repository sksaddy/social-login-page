from django.urls import path
from general import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thank-you', views.leave, name='leave'),
]

