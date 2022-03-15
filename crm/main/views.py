from django.shortcuts import render
from .serializers import PeopleSerializer, CompanySerializer
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
# Create your views here.

def index(request):
    return render(request, 'main/index.html')
def company(request):
    return render(request, 'main/company_two.html')


@api_view(['GET'])
def api_people(request):
    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_company(request):
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
