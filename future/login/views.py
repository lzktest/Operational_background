import requests
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from future import config
from .viewmodels.authmodels import auths
import json


# Create your views here.
def auth(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        aa = request.POST.get('authimage')
        return render(request, 'login/index.html', {'users': user, 'passwords': password, 'session':aa})
def checkout(request):
    from io import BytesIO
    from .viewmodels.authimages import check_code
    img, code = check_code()
    stream = BytesIO()
    img.save(stream, 'png')
    request.session['code'] = code
    return HttpResponse(stream.getvalue())
def index(request):
    return render(request, 'base.html')
def loginold(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        params = { 'name': user, "password": password, }
        head = {"Content-type":"application/json"}
        r = requests.post("%s/user/login" %(config.API_ADDR),data = json.dumps(params), headers = head )
        request.session = r.text
        print(r, r.text, 'aa', r.status_code)
        if r.status_code != 200 :
            raise Exception("%s : %s" % (r.status_code, r.text))
        j = r.json()
        return HttpResponse(request.session)

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user=request.POST.get('user')
        password=request.POST.get('password')
        print(user,password)
        try:
            dbuser = models.User.objects.get(username=user, password=password)
            print(dbuser.username)
            request.session['username'] =  dbuser.username
            print(request.session)
            return render(request,'login/indexs.html')
        except:
            return render(request,'login/login.html')

@auths(pages1='test')
def aa(request):
    return render(request,'login/indexs.html')
