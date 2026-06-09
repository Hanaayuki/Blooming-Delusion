# Confi de la galeria de galiciasss no me peges bella
# te lo documento para que entiendas que hace cada cosa
init python:
    # sistema de galeria
    g = Gallery()

    # Imagen que se muestra si la foto esta bloqueada yo pondre a ineffa y jahoda 
    g.locked_button = "galeria/galeria bloqueada.png"
    
    g.transition = fade

    # volcamos las fotos uwu
    
    g.button("foto_epilogo")
    g.unlock_image("fu fu") # bella le dice amaru di 12 + 1, amaru lo dice, bella en corto mientras mas me la mama mas me crece

    g.button("foto_escena2")
    g.unlock_image("dlagon") # H-O-T-T-O-G-O
    
    g.button("foto_escena3")
    g.unlock_image("tengo hambre") # te dije que ignoraras todo lo que viene después de full traceback
    
    g.button("foto_escena4")
    g.unlock_image("bg ow") # no se que poner aqui pero te cuento algo tenemos a pepe detras de esta puerta: deja que le paso una nota 汉 o me la a respondido jajajajaj la verdad no se que dice 


# me tuve que ver un video de como colacal las fotos pero ya lo entendi aunque tambien me vi cual es la derecha y la izquierda
screen galeria_screen():

    tag menu

    # 
    add "galeria/fondo menu galeria.png"

    #regresar al menú principal
    textbutton _("Volver"):
        xpos 40
        ypos 40
        action Return()

    # contenedor invisible para centrar la cuadricula encima del fondo
    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

# vale entiendo esto bella es importante creo que ya se cual es la derecha y es la que esta encima de la cabeza
            grid 2 2:
                spacing 40
                xalign 0.5
                
              
# Casilla 1 (Arriba Izquierda)
               
                vbox:
                    xalign 0.5
                    spacing 10 # esto es un espacio entre la foto y el texto
                    
                    imagebutton:
                        xalign 0.5
                        idle "galeria/yo y manuel.png"
                        action g.Action("foto_epilogo")
                    
                    # Si la foto esta desbloqueado muestra el tituño si no le hace la de willan afton a los niños
                    if renpy.seen_image("fu fu"):
                        text "El desarrollador y su amante" xalign 0.5 size 22
                    else:
                        text "?????" xalign 0.5 size 22

               
# Casilla 2 (Arriba Derecha)
                
                vbox:
                    xalign 0.5
                    spacing 10
                    
                    imagebutton:
                        xalign 0.5
                        idle "galeria/ow.png"
                        action g.Action("foto_escena2")
                    
                    if renpy.seen_image("dlagon"):
                        text "iris pagame" xalign 0.5 size 22
                    else:
                        text "?????" xalign 0.5 size 22

               
# Casilla 3 (Abajo Izquierda)
               
                vbox:
                    xalign 0.5
                    spacing 10
                    
                    imagebutton:
                        xalign 0.5
                        idle "galeria/fu fu.png"
                        action g.Action("foto_escena3")
                    
                    if renpy.seen_image("tengo hambre"):
                        text "Toy chica era" xalign 0.5 size 22 # la unica animatronica que llevaba shorts
                    else:
                        text "?????" xalign 0.5 size 22

# Casilla 4 (Abajo Derecha)
               
                vbox:
                    xalign 0.5
                    spacing 10
                    
                    imagebutton:
                        xalign 0.5
                        idle "galeria/dlagon.png"
                        action g.Action("foto_escena4")
                    
                    if renpy.seen_image("ow.png"):
                        text "necesito sanación" xalign 0.5 size 22
                    else:
                        text "?????" xalign 0.5 size 22