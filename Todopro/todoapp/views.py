from django.shortcuts import render,HttpResponseRedirect
from todoapp.models import Studentdata

# Create your views here.
def home(request):
    stu_list=Studentdata.objects.all()
    return render(request, 'todoapp/home.html',{'stu_list':stu_list})


def add(request):
    data=Studentdata(name=request.POST['stuname'],rollno=request.POST['sturoll'],marks=request.POST['stumarks'])
    print(data)
    data.save()
    return HttpResponseRedirect('/home/')


def delete(request,stuid):
    data=Studentdata.objects.get(pk=stuid)
    data.delete()
    return HttpResponseRedirect('/home/')
