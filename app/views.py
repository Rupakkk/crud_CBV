from django.shortcuts import render
from django.views import View
from .models import Student
from .serializer import StudentSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name = 'dispatch')
class Student(View):

    
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id',None)  # If python data has any value then it gives it otherwise it gives None
            if id is not None:
                stu =  Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data) 

            stu =  Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return JsonResponse(serializer.data,safe=False)  # For non dictionary

            
    def post(self,request,*args,**kwargs):
        if request.method == "POST":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serialize = StudentSerializer(data = python_data)  # Important
            if serialize.is_valid():
                serialize.save()
                serializer = {'msg':'Data creation Successful'}
                return JsonResponse(serializer)
            data = {'msg':'Data Creation Unsuccessful'}
            return JsonResponse(data)

    def put(self,request,*args,**kwargs):
        if request.method == "PUT":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            serialize = StudentSerializer(stu,data = python_data)  # Important
            if serialize.is_valid():
                serialize.save()
                msg = {'msg':'Data creation Successful'}
                return JsonResponse(msg)
            return JsonResponse(serialize.errors)


    def delete(self,request,*args,**kwargs):
        if request.method == "DELETE":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            msg = {'msg':'Data deletion Successful'}
            return JsonResponse(msg)
            


