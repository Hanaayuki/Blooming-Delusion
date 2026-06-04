# Coloca el código de tu juego en este archivo.

#pronombres
init python:
    def set_genero(g):
        global genero, el, El, ele, Ele, term
        genero = g
        if g == "masculino":
            el, El, ele, Ele, term = "él", "Él", "el", "El", "o"
        elif g == "femenino":
            el, El, ele, Ele, term = "ella", "Ella", "la", "La", "a"
        elif g == "no binario":
            el, El, ele, Ele, term = "elle", "Elle", "le", "Le", "e"

#personajes secundarios 
define el = Character("Elion" , color="C20404")
define ah = Character("Asher" , color="33FFBA")
define r = Character("Ryan" , color="20009E")
define so = Character("Soren" , color="FFE300")
define yk = Character("Ryker" , color="9500D4")

define qn = Character("¿?")

define re = Character("Recepcionista")
define di = Character("Director")
#narrador es empanadas
define narrator = Character(None, window_background=Frame("gui/cuadro_texto_protagonista.PNG", 0, 0, xalign=0.5, yalign=1.0))

define n = Character(None, kind=nvl)

#protagonista
define nj = DynamicCharacter("nombre_jugador" , color="ABABAB", window_background=Frame("gui/cuadro_texto_protagonista.PNG", 0, 0, xalign=0.5, yalign=1.0))

#fondos y imagenes
image fondo habitacion= "BG Fondo Habitacion.PNG"
image fondo ciudad = "BG Ciudad.PNG"
image fondo orfanato = "BG orfanato.JPG"
image fondo orfanato dentro = "BG orfanato dentro.jpg"
image Elion = "Elion.png"
image Asher = "Asher.png"
image Ryan = "Ryan.png"
image Soren = "Soren.png"
image Ryker = "Ryker.png"
image Recepcionista = "Recepcionista.png"
image Director = "Director.png"

#Cuadro de textos personalizado



# El juego comienza aquí.

