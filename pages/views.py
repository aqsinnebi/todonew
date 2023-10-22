from django.shortcuts import render
from .models import *
import datetime, time 





def index(request):
    
    return render(request, 'index.html')

def add(request):
    
    alltodos= Todo.objects.all()
    obj =Todo()
    
    obj.title = request.POST['title']
    obj.description =  request.POST['description']
    obj.created_at = request.POST['time']
    
    
    obj.save()
                            
    context={
        
        'alltodos':alltodos
    }
 
    return render(request, 'list.html',context)

def delete(request,id ):
    alltodos= Todo.objects.all()
    obj= Todo.objects.get(id=id)
    
    obj.delete()
    
    context={
            
            'alltodos':alltodos
        }

    return render(request, 'list.html', context)

def search(request):
    src= request.POST['query']

    alltodos= Todo.objects.filter(title__contains=src)
    
    context= {
            
            'alltodos':alltodos
        }
    
    return render(request, 'list.html', context)

def edit(request,id):
    
    obj= Todo.objects.get(id=id)
    
    title= obj.title
    description= obj.description
    priority= obj.priority
    id = obj.id
    
    context ={
       
       'title': title,
       'description':description,
        'priority':priority,
        'id': id,
    }
    return render(request, 'edit.html', context)

def update(request, id):
    alltodos= Todo.objects.all() 
    obj =Todo(id=id)

    obj.title = request.POST['title']
    obj.description = request.POST['description']
    
    update_at=datetime.datetime.now()
    
    obj.created_at= update_at
    
    obj.save()
    
    context={
        "alltodos":alltodos
    }
    
    return render(request, 'list.html', context)



def timee(request):
    
    alltodos= Todo.objects.all() 

    ret = ''
    pythonic_date = datetime.date.today()
    for i in range(0, 8):
        pythonic_date -= datetime.timedelta(days=1)
        ret=str
        ret += "SomePage" + datetime.date.today().strftime("%B" + " ")
        ret += str(pythonic_date.day).lstrip('0')
        ret += ", " + str(pythonic_date.year) + "|"
    ret = ret[0:len(ret) - 1]
    return render(request,'main/list.html',{'alltodos':alltodos})





  
   
    
    
	
	






