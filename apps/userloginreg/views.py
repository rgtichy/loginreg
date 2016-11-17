from django.shortcuts import render, redirect
from . import models
# Create your views here.
# home route
def index(request):
    context = {}
    return render(request,'userloginreg/index.html',context)
def login(request):
    context = {}
    try:
        return render(request,'userloginreg/success.html',context)
    except:
        return redirect(index)
def register(request):
    context = {}
    ( flag , data ) = models.User.objects.register(request.POST)
    print "Got Here!"
    if flag == True:
        print "Successful Registration"
        context={'new_user':data}
        return render(request,'userloginreg/success.html',context)
    else:
        print "Something didn't work"
        return redirect(index)