label start:
    $ renpy.music.stop(channel='music', fadeout=1.5)
    scene fondo habitacion
    # Nombre provisional para evitar errores en el prólogo
    $ nombre_jugador = "..."

    #PRÓLOGO 

    "Abrí los ojos de golpe."

    "La respiración me temblaba."

    play music "audio/Fallen Down (Reprise).mp3" fadein 1.0

    "Por un momento me quedé inmóvil, mirando el techo de la habitación mientras intentaba entender qué acababa de pasar."

    "Otra vez."

    "Otra maldita vez."

    "Había sido un sueño."

    "No… una pesadilla."

    "Creo."

    "Ni siquiera podía recordarla bien."

    "Solo quedaba esa sensación incómoda en el pecho."

    "Pesada."

    "Fría."

    "Como si hubiera olvidado algo importante."

    "Como si hubiera estado conteniendo la respiración demasiado tiempo."

    "Cerré los ojos un segundo, intentando recuperar alguna imagen,{w=0.2} algún sonido,{w=0.1} cualquier cosa."

    "Nada."

    "Todo se deshacía demasiado rápido."

    "Suspiré despacio y me incorporé en la cama, apartando las mantas de encima."

    "La habitación permanecía en silencio, apenas iluminada por la tenue luz gris que atravesaba las cortinas."

    "Por unos segundos no me movi."

    "Solo mire el techo, intentando ordenar los restos de algo que ya empezaba a deshacerse en mi cabeza."

    "La habitación estaba en silencio."

    "Demasiado silencio."

    "La luz grisácea que entra entre las cortinas hacía que todo se viera apagado."

    "Vacío."

    "Me llevé una mano a la cara."

    "Últimamente dormía peor."

    "O quizá simplemente empezaba a recordar más de lo que debería."

    "El sonido suave de la cama hundiéndose rompió el silencio mientras me levantaba."

    "El suelo estaba frío."

    "Demasiado frío."

    "Camine hasta el espejo apoyado cerca de la pared."

    "Por un instante me quede observando mi reflejo sin decir nada."

    nj "\"...Vaya cara.\""

    #PERSONA5licion

    "Las ojeras eran bastante evidentes ya que hacía un contraste con mis ojos... "

    menu:
        "Azules":
            $ color_ojos = "azules"
        "Verdes":
            $ color_ojos = "verdes"
        "Marrones":
            $ color_ojos = "marrones"
        "Grises":
            $ color_ojos = "grises"

    extend "[color_ojos]."
    
    "Mi pelo... "

    menu:
        "Rubio":
            $ color_pelo = "rubio"
            extend "Me acomodé el cabello rubio, que estaba completamente desordenado."
            
        "Castaño":
            $ color_pelo = "castaño"
            extend "Pasé una mano por mi cabello castaño para quitarlo de mi cara."
            
        "Negro":
            $ color_pelo = "negro"
            extend "Mi cabello negro se veía opaco bajo la luz gris."
        
        "Pelirrojo":
            $ color_pelo = "pelirrojo"
            extend "El tono pelirrojo de mi cabello era lo único con color en este lugar."

    #Genero 
    "Me apoyé en el mueble a un lado, sin querer tirando mi ID."
    "Lo tomé, y leí por encima mis datos, como si fueran los de alguien más."

    menu:
        "Masculino":
            $ set_genero("masculino")
        "Femenino":
            $ set_genero("femenino")
        "No binario":
            $ set_genero("no binario")

    #Nombre
    $ nombre_jugador = renpy.input("¿Cómo me llamo?", default="MC")
    $ nombre_jugador = nombre_jugador.strip()

    if not nombre_jugador:
        $ nombre_jugador = "MC" 

    nj "...Bueno, [nombre_jugador]. Sigues viv[term]. Supongo que eso ya es algo."

    "Intenté bromear conmigo mism[term], pero la voz salió más vacía de lo que esperaba."

    stop music fadeout 3.0

    "Por un instante seguí mirando mi reflejo."

    "A veces se sentía extrañ[term]."

    "Como si estuviera viendo a otra persona."

    "..."

    "..."

    play sound "audio/Ding.OGG" fadein 1.0
    "*ding*"

    play sound "audio/Ding.OGG" fadein 1.0
    "*ding*"

    "El sonido de una notificación rompió el silencio de la habitación"

    "Parpadeé y giré la cabeza hacia el escritorio."

    "El portátil seguía encendido."

    "Fruncí ligeramente el ceño antes de acercarme."

    "No esperaba ningún mensaje"

    "Mucho menos uno así."

    "Asunto:" 
    extend "\nConfirmación de acceso a archivos — Orfanato Tsukimi."

    menu:
        "Abrir el correo.":
            jump Lee_el_correo
        "Ya lo abriré más tarde.":
            jump No_lee_el_correo

