from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.taskList,name='taskList'),
    path('taskDetails/<str:pk>/',views.taskDetails,name='taskDetails'),
    
]
