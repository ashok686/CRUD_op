import imp
from django.db import connections
from django.dispatch import receiver
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employer, user 
from .serializers import employerSerializers, userSerializers ,userEmployeeJoin
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import psycopg2

# from user.userprofile import serializers

# from user.userprofile import serializers

# Create your views here.
@csrf_exempt
def get(request):
    if request.method=='GET':
        allUsers = user.objects.all()
        print(allUsers);
        serializer = userSerializers(allUsers,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt        
def post(request):
    if request.method=='POST':
        receivedData = JSONParser().parse(request)
        serializer = userSerializers(data=receivedData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Succesfully',safe=False)
        return JsonResponse('Failed to add',safe=False)  

@csrf_exempt
def put(request):
    if  request.method=='PUT':
        receivedData = JSONParser().parse(request)
        user1 = user.objects.get(id=receivedData['id'])
        serializer = userSerializers(user1,data=receivedData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated successfully',safe=False)
        return JsonResponse('Update failed',safe=False)     

@csrf_exempt   
def delete(request,id=0):
    if request.method=='DELETE':
        user1 = user.objects.get(id=id)
        user1.delete()
        return JsonResponse('Deleted succesfully',safe=False)

@csrf_exempt 
def find(request,id=0):
    if request.method == 'GET':
        user1 = user.objects.get(id=id)
        serializer = userSerializers(user1)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def getEmployer(request):
    if request.method=='GET':
        allEmployers = Employer.objects.all()
        serializer = employerSerializers(allEmployers,many=True)
        return JsonResponse(serializer.data,safe=False)

        
    

@csrf_exempt
def createEmployer(request):
    if request.method=='POST':
        receivedData = JSONParser().parse(request)
        serializer = employerSerializers(data=receivedData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Employer added successfully',safe=False)
        return JsonResponse('Failed to add Employer',safe=False)    


@csrf_exempt
def deleteEmployer(request,id=0):
        if request.method=='DELETE':
            employer1 = Employer.objects.get(id=id)
            employer1.delete()
            return JsonResponse('Deleted succesfully',safe=False)



@csrf_exempt 
def joinUserEmployer(request):
    allusers = Employer.objects.all()
    serializer = userEmployeeJoin(allusers,many=True)
    return JsonResponse(serializer.data,safe=False)

def getKeyAndValue():
    allUsers = user.objects.filter(firstname = 'Ashok  ')
    print(allUsers)




getKeyAndValue()
        



   
    








       