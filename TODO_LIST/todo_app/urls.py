from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.taskList,name='taskList'),
    path('taskCreate',views.taskCreate,name='taskCreate'),
    path('taskDetails/<str:pk>/',views.taskDetails,name='taskDetails'),
    path('taskEdit/<str:pk>/',views.taskEdit,name='taskEdit'),
    path('taskDelete/<str:pk>/',views.taskDelete,name='taskDelete'),
    
]
