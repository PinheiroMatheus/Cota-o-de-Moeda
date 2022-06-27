import PySimpleGUI as sg
from cotacao import pegar_cotacoes

sg.theme("DarkGreen")

layout = [
    [sg.Text("Digite o código da moeda", key="texto_cotacao")],
    [sg.InputText(key="nome_cotacao", do_not_clear = False)],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("", key="valor_cotacao")],
]

janela = sg.Window("Sistema de Cotações", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar Cotação":
        codigo_cotacao = valores["nome_cotacao"].upper()
        cotacao = pegar_cotacoes(codigo_cotacao)
        if cotacao != None:
            janela["valor_cotacao"].update(f"A cotação do {codigo_cotacao} é de R${cotacao}")
        else:
            janela["valor_cotacao"].update(f"O código '{codigo_cotacao}' é inválido. Por favor digite outro!")
            
janela.close()