from django.contrib import admin 
from django.urls import path
from . import views

urlpatterns = [
   path('admin/',admin.site.urls),
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('delete/<int:todo_id>/',views.deleteItem,name='deleteItem')
    
]