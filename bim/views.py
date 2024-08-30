from django.http import HttpResponse
from django.shortcuts import render


def form(request):
    data={
        'title':"Home page",
        'clist':['php','python']

    }
    return render(request,'index.html',data)