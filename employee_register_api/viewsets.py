from rest_framework import viewsets
from . import models, serializers


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class PositionViewset(viewsets.ModelViewSet):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer


