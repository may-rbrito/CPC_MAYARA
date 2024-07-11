from django.shortcuts import render
from rest_framework import generics
from .models import TemperatureRecord
from .serializers import TemperatureRecordSerializer

class TemperatureRecordListCreate(generics.ListCreateAPIView):
    queryset = TemperatureRecord.objects.all()
    serializer_class = TemperatureRecordSerializer
