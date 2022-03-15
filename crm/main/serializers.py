from rest_framework import serializers
from .models import *


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('first_name', 'patronymic', 'last_name', 'date_of_birth', 'languages', 'level', 'skills')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'description', 'country', 'address')
