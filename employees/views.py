from django.shortcuts import render
#from django.contrib.auth.models import employees
from django.http import HttpResponse
from django.shortcuts import get_object_or_404#if employees doesnot exist in data this is used 
# Create your views here.
from . models import employee
from . serializers import employeeSerializer
from rest_framework import status #with the 200 code status means everthing is okay
from rest_framework.views import APIView
from rest_framework.response import Response
'''
def get_queryset(self):
    user = self.request.user
    return user.accounts.all()'''

#def home(request):
 #   return HttpResponse("this is the main portal soaron")

class List_Employees(APIView):#inherited from APIView
    def get(self,request,format=None):
        #all_users=self.employee.objects.all() error bad waay using
        all_users=employee.objects.all()
        serializer=employeeSerializer(all_users,many=True)#which means returning all users
        #return HttpResponse
        return Response(serializer.data)# as we  going with endpoint using json for parsing the data 

    def post(self, request, format=None):
        serializer = employeeSerializer(data=request.data)
        #data={}
        if serializer.is_valid():
            serializer.save()
            #data['success']="new user have been created"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self):
        pass
    def delete(self):
        pass
    def update(self):
        pass


