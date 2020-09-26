from django.shortcuts import render,redirect
from home.models import Content
# Create your views here.
def index(request):
    data= Content.objects.all()
    return render(request,'index.html',{'data':data})

def add(request):
    tododata= request.POST['todo']
    todo_item=Content(content=tododata)  #object of type Content
    todo_item.save()
    return redirect(index)
def deleteItem(request,todo_id):
    item = Content.objects.get(id=todo_id)
    item.delete()
    return redirect(index)
