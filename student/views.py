import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home_page(req):
    return HttpResponse('This is Home Page..s')

@csrf_exempt
def entry_page(req):
    username = req.POST.get('user')
    password = req.POST.get('pass')
    return HttpResponse(f"Username: {username}, Password: {password}")
    # return render(req,'login.html')

def home_page(req):
    username = req.POST.get('user')
    password = req.POST.get('pass')
    return render(req,'result.html',{'name':username,'pass':password})

# render -> backend
# aiven -> db