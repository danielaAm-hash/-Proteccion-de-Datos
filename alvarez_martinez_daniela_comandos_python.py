# -*- coding: utf-8 -*-
"""Alvarez_Martinez_Daniela_Comandos_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lt3sMY_n8Zmf4Qwk__DicdCeYfUc-_mg
"""

# Local versus Global

# Definimos una función llamada local
def local():
    m = 7
    print(m)

# Definimos m dentro del alcance global
m = 5

# Llamamos o ejecutamos la función local
local()
print(m)

# Definimos una función llamada "enclosing_func" (función envolvente).
def enclosing_func():
    m = 13  # Variable "m" en el ámbito de "enclosing_func".

    # Definimos una función anidada llamada "local" (función local).
    def local():
        # La variable "m" no pertenece al ámbito definido por la función local,
        # por lo que Python seguirá buscando en el siguiente ámbito envolvente.
        # En este caso, "m" se encuentra en el ámbito envolvente de enclosing_func.
        print(m, 'imprimiendo desde el ámbito local')

    # Llamamos a la función "local".
    local()

    m = 5  # Cambiamos el valor de la variable "m" en el ámbito global.
    print(m, 'imprimiendo desde el ámbito global')

# Llamamos a la función "enclosing_func".
enclosing_func()

# Definimos dos variables, 'a' y 'b'
a = 14
b = 3

# Realizamos una operación de suma entre 'a' y 'b'
a + b
# Realizamos una operación de resta entre 'a' y 'b'
a - b
# Realizamos una operación de multiplicación entre 'a' y 'b'
a * b
# Realizamos una operación de división verdadera (con decimales) entre 'a' y 'b'
a / b
# Realizamos una operación de división entera entre 'a' y 'b'
a // b
# Realizamos una operación de módulo (residuo de la división) entre 'a' y 'b'
a % b
# Realizamos una operación de potenciación entre 'a' y 'b'
a ** b  # operación de potenciación

# Calcula 10 elevado a la tercera potencia utilizando la función pow().
# El resultado es 1000.0 y se almacena como un número en punto flotante.
pow(10, 3)
1000.0 # El resultado es un flotante (float).

# Aquí, 10  3 parece un error de sintaxis, debería ser 10 ** 3.
# Pero si interpretamos esto como una simple expresión matemática,
# sería equivalente a 10 multiplicado por 3, que es 30.
10*3
1000 # El resultado (30) es un número entero (int), aunque esto parece incorrecto.

# Calcula 10 elevado a la potencia -3 utilizando la función pow().
# El resultado es 0.001 y se almacena como un número en punto flotante.
pow(10, -3)
0.001 # El resultado es un flotante (float).

# Similar al segundo caso, 10  -3 parece un error de sintaxis,
# debería ser 10 ** -3.
# Pero si interpretamos esto como una expresión matemática,
# sería equivalente a 10 dividido por -3, que es -3.333...,
# pero parece incorrecto ya que el resultado debe ser positivo.
10  -3
0.001 # El resultado (-3.333...) parece incorrecto como un flotante (float).

# Local versus Global

# Definimos una función llamada 'local'.
def local():
    # La variable 'm' no pertenece al ámbito definido por la función 'local'.
    # Por lo tanto, Python buscará en el siguiente ámbito más externo.
    # La variable 'm' se encuentra finalmente en el ámbito global.
    print(m, 'printing from the local scope')

# Definimos una variable global 'm' con el valor 5.
m = 5

# Imprimimos el valor de 'm' desde el ámbito global.
print(m, 'printing from the global scope')

# Llamamos a la función 'local', que intenta imprimir 'm' desde su ámbito.
local()

"""**1.3 Importacion de datos python**"""

# Importamos la biblioteca 'requests', que nos permite realizar solicitudes HTTP.
import requests

# Definimos un diccionario 'urls' que contiene varios títulos y las URL correspondientes.
urls = {
    "get": "https://httpbin.org/get?t=learn+python+programming",
    "headers": "https://httpbin.org/headers",
    "ip": "https://httpbin.org/ip",
    "user-agent": "https://httpbin.org/user-agent",
    "UUID": "https://httpbin.org/uuid",
    "JSON": "https://httpbin.org/json",
}

