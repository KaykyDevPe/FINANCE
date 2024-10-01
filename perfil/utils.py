from extrato.models import Valores
from datetime import datetime

def calcula_total(obj, campo):
    total = 0
    for i in obj:
        total += getattr(i, campo)
    return total

def calcula_equilibrio_financeiro():
    gastos_essencias = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='S').filter(categoria__essencial=True)
    gastos_nao_essencias = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='S').filter(categoria__essencial=False)
    
    total_gastos_essenciais = calcula_total(gastos_essencias, 'valor')
    total_gastos_nao_essenciais = calcula_total(gastos_nao_essencias, 'valor')
    
    total = total_gastos_essenciais + total_gastos_nao_essenciais
    
    try:
        percentual_gastos_essenciais = total_gastos_essenciais * 100 / total
        percentual_gastos_nao_essenciais = total_gastos_nao_essenciais * 100 / total
        
        return percentual_gastos_essenciais, percentual_gastos_nao_essenciais
    except:
        0, 0
        
def calcula_saldo_mensal():
    entrada_mensal = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='E')
    despesa_mensal = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='S')

    total_entrada_mensal = calcula_total(entrada_mensal, 'valor')
    total_despesa_mensal = calcula_total(despesa_mensal, 'valor')

    saldo_mensal = total_entrada_mensal - total_despesa_mensal
    
    return saldo_mensal, total_despesa_mensal, total_entrada_mensal
    