
def inicializarAgenda(salas, horarios):
    agendaGeral = {}

    for sala in salas:
        agendaDaSala = {}
        for horario in horarios:
            agendaDaSala[horario] = "Livre"
        agendaGeral[sala] = agendaDaSala
    
    return agendaGeral

def cabecalho(msg=""):
    tam = 40
    print('-' * tam)
    print(f"{msg}".center(tam))
    print('-' * tam)

def menu():
    print('1. Ver Agenda Completa\n2. Fazer Reserva\n3. Cancelar Reserva\n4. Sair')