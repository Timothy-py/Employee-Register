from ..employee_register_api.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('employee', EmployeeViewset)