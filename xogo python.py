nombre = input ("Antes de empezar, dime tu nombre ")
print ("Hola", nombre, "te doy la bienvenida al juego")
while True:
    personaje= input ("Elige una de entre estas mujeres: \n A) Hedy Lammar \n B) Ángela Ruiz Robles \n C) Roberta Williams \
           \nSelecciona A, B o C: ")
    if personaje == "A" or personaje == "a":
        print ("Has seleccionado a Hedy Lammar (1914-2000): Inventora de la red wifi. Fue una actriz y estudió ingeniería.\nDesde pequeña fue considerada por sus profesores como una mujer superdotada.")
        break
    elif personaje == "C" or personaje == "c":
        print ("Has seleccionado a Roberta Williams (1953- ): Creadora de videojuegos y escritora. Diseñó aventuras gráficas\
similares a esta desde el punto de vista lógico y este es mi homenaje personal hacia su trabajo.")
        break
    else:
        print ("Aquí comienza el verdadero juego. ¿Estás preparado?")
    if personaje != "a" and personaje != "b" and personaje !="c":
        print ("Esta respuesta no existe")
        continue
    print ("Ángela Ruiz Robles llegó en 1918 a Ferrol tras obtener su plaza como maestra en Santa Eugenia de Mandiá")
    decide= input ("Si tú fueses Ángela, ¿Qué hubieses hecho al llegar allí?: Divertirse o Enseñar  ")
    decide= decide.upper()
    if decide == "DIVERTIRSE":
        print ("Para llegar lejos, Ángela tuvo que estudiar y su mayor deseo era ser una gran maestra")
        x=input ("Pulse intro para salir")
    elif decide== "ENSEÑAR":
        print ("Este es el camino correcto para llegar a ser inventora")
        print ("Llegados a este punto de la historia, interesa saber cuál ha sido la profesión que desempeñó descubriendo este códigos ocultos en ASCII:")
    for i in range (3):
        print("A) 01100001 01100011 01110100 01110010 01101001 01111010")
        print ("B) 01101001 01101110 01100111 01100101 01101110 01101001 01100101 01110010 01100001")
        print ("C) 01101101 01100001 01100101 01110011 01110100 01110010 01100001")
        decide = input ("Indica A, B o C: ")
        if decide== "C" or decide =="c":
            print ("Correcto")
            break
        else:
            print ("Incorrecto")

