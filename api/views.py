from django.shortcuts import render
from rest_framework.response import Response
from api import models
from api import serialisers
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

# Create your views here.
class StudentAPI(ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serialisers.StudentSerializer

class StudentDAPI(RetrieveUpdateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serialisers.StudentSerializer

class StudentDeAPI(DestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serialisers.StudentSerializer