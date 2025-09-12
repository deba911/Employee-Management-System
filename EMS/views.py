from django.http import HttpResponse
from django.shortcuts import render, redirect

import datetime

def home(request):
    isActive = True
    if request.method=='POST':
        check = request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True
    date=datetime.datetime.now()

    return render(request,"home.html")