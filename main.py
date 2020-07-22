import pygame

# Se definen el NEGRO y el BLANCO.
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)

pygame.init()

# Se definen las dimensiones de la pantalla.
dimensiones = [700,500]

# Se define la pantalla con los parametros previamente definidos.
pantalla = pygame.display.set_mode(dimensiones)

# Se define el titulo de la vnetana de la pantalla.
pygame.display.set_caption('GRAVEDAD CON REBOTE VERTICAL Y ORIZONTEAL')

# Estado del boton de cierre del bucle principal.
hecho = False

# Se define la gravedad que afectara a los objetos
# esta esta multiplicada por la escala en pixeles.
gravedad = 6.674 * 10

# Se define el tamaño de la bola.
tamaño = 15

# Se define el grosor de la bola, este no puede se mayor que el tamaño.
grosor = 15

# Se definen la altura de los objetos. Posicion inicial igual a 50px.
posicion_y = 50

# Se definen la  de los objetos. Posicion inicial igual a 150px.
posicion_x = 150

# Se define la inercia inicial que ba a tener el objeto tanato vertical como horizontalmente.
inercia = [0, 14]

# Se define la masa que ba a tener el objeto.
masa = 50

# Se define los eventos del bucle principal.
event = pygame.event.wait()


# Se define la cantidad de fotogramas por segundo.
reloj = pygame.time.Clock()

# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ


    # XXXXXXXXX GRAVEDAD CON REBOTE VERTICAL Y HORIZONTAL. XXXXXXXXX

    # Aumento de la inercia del objeto. Afectado por la fuerza de la gravedad.
    if inercia[0] < gravedad:
        inercia[0] += (gravedad / masa)

    # Si el objeto se encuentra antes del borde inferior de la pantalla, se agrega la inercia vertical a su altura.
    if posicion_y < (dimensiones[1] - tamaño):
        posicion_y += round(inercia[0])

    #Si el objeto se encuntra mas abajo o en el mismo lugar del borde inferior de la pantallla...
    elif posicion_y >= (dimensiones[1] - tamaño):

        # Si la inercdia vertical del objeto es mayor a 0, esta se multiplica por -1,
        # se le agrega un quinto de la masa del objeto y se lleva al borde de la pantalla.
        if round(inercia[0]) > 0:
            inercia[0] *= -1
            inercia[0] += masa / 5
            posicion_y = (dimensiones[1] - tamaño)

        # Si la inercia vertical del objeto es menor a 0, se le agrega la inercia vertical a la altura.
        if inercia[0] < 0:
            posicion_y += round(inercia[0])

    # Si el objeto se pasa del borde inferior de la pantalla, es llevado de vuelta a este.
    if posicion_y > (dimensiones[1] - tamaño):
        posicion_y = (dimensiones[1] - tamaño)

    #Si el objeto se encuntra mas abajo o en el mismo lugar del borde superior de la pantallla...
    if posicion_y <= tamaño:

        # Si la inercdia vertical del objeto es menor a 0, esta se multiplica por -1,
        # se le agrega un decimo de la masa del objeto y se lleva al borde de la pantalla.
        if round(inercia[0]) < 0:
            inercia[0] *= -1
            inercia[0] += masa / 10
            posicion_y = tamaño

        # Si la inercia vertical del objeto es mayor a 0, se le agrega la inercia vertical a la altura.
        if inercia[0] > 0:
            posicion_y += round(inercia[0])

    # Si el objeto esta dentro de los bordes laterales se le agrega a su posicion horizontal su
    # inercia Horizontal.
    if posicion_x < (dimensiones[0] - tamaño) and posicion_x > 0:
        posicion_x += round(inercia[1])

    #Si el objeto se encuntra mas alla o en el mismo lugar del borde derecho de la pantallla...
    elif posicion_x >= (dimensiones[0] - tamaño):

        # Si la inercia horizontal del objeto es menor a 0, se le agrega la inercia horizontal
        # a la posicion horizontal.
        if inercia[1] < 0:
            posicion_x += round(inercia[1])

        # Si la inercdia horizontal del objeto es mayor a 0, esta se multiplica por -1,
        # se le agrega un decimo de la masa del objeto y se lleva al borde de la pantalla.
        if round(inercia[1]) > 0:
            inercia[1] *= -1
            inercia[1] += masa / 10
            posicion_x = (dimensiones[0] - tamaño)

    #Si el objeto se encuntra mas alla o en el mismo lugar del borde izquierdo de la pantallla...
    if posicion_x <= tamaño:

        # Si la inercia horizontal del objeto es menor a 0, se le agrega la inercia horizontal
        # a la posicion horizontal.
        if inercia[1] > 0:
            posicion_x += round(inercia[1])

        # Si la inercdia horizontal del objeto es mayor a 0, esta se multiplica por -1,
        # se le agrega un decimo de la masa del objeto y se lleva al borde de la pantalla.
        if round(inercia[1]) < 0:
            inercia[1] *= -1
            inercia[1] -= masa / 10
            posicion_x = tamaño


    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(BLANCO)

    # A continuacion se dibuja el obeto.
    pygame.draw.circle(pantalla, NEGRO, (posicion_x, posicion_y), tamaño, grosor)


    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo.
    reloj.tick(100)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
