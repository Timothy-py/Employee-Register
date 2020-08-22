from employee_register_api.viewsets import EmployeeViewset, PositionViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('employee', EmployeeViewset)
router.register('position', PositionViewset)