from django.shortcuts import render,HttpResponse,Http404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
import re


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .serializers import taskSerializer,UserSerializer,LoginSerializer
from .models import todoList
# Create your views here.

class userRegistrationView(GenericAPIView):
    
    serializer_class = UserSerializer
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userLoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = LoginSerializer(data=request.data)

        user = authenticate(request,username=request.data["username"], password=request.data["password"])
    
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_202_ACCEPTED)
            
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class taskCreateView(APIView):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = taskSerializer

    def post(self,request):
        try:            
            newTask  = request.data["task"] 
            
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(newTask)==None):
                todoList.objects.create(task=newTask, user=request.user)            
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response('No special characters are allowed',status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class taskListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self,request):
        tasks = todoList.objects.all().order_by('-id')
        serializer = taskSerializer(tasks, many=True)
        print(request.user)
        return Response(serializer.data)         

class taskDetailsView(APIView):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return todoList.objects.get(id=pk)
        except:
            raise Http404()

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = taskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = taskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class taskDetailView(APIView):

#     def get_object(self,pk):
#         try:
#             return todoList.objects.get(id=pk)
#             # serializer = taskSerializer(task, many=False)
#             # return Response(serializer.data,status=status.HTTP_200_OK)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self,request,pk):
#         task = self.get_object(pk)
#         serializer = taskSerializer(task, many=False)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# class taskEditView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get_object(self,pk):
#         try:
#             return todoList.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk, format=None):
#         task = self.get_object(pk)
#         serializer = taskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class taskDeleteView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get_object(self,pk):
#         try:
#             return todoList.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk, format=None):
#         task = self.get_object(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET'])
# def taskList(request):
#     tasks = todoList.objects.all().order_by('-id')
#     serializer = taskSerializer(tasks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def taskDetails(request,pk):
    
#     try:
#         task = todoList.objects.get(id=pk)
#         serializer = taskSerializer(task, many=False)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def taskCreate(request):
#     serializer = taskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET','POST'])
# def taskEdit(request,pk):
#     try:
#         task = todoList.objects.get(id=pk)
#         serializer = taskSerializer(instance=task,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#     except:
#         return Response("Item not Found",status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['DELETE'])
# def taskDelete(request,pk):
#     try:
#         task = todoList.objects.get(id=pk)
#         task.delete()
#         return Response("Item Successfully Deleted !!",status=status.HTTP_204_NO_CONTENT)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
