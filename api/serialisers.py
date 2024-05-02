from rest_framework import serializers
from api import models


class InstituteSerialiser(serializers.ModelSerializer):
    class Meta:
        model=models.Institute
        fields='__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    institute = InstituteSerialiser(read_only=True)
    class Meta:
        model=models.Student
        fields="__all__"