from django.shortcuts import render
from api.models import *
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
import pymysql

class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        #database = pymysql.connect(host="localhost", user="root", password="33649464", database="bjpowernode",charset='utf8')
        for item in request.data:
            print(item)
            print(request.data[item])
            #增
            UserInfo.objects.create(name=item,password=request.data[item],age=18)
            #删
            #UserInfo.objects.all().delete() 删除所有数据
            #data_list = UserInfo.objects.filter(id=3).delete() #只删某一行
            #查
            # data = UserInfo.objects.all() #获取表中所有数据
            # for obj in data:
            #     print(obj.name,obj.password,obj.age)
            #data_list = UserInfo.objects.filter(id=3) #只选某一行
            #data_list = UserInfo.objects.filter(id=3).first() #直接提取数据
            #更新
            # UserInfo.objects.filter(id=3).update(age=999) #该一行
            # UserInfo.objects.all().update(age=999) #改所有
        return Response({'status':True})