# Definimos una función 'get_content' que toma un título y una URL como argumentos.
def get_content(title, url):
    # Realizamos una solicitud GET a la URL proporcionada.
    resp = requests.get(url)

    # Imprimimos el título y la respuesta JSON obtenida de la solicitud.
    print(f"Response for {title}")
    print(resp.json())

# Iteramos a través de las URL en el diccionario 'urls' y llamamos a la función 'get_content' para cada una.
for title, url in urls.items():
    get_content(title, url)

# Imprimimos una línea de separación para distinguir entre las respuestas de diferentes solicitudes.
print("-" * 40)

# Importamos la biblioteca 'requests', que nos permite realizar solicitudes HTTP.
import requests

# Definimos la URL a la que vamos a realizar la solicitud POST.
url = 'https://httpbin.org/post'

# Creamos un diccionario 'data' con datos que deseamos enviar en la solicitud POST.
data = dict(title='Learn Python Programming')

# Realizamos una solicitud POST a la URL proporcionada, enviando los datos contenidos en el diccionario 'data'.
resp = requests.post(url, data=data)

# Imprimimos un encabezado para indicar que estamos mostrando la respuesta de la solicitud POST.
print('Response for POST')

# Imprimimos la respuesta JSON obtenida de la solicitud.
print(resp.json())

# Importamos el módulo json.
import json
# Creamos un diccionario llamado 'info' que contiene información personal y de dirección.
info = {
    'full_name': 'Sherlock Holmes',
    'address': {
        'street': '221B Baker St',
        'zip': 'NW1 6XE',
        'city': 'London',
        'country': 'UK',
    }
}
# Usamos la función 'json.dumps' para serializar el diccionario 'info' en formato JSON.
# - 'indent=2' se utiliza para formatear el resultado con una sangría de 2 espacios para una mejor legibilidad.
# - 'sort_keys=True' se utiliza para ordenar las claves del diccionario en el resultado JSON.
result = json.dumps(info, indent=2, sort_keys=True)
# Imprimimos el resultado JSON generado.
print(result)

# Importamos la biblioteca 'json' para trabajar con datos en formato JSON y 'datetime' para trabajar con fechas y horas.
import json
from datetime import datetime, timedelta, timezone

# Obtenemos la fecha y hora actual sin zona horaria.
now = datetime.now()

# Creamos un objeto de fecha y hora con zona horaria de UTC+1 (una hora adelante de UTC).
now_tz = datetime.now(tz=timezone(timedelta(hours=1)))

# Definimos una clase personalizada 'DatetimeEncoder' que hereda de 'json.JSONEncoder'.
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            try:
                # Intentamos obtener el desplazamiento UTC en segundos, si no está disponible, lo establecemos en None.
                off = obj.utcoffset().seconds
            except AttributeError:
                off = None
            # Serializamos objetos de tipo 'datetime' en un formato personalizado.
            return {
                '_meta': '_datetime',
                'data': obj.timetuple()[:6] + (obj.microsecond, ),
                'utcoffset': off,
            }
        return super().default(obj)
# Creamos un diccionario 'data' que contiene diferentes tipos de datos, incluyendo objetos 'datetime'.
data = {
    'an_int': 42,
    'a_float': 3.14159265,
    'a_datetime': now,
    'a_datetime_tz': now_tz,
}

# Convertimos el diccionario 'data' en una cadena JSON utilizando nuestra clase personalizada 'DatetimeEncoder'.
json_data = json.dumps(data, cls=DatetimeEncoder)
print(json_data)

# Importamos el módulo 'io' que nos proporciona herramientas para trabajar con entrada/salida.

import io

# Creamos un objeto 'stream' de tipo 'io.StringIO'. Esto permite tratarlo como un archivo en memoria que almacena texto.

with io.StringIO() as stream:
    # Escribimos una línea de texto en el 'stream'.
    stream.write('Learning Python Programming.\n')

    # Usamos 'print' para escribir otra línea de texto en el 'stream'. El argumento 'file' especifica el destino, que es el 'stream'.
    print('Become a Python ninja!', file=stream)

    # Obtenemos el contenido completo del 'stream' utilizando 'getvalue()' y lo almacenamos en la variable 'contents'.
    contents = stream.getvalue()

    # Imprimimos el contenido que hemos almacenado en 'contents'.
    print(contents)