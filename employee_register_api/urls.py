from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('employee/', views.employee_form),
    path('position/')
]