label Lee_el_correo:

    "Dudé unos segundos antes de pulsar la notificación."

    "La pantalla iluminó ligeramente mi rostro mientras el correo terminaba de cargar."

    "Asunto:" 
    extend "\nConfirmación de acceso a archivos — Orfanato Tsukimi."

    "..."

    nj "Tragué saliva sin darme cuenta."

    nj "Abrí el mensaje."

    show correo_orfanato at truecenter
    pause

    "..."

    hide correo_orfanato

    nj "...Hoy..."

    "Miré la hora rápidamente."

    "Aún tenía tiempo."

    "Aunque no demasiado."

    "El estómago se me revolvió ligeramente."

    "Después de tantos años... {w}por fin iba a descubrir algo."

    "Algo sobre mí."

    "Sobre mi infancia."

    "Sobre lo que ocurrió realmente."

    "..."

    "O eso esperaba."

    "Cerré lentamente el portátil y me quedé sentad[term] unos segundos al borde de la cama."

    "De repente ya no tenía tan claro querer ir."

    "Había pasado años intentando no pensar en ello."

    "En el orfanato."

    "En mis padres."

    "En esa parte de mi vida que apenas podía recordar."

    "Y ahora... {w}ahora estaba a punto de abrir una puerta que quizá nunca debió abrirse."

    "Me levanté lentamente y tomé la chaqueta que descansaba sobre la silla del escritorio."

    "Las manos me temblaban un poco."

    "No sabía si era miedo o ansiedad."

    "Quizá ambas."

    "Antes de salir lancé una última mirada a la habitación."

    "Vacía."

    "Silenciosa."

    "Y fría."

    "..."

    "Cerré la puerta tras de mí."

    scene fondo ciudad with fade

    "El cielo estaba cubierto."

    "La ciudad parecía extrañamente apagada bajo la luz grisácea de la tarde."

    "Las personas caminaban a mi alrededor sin mirarme siquiera."

    "Como si yo no existiera realmente."

    "Metí las manos en los bolsillos mientras seguía avanzando."

    "Cada paso hacia el orfanato hacía que el pecho me pesara más."

    "Intentaba recordar algo."

    "Cualquier cosa."

    "Una voz."

    "Un rostro."

    "Un nombre."

    "Pero mi cabeza seguía sintiéndose vacía."

    "Rota."

    "..."

    "Entonces lo vi."

    scene fondo orfanato with fade 
    show text "{color="#00000"}Orfanato Tsukimi{/color}" at truecenter
    pause 1.0
    hide text

    
    "El edificio parecía más pequeño de lo que imaginaba."

    "Viejo."

    "Silencioso."

    "Casi abandonado."

    "Me detuve unos segundos frente a la entrada."

    "El pecho me dolía."

    "Como si mi cuerpo estuviera intentando decirme que me fuera."

    "Pero ya había llegado demasiado lejos para echarme atrás."


    play sound "audio/puerta_abrir.MP3" 

    "Empujé lentamente la puerta."

    scene fondo orfanato dentro with fade

    "El ambiente olía a papel viejo y madera húmeda."
   
    "Una mujer detrás del mostrador levantó ligeramente la mirada al verme entrar."
  
    re "...¿[nombre_jugador]?"

    "Asentí lentamente"

    "La mujer sonrió de manera educada, aunque había algo extraño en su expresión."

    "Como si me reconociera."

    re "Estábamos esperándote."
    show Recepcionista at left with fade
    "No supe por qué esa frase me hizo sentir incómod[term]."

    "La mujer me pidió que la siguiera por uno de los pasillos."

    "El sonido de mis pasos resonaba demasiado fuerte."

    "Las paredes estaban cubiertas de fotografías antiguas."

    "Niños."

    "Empleados."

    "Habitaciones."

    "Intenté mirar rápido, pero algo dentro de mí seguía sintiéndose extraño."

    "Familiar."

    "..."

    "Entonces me detuve."

    "Una fotografía."

    "Vieja."

    "Gastada."

    "Mis ojos se quedaron clavados en ella."

    "Un grupo de niños sonriendo frente al edificio."

    "Y entre ellos-"

    "..."

    "Mi respiración se cortó."

    "Ese era yo."

    "Mucho más pequeñ[term]"

    "Pero no estaba sol[term]."

    "Había alguien más a mi lado."

    "Alguien cuya cara había sido arrancada de la fotografía."

    "Aparté lentamente la mirada."

    "La sensación incómoda seguía clavada en mi pecho."

    re "...¿Ocurre algo?"
    show Recepcionista at left with fade
    "La voz de la recepcionista me hizo reaccionar"

    "Negué rápidamente con la cabeza."

    nj "No... nada."

    "Aunque claramente no era verdad."

    "La mujer observó unos segundos más antes de continuar caminando por el pasillo."

    "La seguí en silencio."

    "Intentando ignorar esa horrible sensación creciendo dentro de mí."

    "Finalmente nos detuvimos frente a una puerta de madera oscura."

    "La recepcionista llamó suavemente dos veces antes de abrir."

    re "Director, [nombre_jugador] ya ha llegado."
    show Recepcionista at left with fade
    "El despacho era pequeño."

    "Demasiado ordenado."

    "El olor a papel viejo seguía impregnándolo todo."

    "Un hombre mayor levantó la mirada desde unos documentos al verme entrar."

    "Por un instante pareció sorprendido."

    "Solo un segundo."

    "Después sonrió suavemente."

    di "…Así que eres tú."
    show Director at right with fade
    "No supe por qué esas palabras me incomodaron tanto."

    "El director señaló la silla frente al escritorio."

    di "Siéntate, por favor."
    show Director at left with fade   
    "Obedecí lentamente mientras la recepcionista cerraba la puerta detrás de mí."

    "El sonido hizo que el ambiente se sintiera todavía más encerrado."

    "El director abrió uno de los cajones del escritorio y sacó una carpeta bastante gruesa."

    "Vieja."

    "Gastada por el tiempo."

    "Mi estómago se tensó al verla."

    di "…Estos son los registros que conservamos sobre ti."
    show Director at left with fade
    "La colocó frente a mí lentamente."

    "Por un momento dudé antes de abrirla."

    "Pero ya había llegado demasiado lejos para echarme atrás."

    "Abrí la carpeta."

    "Lo primero que vi fue una hoja con varias fotografías mías."

    "Fotos antiguas."

    "Demasiado antiguas."

    window hide
    nvl clear
    nvl show

    n "Nombre: {w}[nombre_jugador]."
    n "Edad al ingresar: {w}7 años."
    n "Fecha de nacimiento: {w}28/05/XX."
    n "Altura: {w}1,25 cm"
    n "Descripción física:"
    n "— Cabello [color_pelo]."
    n "— Ojos [color_ojos]."
    n "Estado de ingreso:"
    n "— Encontrad[term] sol[term] durante la madrugada del 12 de noviembre del 20XX."
    n "— Sin familiares localizados."
    n "— Estado emocional inestable."
    n "— Dificultad para recordar información previa al incidente."
    
    nvl hide
    nvl clear
    window show

    "Mi respiración se volvió más pesada."

    "Pasé lentamente a la siguiente hoja."

    "Un informe policial."

    "El papel estaba ligeramente amarillento."

    window hide
    nvl clear
    nvl show

    n "Reporte policial — Caso 2471"
    n "Menor encontrad[term] cerca de la carretera nacional junto a los restos del accidente registrado la noche del 11 de noviembre."
    n "No se encontraron adultos con vida en la escena."
    n "[Ele] menor presentaba heridas leves y un evidente estado de shock."
    n "Durante el interrogatorio inicial, [ele] menor fue incapaz de proporcionar información coherente sobre lo ocurrido o sobre sus familiares."
    n "Posteriormente fue trasladad[term] al Orfanato Tsukimi bajo custodia temporal."

    nvl hide
    nvl clear
    window show

    "Por último pase a la última documentación  que era la mas gastada y la menos legible  la información psiquiátrica "

    window hide
    nvl clear
    nvl show

    n "Registro psicológico inicial — Archivo parcial"
    n "Paciente: {w}[nombre_jugador]."
    n "Edad al ingreso: {w}7 años."
    n "Estado observado al llegar:"
    n "— [Ele] menor presentaba signos evidentes de shock y desorientación."
    n "— Durante las primeras entrevistas mostró dificultades para responder preguntas relacionadas con identidad, entorno familiar y recuerdos previos al incidente."
    n "— Se recomienda evitar insistir en la recuperación inmediata de memoria debido al estado emocional actual."
    nvl clear

    n "Observaciones iniciales:"
    n "— Escasa interacción con otros menores."
    n "— Episodios frecuentes de ansiedad nocturna."
    n "— Reacción negativa ante separaciones prolongadas del personal."
    n "— Dificultad para permanecer solo/a durante largos periodos de tiempo."
    n "━━━━━━━━━━━"
    n "Nota adicional:"
    n "[Ele] menor parece reaccionar favorablemente cuando recibe atención constante o validación emocional."
    n "Se recomienda supervisión continua durante las próximas semanas."

    nvl hide
    nvl clear
    window show

    "No hay más páginas..."
     
    "Mis manos empezaron a temblar ligeramente."

    nj "No recuerdo nada de esto…"

    "La voz salió apenas en un susurro."

    "El director permaneció en silencio unos segundos."

    "Como si estuviera decidiendo cuánto debía decirme realmente."

    "Entonces habló."

    di "…Eso es normal."

    "Levanté lentamente la mirada."

    "El hombre suspiró suavemente antes de continuar."

    di "El trauma puede hacer que la mente entierre ciertas cosas."

    "..."

    di "…Aunque hay algo extraño."

    "El ambiente se volvió todavía más pesado."

    di "Tus archivos están incompletos."

    "Sentí un escalofrío recorrerme la espalda."

    nj "Incompletos… ¿cómo?"

    "El director frunció ligeramente el ceño."

    di "Faltan documentos."

    "..."

    di "Y no sabemos quién los retiró."

    "..."

    "El silencio que siguió fue insoportable."

    "Sentía el corazón golpeándome demasiado fuerte contra el pecho."

    nj "No…"

    "Bajé rápidamente la mirada hacia los documentos otra vez."

    "Las fotografías."

    "El informe."

    "La fecha."

    "Todo parecía borroso de repente."

    "Como si mi cabeza estuviera dejando de procesarlo correctamente."

    nj "Eso no tiene sentido…"

    "Mis manos temblaban."

    "Intenté seguir leyendo, pero las letras empezaban a mezclarse frente a mis ojos."

    "Entonces ocurrió."

    "Una imagen atravesó mi mente de golpe."

    "Una carretera oscura."

    "Lluvia."

    "Alguien sujetándome la mano."

    "Y una voz—"

    qn "Corre."

    "Me levanté tan rápido que la silla chocó contra el suelo."

    "La respiración empezó a romperse."

    "El director se incorporó inmediatamente."

    di "¿[nombre_jugador]?"

    nj "No..."

    "Me llevé ambas manos a la cabeza."

    "Dolía."

    "Dolía demasiado."

    "Más imágenes aparecieron de golpe."

    "Luces."

    "Sangre."

    "El sonido metálico de algo rompiéndose."

    "Una figura borrosa."

    "Y alguien llorando."

    nj "Necesito salir…"

    "La voz apenas parecía mía."

    "El director intentó acercarse."

    di "Espera, tranquilízate—"

    nj "¡No me toque!"

    "Retrocedí casi automáticamente."

    "La habitación empezó a sentirse demasiado pequeña."

    "Demasiado cerrada."

    "No podía respirar."

    "Necesitaba salir."

    "Ahora."

    "Sin pensar demasiado agarré mi chaqueta y salí del despacho apresuradamente."

    "Escuché al director decir algo detrás de mí, pero ya no podía entenderlo."

    "Todo sonaba lejano."

    "Distorsionado."

    "Atravesé el pasillo casi corriendo."

    "Las fotografías de las paredes parecían observarme mientras pasaba."

    "Mi respiración se quebraba más con cada paso."

    nj "No recuerdo…"

    "La voz me tembló horriblemente."

    nj "No recuerdo nada…"

    "Empujé la puerta principal del orfanato y salí al exterior."

    "El aire frío golpeó mi rostro de inmediato."

    "Pero no ayudó."

    "Nada ayudaba."

    "Las imágenes seguían apareciendo."

    "Fragmentos."

    "Pedazos rotos de algo que mi mente llevaba años intentando esconder."

    "Seguí avanzando sin mirar realmente hacia dónde iba."

    "Demasiado rápido."

    "Demasiado ruido."

    "Las luces de la calle se mezclaban frente a mis ojos."

    "Entonces—"

    "*Sonido de claxon*"

    "Giré la cabeza demasiado tarde."

    "Una luz blanca atravesó mi visión."

    "El cuerpo se me congeló por completo."

    "Y entonces—"

    play sound "audio/Camion Chocar Sonido.MP3" 

    "..."

    "..."

    show text "FIN DEL PROLOGO" at truecenter
    pause 3.0

    return

