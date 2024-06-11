from django.urls import path
from .views import main_view, task_list, add_task, delete_task, edit_task

urlpatterns = [
    # path("", main_view , name="main_view"), 
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('edit/<int:id>', edit_task, name='edit_task'),

]