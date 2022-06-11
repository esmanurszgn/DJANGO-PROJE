from audioop import add
import imp
from multiprocessing import context
from tkinter.messagebox import NO
from turtle import title
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import KullaniciMesajForm




from uygulama.models import Yazar,Dergi,KullaniciMesaj

def index(request):
    return render(request, "anasayfa.html")


def sayilarimiz(request):
    context = {
        "data" : Dergi.objects.all()
    }
    return render(request, "sayilarimiz.html", context)

def yazarlarimiz(request):
    context = {
        "data": Yazar.objects.all()
    }
    return render(request, "yazarlarimiz.html",context)

def yazigönder(request):
    submitted = False
    if request.method == "POST":
        form = KullaniciMesajForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('yazigönder?submitted=True')
    else:
        form = KullaniciMesajForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "yazigönder.html" , {'form': form, 'submitted':submitted})


def icerik(request,id):
    # if not request.user.is_authenticated:
    #  return redirect("anasayfa")
     

    dergi = Dergi.objects.get(id=id)
    
    return render(request , "icerik.html" , {
        "dergi" : dergi
    })