label No_lee_el_correo:

    nj "Desvié la mirada de la pantalla."

    nj '"...Luego."'

    nj "No tenía ganas de lidiar con eso ahora mismo."

    nj "Cerré los portátil sin siquiera abrir el mensaje."

    nj "El sonido seco de la tapa resonó ligeramente en la habitación."

    nj "Demasiado fuerte."

    nj "Suspiré y me dejé caer nuevamente sobre la cama."

    nj "Intentando ignorar esa sensación incómoda en el pecho."

    nj "Como si algo estuviera esperando."

    "..."

    "..."

    show text "~ Horas después ~" at truecenter
    pause 3.0
    hide text

    nj "La tenue luz grisácea había desaparecido hacía rato."

    nj "Parpadeé lentamente al escuchar vibrar el móvil sobre el escritorio."

    nj "Fruncí el ceño."

    nj "¿Cuánto tiempo había pasado?"

    nj "Me incorporé confundid[term] y tomé el teléfono."

    "18:07"

    "..."

    nj "El cuerpo se me tensó."

    nj '"No..."'

    nj "Abrí rápidamente el portátil."

    nj "La pantalla iluminó la habitación oscura mientras buscaba el correo."

    show correo_orfanato at truecenter

    "Asunto:"

    "Confirmación de acceso a archivos — Orfanato Tsukimi."

    nj "Lo abrí de golpe."

    "Su cita ha sido programada para hoy, 17 de noviembre, a las 16:30."

    "..."

    hide correo_orfanato

    nj '"...Mierda."'

    nj "Sentí un vacío horrible en el estómago."
   
    menu:
        "Todavía puedo llegar.":
            nj "Apenas eran las seis pasadas. Si corría, si inventaba una excusa, si les suplicaba..."
            nj "Quizá aún quedara alguien allí. No podía perder esta oportunidad."
            nj "La desesperación me nubló el juicio."
            
            nj "Tomé lo primero que encontré y salí del apartamento casi corriendo."
            nj "Los pensamientos se atropellaban en mi cabeza mientras bajaba las escaleras."
            nj "Demasiado rápido."
            nj "Demasiado ruido."
            nj "La respiración empezaba a temblarme otra vez."
            nj "Necesitaba llegar."
            nj "Necesitaba saber."
            nj "Necesitaba—"

            play sound "audio/Camion Chocar Sonido.MP3" 
            scene black with fade

            "Una luz blanca atravesó mi visión."
            "Y entonces todo desaparece."

            show text "FIN DEL PROLOGO" at truecenter
            pause 3.0
            return 

        "…Ya es demasiado tarde.":
            nj "Me quedé mirando la pantalla en silencio."
            "18:07."
            nj "La cita había terminado hacía más de una hora."
            "..."
            nj "Poco a poco dejé caer el portátil sobre el escritorio."
            nj '"...Da igual."'
            nj "La voz salió vacía."
            nj "Como si realmente ya no importara."
            nj "Volví a sentarme en la cama mientras la habitación quedaba nuevamente en silencio."
            nj "El correo seguía abierto frente a mí."
            nj "Esperando."
            nj "Como si quisiera decir algo más."
            nj "Pero no lo hacía."
            nj "Y yo tampoco tenía fuerzas para insistir."
            "..."
            nj "Quizá nunca debí pedir aquella cita."
            nj "Quizá remover el pasado solo iba a empeorar las cosas."
            nj "Me tumbé lentamente, mirando el techo una vez más."
            nj "La misma sensación vacía seguía ahí."
            nj "Pesada."
            nj "Fría."
            nj "Y aunque intentara ignorarla... {w}nunca desaparecía del todo."
            scene black with fade

            show text "━━━━━━━━━━━\nFINAL ALCANZADO\n━━━━━━━━━━━" at truecenter

            pause 2.0
            
            show text "{i}Lo que nunca se busca…\nnunca llega a encontrarse.{/i}" at truecenter
            
            pause

            return


