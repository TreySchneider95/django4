from django.urls import path
from formAssignment import views

urlpatterns = [
    path('', views.get_info, name='home'),
]