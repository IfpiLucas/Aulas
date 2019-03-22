from django.shortcuts import render,redirect
from django.views.generic import DeleteView
from .models import *
from .forms import *

def listaA(request):
    form = Aluno.objects.all()
    return render(request,'listaA.html', {'form':form})

def addA(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('lista')
    else:
        return render(request,'adiciona.html',{'form':form})
