from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    index_page=render(request,'index.html',context)
    return index_page
def index1(request):
    context={}
    index_page=render(request,'index1.html',context)
    return index_page