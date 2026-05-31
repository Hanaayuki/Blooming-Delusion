# Coloca el código de tu juego en este archivo.

#personajes secundarios 
define e = Character("Elion" , color="C20404")
define a = Character("Asher" , color="33FFBA")
define r = Character("Ryan" , color="20009E")
define s = Character("Soren" , color="FFE300")
define y = Character("Ryker" , color="9500D4")

#protagonista
define nj = DynamicCharacter("nombre_jugador" , color="ABABAB")

# El juego comienza aquí.
label start:
    image fondo1= "BG Fondo Habitacion.PNG"
    scene fondo1
    # Nombre provisional para evitar errores en el prólogo
    $ nombre_jugador = "..."

    #PRÓLOGO 

    nj "Abrí los ojos de golpe."

    nj "La respiración me temblaba."

    play music "audio/Fallen Down (Reprise).mp3" fadein 1.0

    nj "Por un momento me quedé completamente quieto/a, mirando el techo de la habitación mientras intentaba entender qué acababa de pasar."

    nj "Otra vez."

    nj "Otra maldita vez."

    nj "Había sido un sueño."

    nj "No… una pesadilla."

    nj "Creo."

    nj "Ni siquiera podía recordarla bien."

    nj "Solo quedaba esa sensación incómoda en el pecho."

    nj "Pesada."

    nj "Fría."

    nj "Como si hubiera olvidado algo importante."

    nj "Como si hubiera estado conteniendo la respiración demasiado tiempo."

    nj "Cerré los ojos un segundo, intentando recuperar alguna imagen, algún sonido, cualquier cosa."

    nj "Nada."

    nj "Todo se deshacía demasiado rápido."

    nj "Suspiré despacio y me incorporé en la cama, apartando las mantas de encima."

    nj "La habitación permanecía en silencio, apenas iluminada por la tenue luz gris que atravesaba las cortinas."

    nj "Por unos segundos no me movi."

    nj "Solo mire el techo, intentando ordenar los restos de algo que ya empezaba a deshacerse en mi cabeza."

    nj "La habitación estaba en silencio."

    nj "Demasiado silencio."

    nj "La luz grisácea que entra entre las cortinas hacía que todo se viera apagado."

    nj "Vacío."

    nj "Me llevé una mano a la cara."

    nj "Últimamente dormía peor."

    nj "O quizá simplemente empezaba a recordar más de lo que debería."

    nj "El sonido suave de la cama hundiéndose rompió el silencio mientras me levantaba."

    nj "El suelo estaba frío."

    nj "Demasiado frío."

    nj "Camine hasta el espejo apoyado cerca de la pared."

    nj "Por un instante me quede observando mi reflejo sin decir nada."

    nj '"...Vaya cara."'

    #PERSonalicion
    "de que color eran mis ojos?"
    menu:
        "Azules":
            $ color_ojos = "azul"
            nj "Las ojeras eran bastante evidentes ya que hacía un contraste con mis ojos color [color_ojos]."
        "Verdes":
            $ color_ojos = "verde"
            nj "Las ojeras eran bastante evidentes ya que hacía un contraste con mis ojos color [color_ojos]."
        "Marrones":
            $ color_ojos = "marrón"
            nj "Las ojeras eran bastante evidentes ya que hacía un contraste con mis ojos color [color_ojos]."
        "Grises":
            $ color_ojos = "gris"
            nj "Las ojeras eran bastante evidentes ya que hacía un contraste con mis ojos color [color_ojos]."
    
    "Mi pelo siempre fue de estre color?"
    menu:
        "Rubio":
            $ color_pelo = "rubio"
            nj "Me acomodé el cabello rubio, que estaba completamente desordenado."
            
        "Castaño":
            $ color_pelo = "castaño"
            nj "Pasé una mano por mi cabello castaño para quitarlo de mi cara."
            
        "Negro":
            $ color_pelo = "negro"
            nj "Mi cabello negro se veía opaco bajo la luz gris."
            
        "Pelirrojo":
            $ color_pelo = "pelirrojo"
            nj "El tono pelirrojo de mi cabello era lo único con color en este lugar."

    #Genero 
    "Pero... ¿qué género tenía?"
    menu:
        "Masculino":
            $ genero = "masculino"
            $ o_a ="o"
            $ o_a_e= "o"
            nj "un chico espero no quedarme calvo"
        "Femenino":
            $ genero = "femenino"
            $ o_a ="a"
            $ o_a_e= "a"
            nj "una chica ojala ser mas alta"
        "No binario":
            $ genero = "no binario"
            $ o_a ="e"
            $ o_a_e= "e"
            nj " me siento azul kris?"


    #Nombre
    $ nombre_jugador = renpy.input("¿Cómo me llamo?", default="mc")
    $ nombre_jugador = nombre_jugador.strip()

    if not nombre_jugador:
        $ nombre_jugador = "mc" 

    nj '"...Bueno, [nombre_jugador]. Sigues viv[o_a]. Supongo que eso ya es algo."'

    nj "Intenté bromear conmigo mism[o_a_e], pero la voz salió más vacía de lo que esperaba."

    nj "Por un instante seguí mirando mi reflejo."

    nj "A veces se sentía extraño."

    nj "Como si estuviera viendo a otra persona."

    stop music fadeout 1.0

    "..."

    "..."

    play sound "audio/Ding.OGG" fadein 1.0
 
    nj "El sonido de una notificación rompió el silencio de la habitación"

    nj "Parpadeé y giré la cabeza hacia el escritorio."
    
    nj "Parpadeé y giré la cabeza hacia el escritorio."

    nj "El portátil seguía encendido."

    nj "Fruncí ligeramente el ceño antes de acercarme."

    nj "No esperaba ningún mensaje"

    nj "Mucho menos uno así."

    "Asunto: Confirmación de acceso a archivos — Orfanato Tsukimi."

