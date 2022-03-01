from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import taskSerializer
from .models import todoList
# Create your views here.

@api_view(['GET'])
def taskList(request):
    tasks = todoList.objects.all()
    serializer = taskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request,pk):
    tasks = todoList.objects.get(id=pk)
    serializer = taskSerializer(tasks, many=False)
    return Response(serializer.data)