# Modulo responsavel por ler e escrever na planilha do Excel.

from openpyxl import load_workbook

caminho_planilha = "Controle Restaurante.xlsx"
nome_aba_mov = "mov diarias"


def abir_planilha():
    wb = load_workbook(caminho_planilha)
    if nome_aba_mov not in wb.sheetnames:
        raise ValueError(f"A aba'{nome_aba_mov}'Não foi encontrado na planilha.")
    ws = wb [nome_aba_mov]
    return wb, ws

def proxima_linha_vazia(ws):
    return ws.max_row + 1

#Adiciona uma nova linha na aba movimentações.
def registrar_movimentacao(cliente, valor, data, hora, tipo_transacao, observacao=""):

    pass

#Lê todas as movimentações da aba de dados e devolve uma estrutura de dados.
def ler_movimentacoes():
    pass

#Usa ler_movimentacoes_por_data apenas as que têm a data desejada.
def filtrar_movimentações_por_data(data_referencia):
    pass

#Usa ler_movimentacoes e devolve apenas as que pertencem ao mês/ano informados.
def filtrar_movimentacoes_por_mes(mes,ano):
    pass

#Usa ler_movimentacoes e devolve apenas as de um cliente específico.
def filtrar_movimentacoes_por_cliente(nome_cliente):
    pass
