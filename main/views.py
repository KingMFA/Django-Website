from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from main.models import Person
from main.forms import CreateNewPerson,AddSubjectToPerson
import datetime
# Create your views here.

def index(request):
    response = HttpResponseRedirect("/home/")
    return response

def home(request):
    p = Person.objects.all()
 
    response = render(request,"main/home.html",{"person": p})
    return response


def list(request,id):
  
    ls = Person.objects.get(id=id)
    if(request.method == "POST" and "save" in request.POST):
        form = AddSubjectToPerson(request.POST)
        if (form.is_valid()):
            sub = form.cleaned_data["subject"]
           
           
            reason = form.cleaned_data["reason"]
            
            ls.favoritesubject_set.create(subject=sub,reason=reason)
            ls.save()
    else:
        form = AddSubjectToPerson()
    response = render(request,"main/list.html",{"ls":ls,"form":form})
    return response

def create(request):
    if(request.method == "POST"):
        form = CreateNewPerson(request.POST)
        if (form.is_valid()):
            name1 = form.cleaned_data["first_name"]
            name2 = form.cleaned_data["last_name"]
            p = Person(first_name=name1, last_name=name2)
            
            p.save()
            sid = p.id
            return HttpResponseRedirect("/list/" + str(sid))
    else:
        form = CreateNewPerson()
            
           
    
    return render(request,"main/create.html",{"form":form})

def addSubject(request,NewID):
    
    if(request.method == "POST" and "save" in request.POST):
        form = AddSubjectToPerson(request.POST)
        if (form.is_valid()):
            sub = form.cleaned_data["subject"]
            per = form.cleaned_data["person"]
           
            reason = form.cleaned_data["reason"]
            l = Person.objects.get(id=per)
            l.favoritesubject_set.create(subject=sub,reason=reason)
            l.save()
            return redirect("/list/" + str(per))
    else:
        form = AddSubjectToPerson()
            
    return render(request,"main/newApp.html",{"form":form})


def removeTask(request,task_id,person):
    form = AddSubjectToPerson()
    p = Person.objects.get(id=person)
    if (request.method == "POST" and "deletor" in request.POST):
        
        item = p.favoritesubject_set.get(id=task_id)
        item.delete()
        p.save()

    return render(request,"main/list.html",{'ls':p,'form':form})