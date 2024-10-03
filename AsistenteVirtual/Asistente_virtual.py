import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idiomas
david_english = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
zira_english = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
elena_spain = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
sabina_mex = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# escuchar nuestro microfono y devolver el audio como texto
def trasformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("ups, no entendi")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"


#  funcion para transformar el texto a voz humana
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', sabina_mex)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el dia de la semana
def pedir_dia():

    # Crear variables con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de los dias de la semana
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'}

    # decir el dia de la semana
    nombre_dia = calendario[dia_semana]
    hablar(f'Hoy es {nombre_dia}')
#pedir_dia()

# Informar que hora es
def pedir_hora():
    # Crear variable con datos de la hora actual
    hora = datetime.datetime.now()
    hora = f'Miguel en este momento la hora es {hora.hour} con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # Pueda decir la hora
    hablar(hora)
#pedir_hora()


# Funcion  saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'{momento} soy sabina la chola mexicana tu asistente personal, Por favor, dime ¿en que te puedo ayudar?')
#saludo_inicial()


# Funcion central del asistente
def pedir_cosas():

    # Activar el saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    while comenzar:
        # Activar el micro y guardar el pedido en un string
        pedido = trasformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('De una!! procedo a abrir youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abrir el navegador' in pedido:
            hablar('Báncame un toque!!')
            webbrowser.open('https://www.google.com')
            continue

        elif 'hora' in pedido:
            pedir_dia()
            pedir_hora()
            continue

        elif 'busca en wiki' in pedido:
            # Eliminar la frase clave del pedido
            pedido = pedido.replace('busca en wiki', '').strip()

            # Verificar lo que se está buscando
            print(f"Buscando en Wikipedia: {pedido}")

            wikipedia.set_lang('es')

            # Realizar la búsqueda
            try:
                resultado = wikipedia.summary(pedido, sentences=1)
                hablar('Wikipedia dice lo siguiente:')
                hablar(resultado)
            except wikipedia.exceptions.DisambiguationError as e:
                hablar("Lo siento, hay varias opciones para esa búsqueda, intenta ser más específico.")
            except wikipedia.exceptions.PageError:
                hablar("No encontré resultados para esa búsqueda.")
            continue

        elif 'busca en internet' in pedido:
            pedido = pedido.replace('busca en internet', '').strip()
            hablar('De una!!')
            pywhatkit.search(pedido)
            hablar('Esto fue lo que encontre para ti')
            continue

        elif 'reproducir' in pedido:
            hablar('Buena idea, ahi voy!!')
            pywhatkit.playonyt(pedido)
            continue

        elif 'pequeña bromilla' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de ')[-1].strip()
            cartera = {
                'apple': 'AAPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }
            try:
                # Convertir la acción a su ticker correspondiente
                accion_buscada = cartera[accion.lower()]

                # Obtener información de la acción
                accion_buscada = yf.Ticker(accion_buscada)

                # Imprimir toda la información para verificar si tiene 'currentPrice'
                info_accion = accion_buscada.info
                print(info_accion)

                # Revisar si la clave 'currentPrice' existe en la información
                if 'currentPrice' in info_accion:
                    precio_actual = info_accion['currentPrice']
                    hablar(f'La encontré, el precio de la {accion} es {precio_actual}')
                else:
                    hablar(f'Lo siento, no pude encontrar el precio actual para {accion}.')
                continue

            except Exception as e:
                print(f"Error: {e}")  # Para diagnosticar el error
                hablar('Perdón, pero no la encontré')
                continue

        elif 'salite chola' in pedido:
            hablar('Me voy a la chingada, cualquier cosa me dices')
            break

pedir_cosas()


# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#     print(voz)

#hablar('hola soy sabrina la españoleta')
#trasformar_audio_en_texto()
