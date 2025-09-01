SALAS = ["Sala A", "Sala B", "Sala C"]
HORARIOS = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]

def inicializarAgenda(salas, horarios):
    agendaGeral = {}

    for sala in salas:
        agendaDaSala = {}
        for horario in horarios:
            agendaDaSala[horario] = "Livre"
        agendaGeral[sala] = agendaDaSala
    
    return agendaGeral


print(inicializarAgenda(SALAS, HORARIOS))