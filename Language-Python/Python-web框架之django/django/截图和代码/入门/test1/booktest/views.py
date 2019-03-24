from django.shortcuts import render
from django.http import *
from .models import *
# from django.template import RequestContext,loader

def index(request):
    # temp=loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    bookList=BookInfo.objects.all()
    context={'list':bookList}
    return render(request,'booktest/index.html',context)

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={'list':herolist}
    return render(request,'booktest/show.html',context)
