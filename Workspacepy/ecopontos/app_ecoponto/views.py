
from django.http import HttpResponse
from django.shortcuts import render
from .models import Classes,Usuario,Descartadores




# Create your views here.


def listview(request):
    td={
        "data": Classes.objects.all(),
        "data1":Usuario.objects.all(),
        "data2":Descartadores.objects.all()
    }
   
    return render(request, 'inicial.html', td)
   


