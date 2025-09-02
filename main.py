from metodos import funcoes

SALAS = ["Sala A", "Sala B", "Sala C"]
HORARIOS = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]

agenda = funcoes.inicializarAgenda(SALAS, HORARIOS)

while True:
    funcoes.cabecalho('Sistema de Reservas')
    funcoes.menu()
    try:
        op = int(input('Sua opção: '))
        
        if op == 4:
            print('Saindo do Programa...')
            break
        elif op == 1:
            funcoes.verAgenda(agenda, HORARIOS)
        elif op == 2:
            pass
        elif op == 3:
            pass
        else:
            print('Opção inválida! Selecione apenas dentre as opções disponiveis! ')
    except:
        print('ERRO! Digite apenas números...')
