from django.urls import path
from .views import main_view, task_list, add_task

urlpatterns = [
    # path("", main_view , name="main_view"), 
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),

]