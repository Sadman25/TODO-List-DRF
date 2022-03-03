from django.urls import path,include
from .import views

urlpatterns = [
    # path('',views.taskList,name='taskList'),
    # path('taskCreate',views.taskCreate,name='taskCreate'),
    # path('taskDetails/<str:pk>/',views.taskDetails,name='taskDetails'),
    # path('taskEdit/<str:pk>/',views.taskEdit,name='taskEdit'),
    # path('taskDelete/<str:pk>/',views.taskDelete,name='taskDelete'),

    path('',views.taskListView.as_view()),
    path('/taskCreate',views.taskCreateView.as_view()),
    path('/taskDetails/<str:pk>/',views.taskDetailsView.as_view()),
    # path('/taskDetails/<str:pk>/',views.taskDetailView.as_view()),
    # path('/taskEdit/<str:pk>/',views.taskEditView.as_view()),
    # path('/taskDelete/<str:pk>/',views.taskDeleteView.as_view()),
    
    
]
