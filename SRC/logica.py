#Módulo responsável pela lógica de negócio:
#Cálculo de saldos (diário, mensal, por cliente)
#Geração de relatórios mensais e anuais.

from datetime import date

#Calcula os dados de um dia.
def calcular_saldo_diario(data_referencia: date):
    pass

#Calcula o balanço do mês.
def calcular_saldo_mensal(mes: int, ano: int):
    pass

#Calcula os dados de um cliente individual.
def calcular_saldo_cliente(nome_cliente: str):
    pass

#Gera um relatório mensal.
def gerar_relatorio_mensal(mes: int, ano:int):
    pass

#Gera um relatório anual.
def gerar_relatorio_anual(ano: int):
    pass
