from django.shortcuts import render, redirect
from .models import Aluno
from .forms import *

def listar(request):
    #Aqui criamos uma lista com todas as instâncias de ALUNO
    alunos = Aluno.objects.all()
    return render(request, 'listar.html', {'alunos': alunos})

def adicionar(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('url_listar')
    else:
        return render(request, 'adicionar.html', {'form': form})

def atualizar(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    #   Acima estamos criando uma instância de AlunoForm e preenchendo seus campos com
    # as informações de ALUNO

    if form.is_valid():
        form.save()
        return redirect('url_listar')

    return render(request, 'upgrade.html', {'form': form, 'aluno': aluno})

#   Aqui criamos a Função deletar e passamos por parâmetro a chave primária
# de nosso objeto
def deletar(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect('url_listar')