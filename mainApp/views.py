from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import *

def ustozlar(request):
    context = {
        'ustozlar': Ustoz.objects.all()
    }
    return render(request, 'ustozlar.html', context)


def ustoz_tahrirlash(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    if request.method == 'POST':
        ustoz.ism = request.POST.get('ism')
        ustoz.jins = request.POST.get('jins')
        ustoz.yosh = request.POST.get('yosh')
        ustoz.daraja = request.POST.get('daraja')
        ustoz.fan=Fan.objects.get(id=request.POST.get('fan_id'))
        ustoz.save()
        return redirect('ustozlar')
    context = {
        'ustoz': ustoz,
        'fanlar': Fan.objects.all()
    }
    return render(request, 'ustoz_tahrirlash.html', context)