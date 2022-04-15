from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')
def user_list(request):
    return render(request, 'user_list.html')
def user_add(request):
    return HttpResponse('添加用户')
def tpl(request):
    name='洛潆'
    roles=['管理员','CEO','保安']
    user_info={'name':'洛潆','salary':'100000','role':'CEO'}
    return render(request,'tpl.html', {'n1':name,'n2':roles,'n3':user_info})
