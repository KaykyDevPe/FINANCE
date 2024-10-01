from django.shortcuts import render, redirect
from perfil.models import Categoria, Conta
from .models import ContaPagar, ContaPaga
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime

def definir_contas(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias})
    else:
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        dia_pagamento = request.POST.get('dia_pagamento')
        
        conta = ContaPagar(
            titulo=titulo,
            categoria_id=categoria,
            descricao=descricao,
            valor=valor,
            dia_pagamento=dia_pagamento,
        )
        
        conta.save()
        
        messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso!')
        return redirect('/contas/definir_contas')
    
def pagar_conta(request, id):
    conta = ContaPagar.objects.get(id=id)   
    
    conta_paga = ContaPaga(
        conta=conta,
        data_pagamento=datetime.now()
    )
    
    conta_paga.save()
    
    messages.add_message(request, constants.SUCCESS, 'Conta paga com sucesso')
    return redirect('/contas/ver_contas')
    
def ver_contas(request):
    MES_ATUAL = datetime.now().month
    DIA_ATUAL = datetime.now().day
    
    contas = ContaPagar.objects.all()
    
    contas_pagas = ContaPaga.objects.filter(data_pagamento__month=MES_ATUAL).values('conta')

    contas_vencidas = contas.filter(dia_pagamento__lt=DIA_ATUAL).exclude(id__in=contas_pagas)
    
    contas_proximas_vencimento = contas.filter(dia_pagamento__lte = DIA_ATUAL + 5 ).filter(dia_pagamento__gt=DIA_ATUAL).exclude(id__in=contas_pagas)

    restantes = contas.exclude(id__in=contas_vencidas).exclude(id__in=contas_proximas_vencimento).exclude(id__in=contas_pagas)
    
    return render(request, 'ver_contas.html', {'contas_vencidas': contas_vencidas, 
                                               'contas_proximas_vencimento': contas_proximas_vencimento, 
                                               'restantes': restantes})