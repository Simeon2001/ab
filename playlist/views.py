from django.shortcuts import render
from .models import Urlinker
from django.views.generic.edit import CreateView
#Xreate Ur Function Here
def index (request):
    ur = Urlinker.objects.all()
    return render(request,'playlist/index.html',{'ur': ur})
def ask (request):
    return render(request,'playlist/ask.html')
    
#def share (request):
    #return render(request,'playlist/share.html')
    
class UrlinkerCreate(CreateView):
    model = Urlinker
    fields = ['username','website_link','description','images']