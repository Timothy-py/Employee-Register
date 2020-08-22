from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.employee_form),
    path('list/', views.employee_list),
]