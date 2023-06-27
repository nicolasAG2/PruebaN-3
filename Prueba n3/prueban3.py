import funciones as fn
jugadores=[]
op=0
while op!=4:
    op=fn.menu()
    for i in range(len(jugadores)):
        print(jugadores[i])
    if op==1:
        print("Grabar jugador")
        jugador=fn.grabar(jugadores)
    elif op==2:
        if len(jugadores)!=0:
            print("Buscar Participante")
            fn.buscar(jugadores)
        else:
            print("No hay jugadores para mostrar.")
    elif op==3:
        if len(jugadores)!=0:
            print("Imprimir parejas")
            fn.imprimir(jugadores)
        else:
            print("No hay jugadores para mostrar!!")
fn.despedida()