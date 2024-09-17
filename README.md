Asistente Virtual con Python

Este proyecto es un asistente virtual de voz desarrollado en Python, capaz de escuchar comandos de voz, procesar información, y responder con texto y audio. Puede realizar diversas tareas como abrir sitios web, decir la hora, el día, buscar en Wikipedia, y tomar capturas de pantalla.

Características

Reconocimiento de voz: Usa la librería speech_recognition para entender los comandos de voz.
Síntesis de voz: Usa pyttsx3 para responder en voz.
Integración con Wikipedia: El asistente puede buscar información en Wikipedia y responder de forma resumida.
Captura de pantalla: Con la librería pywhatkit, el asistente puede tomar capturas de pantalla.
Apertura de sitios web: Puede abrir páginas web como YouTube o Google.
Consultas sobre el tiempo, fecha, y hora.
Requisitos

Para ejecutar este proyecto, necesitarás tener instaladas las siguientes librerías de Python:

pyttsx3 para la síntesis de voz.
speech_recognition para la transcripción de voz a texto.
pywhatkit para tomar capturas de pantalla y más.
yfinance para obtener información financiera.
pyjokes para obtener chistes.
wikipedia para buscar y extraer información de Wikipedia.
Asegúrate de tener Python 3.9 o superior instalado.

Instalación
Clona este repositorio en tu máquina local:

bash
Copiar código
git clone https://github.com/tu-usuario/tu-repositorio.git
Navega al directorio del proyecto:

bash
Copiar código
cd tu-repositorio
Instala las dependencias del proyecto usando pip:

bash
Copiar código
pip install -r requirements.txt
Si no tienes las voces del sistema instaladas, asegúrate de configurarlas en las propiedades de pyttsx3. En Windows, puedes seleccionar las voces desde las opciones en el sistema operativo.

Uso
Para ejecutar el asistente virtual, ejecuta el siguiente comando:

bash
Copiar código
python main.py
El asistente comenzará a escucharte y podrás interactuar con él usando comandos de voz.

Comandos disponibles:
"Abrir YouTube": Abre YouTube en el navegador.
"Qué día es hoy": Informa el día actual.
"Qué hora es": Informa la hora actual.
"Captura de pantalla": Toma una captura de pantalla y la guarda en el directorio del proyecto.
"Busca en Wikipedia [tema]": Busca en Wikipedia y devuelve una respuesta resumida.
Ejemplo de Uso:
El asistente iniciará y dirá: "Buenos días, soy Sabina, tu asistente personal. ¿En qué te puedo ayudar?"
Puedes responder: "¿Qué hora es?"
El asistente responderá: "En este momento la hora es 12 con 30 minutos y 15 segundos."
Contribución
Si deseas contribuir a este proyecto:

Haz un fork del repositorio.
Crea una rama con tu nueva característica (git checkout -b mi-nueva-caracteristica).
Realiza un commit de tus cambios (git commit -am 'Añadir nueva característica').
Envía tus cambios a la rama principal (git push origin mi-nueva-caracteristica).
Crea una Pull Request.
