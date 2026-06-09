# Confi de la galeria de galiciasss no me peges bella
# te lo documento para que entiendas que hace cada cosa
init python:
    # sistema de galeria
    g = Gallery()

    # Imagen que se muestra si la foto esta bloqueada yo pondre a ineffa y jahoda 
    g.locked_button = "galeria/foto bloqueada.png"
    
    g.transition = fade

    # volcamos las fotos uwu
    g.button("foto_epilogo")
    g.unlock_image("Correo_orfanato") # bella le dice amaru di 12 + 1, amaru lo dice, bella en corto mientras mas me la mama mas me crece

    g.button("foto_escena2")
    g.unlock_image("dlagon") # H-O-T-T-O-G-O
    
    g.button("foto_escena3")
    g.unlock_image("tengo hambre") # te dije que ignoraras todo lo que viene después de full traceback
    
    g.button("foto_escena4")
    g.unlock_image("bg ow") # no se que poner aqui pero te cuento algo tenemos a pepe detras de esta puerta: deja que le paso una nota 汉 o me la a respondido jajajaj la verdad no se que dice 


# me tuve que ver un video de como colacal las fotos pero ya lo entendi aunque tambien me vi cual es la derecha y la izquierda
screen galeria_screen():

    tag menu

    # fondo de la galeria 
    add "galeria/fondo menu galeria.png"

    # regresar al menú principal
    textbutton _("Volver"):
        xpos 40
        ypos 40
        action Return()

    # Usamos un frame con tamaño fijo para que no se muevan del centro
    frame:
        background None
        xalign 0.5
        yalign 0.5
        
        # vpgrid ayuda a que no se solapen y permite scroll si pones mas fotos
        vpgrid:
            cols 2
            spacing 40
            draggable True
            mousewheel True
            
            # Casilla 1
            vbox:
                imagebutton:
                    idle g.make_button("foto_epilogo", "galeria/correo_orfanato.png")
                    xysize (400, 400) # Tamaño uniforme para todas
                    action g.Action("foto_epilogo")
                # Si la foto esta desbloqueado muestra el tituño si no le hace la de willan afton a los niños
                text ("Correo del orfanato" if renpy.seen_image("Correo_orfanato") else "?????") size 22 xalign 0.5

            # Casilla 2
            vbox:
                imagebutton:
                    idle g.make_button("foto_escena2", "galeria/ow.png")
                    xysize (400, 400)
                    action g.Action("foto_escena2")
                text ("iris pagame" if renpy.seen_image("dlagon") else "?????") size 22 xalign 0.5

            # Casilla 3
            vbox:
                imagebutton:
                    idle g.make_button("foto_escena3", "galeria/fu-fu.png")
                    xysize (400, 400)
                    action g.Action("foto_escena3")
                text ("Toy chica era" if renpy.seen_image("tengo hambre") else "?????") size 22 xalign 0.5

            # Casilla 4
            vbox:
                imagebutton:
                    idle g.make_button("foto_escena4", "galeria/dlagon.png")
                    xysize (400, 400)
                    action g.Action("foto_escena4")
                text ("necesito sanación" if renpy.seen_image("bg ow") else "?????") size 22 xalign 0.5
# vale bella weona lo que acabo de haqcer aqui es limitar el tamaño de la fotos para que una no se sobreponga a la otra  
# la cosa es que estaria bien que todas esten en el mismo tamaño a la hora de crearla