#elecion 1 

    menu:
        "Abrir el correo.":
            jump Lee_el_correo
        "Ya lo abriré más tarde.":
            jump No_lee_el_correo

label Lee_el_correo:

    nj "Dudé unos segundos antes de pulsar la notificación."

    nj "La pantalla iluminó ligeramente mi rostro mientras el correo terminaba de cargar."

            
    show correo_orfanato at truecenter

    "Asunto:\nConfirmación de acceso a archivos — Orfanato Tsukimi."

    "..."

    nj "Tragué saliva sin darme cuenta."

    nj "Abrí el mensaje."

    "..."

    hide correo_orfanato

    nj "...Hoy..."

    nj "Miré la hora rápidamente."

    nj "Aún tenía tiempo."

    nj "Aunque no demasiado."

    nj "El estómago se me revolvió ligeramente."

    nj "Después de tantos años..."

    nj "por fin iba a descubrir algo."

    nj "Algo sobre mí."

    nj "Sobre mi infancia."

    nj "Sobre lo que ocurrió realmente."

    "..."

    nj "O eso esperaba."

    nj "Cerré lentamente el portátil y me quedé sentad[o_a] unos segundos al borde de la cama."

    nj "De repente ya no tenía tan claro querer ir."

    nj "Había pasado años intentando no pensar en ello."

    nj "En el orfanato."

    nj "En mis padres."

    nj "En esa parte de mi vida que apenas podía recordar."

    nj "Y ahora..."

    nj "ahora estaba a punto de abrir una puerta que quizá nunca debió abrirse."

    nj "Me levanté lentamente y tomé la chaqueta que descansaba sobre la silla del escritorio."

    nj "Las manos me temblaban un poco."

    nj "No sabía si era miedo o ansiedad."

    nj "Quizá ambas."

    nj "Antes de salir lancé una última mirada a la habitación."

    nj "Vacía."

    nj "Silenciosa."

    nj "Fría."

    "..."

    nj "Cerré la puerta tras de mí."

    scene black with fade
   
    image fondo2 = "BG Ciudad.PNG"
    scene fondo2
    nj "El cielo estaba cubierto."

    nj "La ciudad parecía extrañamente apagada bajo la luz grisácea de la tarde."

    nj "Las personas caminaban a mi alrededor sin mirarme siquiera."

    nj "Como si yo no existiera realmente."

    nj "Metí las manos en los bolsillos mientras seguía avanzando."

    nj "Cada paso hacia el orfanato hacía que el pecho me pesara más."

    nj "Intentaba recordar algo."

    nj "Cualquier cosa."

    nj "Una voz."

    nj "Un rostro."

    nj "Un nombre."

    nj "Pero mi cabeza seguía sintiéndose vacía."

    nj "Rota."

    "..."

    nj "Entonces lo vi."

    scene black with fade 
    show text "orfanato tsukimi" at truecenter
    pause 
    hide text
    image fondo3 = "BG orfanato.JPG"
    scene fondo3

    
    nj "El edificio parecía más pequeño de lo que imaginaba."

    nj "Viejo."

    nj "Silencioso."

    nj "Casi abandonado."

    nj "Me detuve unos segundos frente a la entrada."

    nj "El pecho me dolía."

    nj "Como si mi cuerpo estuviera intentando decirme que me fuera."

    nj "Pero ya había llegado demasiado lejos para echarme atrás."


    play sound "audio/puerta_abrir.MP3" 

    nj "Empujé lentamente la puerta."


 image fondo4 = "BG orfanato dentro.JPG"
 scene fondo4 











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

   "~ Horas después ~"

   nj "La tenue luz grisácea había desaparecido hacía rato."

   nj "Parpadeé lentamente al escuchar vibrar el móvil sobre el escritorio."

   nj "Fruncí el ceño."

   nj "¿Cuánto tiempo había pasado?"

   nj "Me incorporé confundid[o_a] y tomé el teléfono."

   "18:07"

   "..."

   nj "El cuerpo se me tensó."

   nj '"No..."'

   nj "Abrí rápidamente el portátil."

   nj "La pantalla iluminó la habitación oscura mientras buscaba el correo."

   show correo_orfanato at truecenter

   "Asunto:\nConfirmación de acceso a archivos — Orfanato Tsukimi."

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
         scene black with Fade(0.1, 0.0, 0.5, color="#000000")

         "Una luz blanca atravesó mi visión."
         "Y entonces todo desaparece."

         window hide 
         show text "FIN DEL PROLOGO"
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
         nj "Y aunque intentara ignorarla..."
         nj "nunca desaparecía del todo."

         
         scene black with fade
         "━━━━━━━━━━━\nFINAL ALCANZADO\n━━━━━━━━━━━"
         '"{i}Lo que nunca se busca…\nnunca llega a encontrarse.{/i}"'
         return

