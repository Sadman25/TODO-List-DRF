from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import taskSerializer
from .models import todoList
# Create your views here.

@api_view(['GET'])
def taskList(request):
    tasks = todoList.objects.all().order_by('-id')
    serializer = taskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request,pk):
    
    try:
        task = todoList.objects.get(id=pk)
        serializer = taskSerializer(task, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def taskCreate(request):
    serializer = taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST'])
def taskEdit(request,pk):
    try:
        task = todoList.objects.get(id=pk)
        serializer = taskSerializer(instance=task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    except:
        return Response("Item not Found",status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def taskDelete(request,pk):
    try:
        task = todoList.objects.get(id=pk)
        task.delete()
        return Response("Item Successfully Deleted !!",status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
