from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    tags = ['น้ำตก','ธรรมชาติ','หน้าฝน','ตากหมอก']
    return render(request,'index.html',
    {
        'name':'Kridtakom  Boom',
        'tags': tags,
        'rating': 5
    })

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def addForm(request):
    name = request.POST['name']
    description = request.POST['description']
    return render(request,'result.html',{'name':name,'description':description})
