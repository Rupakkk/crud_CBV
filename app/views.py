from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def stu_info(request):
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


     if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get(id)
        stu = Student.objects.get(id=id)
        serialize = StudentSerializer(data = stu)  # Important
        if serialize.is_valid():
            serialize.save()
            serializer = {'msg':'Data creation Successful'}
            return JsonResponse(serializer)
        data = {'msg':'Data Creation Unsuccessful'}
        return JsonResponse(data)






