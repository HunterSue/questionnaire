from django.shortcuts import render
from django.http import HttpResponse
import json
from q1.models import user_massage
import random
# Create your views here.
#首页
def index(request):
    return render(request,"index.html",locals())

def add_massage(request):
    if request.method == "POST":
        #获取post请求
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        age = request.POST.get("age")
        sx = request.POST.get("sx")
        region = request.POST.get("region")
        #保存到数据库
        um = user_massage()
        um.name = name
        um.photo = phone
        um.age = age
        um.cz = sx
        um.region = region
        um.save()
        #产生幸运值
        number = random.randint(0,100)
        print(number)
        #返回数据
        state = {"number": number,
                 "state": "ok"}
        return HttpResponse(json.dumps(state, ensure_ascii=False), content_type="application/json,charset=UTF-8")
    else:#如果是get请求，发送报错
        state = {"tips": "Please input massage!",
                 "state": "ERROR"}
        return HttpResponse(json.dumps(state, ensure_ascii=False), content_type="application/json,charset=UTF-8")