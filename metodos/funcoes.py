
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

def verAgenda(agenda, listaDeHorarios):
    cabecalho("Agenda Completa")
    h = "Horario"
    print(f"{h.ljust(8)}| ", end="")
    for salas in agenda.keys():
        print(f"{salas.ljust(8)}| ", end="")
    print()
    print('-' * 40)

    for horario in listaDeHorarios:
        print(f"{horario.ljust(8)}| ", end="")
        for sala in agenda.values():
            print(f"{sala[horario].ljust(8)}| ", end="")
        print()
