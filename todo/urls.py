from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    path('uncomplete/<todo_id>', views.uncomplete, name='uncomplete'),
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    path('deleteall', views.deleteAll, name='deleteall')
]
