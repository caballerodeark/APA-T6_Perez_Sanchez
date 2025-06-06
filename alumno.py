"""
alumno.py

Guillem Perez Sanchez QP 2025
Clase Alumno y la función leeAlumnos de tarea
"""
import re

class Alumno:
    """
    Clase usada para el tratamiento de las notas de los alumnos. Cada uno
    incluye los atributos siguientes:

    numIden:   Número de identificación. Es un número entero que, en caso
               de no indicarse, toma el valor por defecto 'numIden=-1'.
    nombre:    Nombre completo del alumno.
    notas:     Lista de números reales con las distintas notas de cada alumno.
    """

    def __init__(self, nombre, numIden=-1, notas=[]):
        self.numIden = numIden
        self.nombre = nombre
        self.notas = [nota for nota in notas]

    def __add__(self, other):
        """
        Devuelve un nuevo objeto 'Alumno' con una lista de notas ampliada con
        el valor pasado como argumento. De este modo, añadir una nota a un
        Alumno se realiza con la orden 'alumno += nota'.
        """
        return Alumno(self.nombre, self.numIden, self.notas + [other])

    def media(self):
        """
        Devuelve la nota media del alumno.
        """
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __repr__(self):
        """
        Devuelve la representación 'oficial' del alumno. A partir de copia
        y pega de la cadena obtenida es posible crear un nuevo Alumno idéntico.
        """
        return f'Alumno("{self.nombre}", {self.numIden!r}, {self.notas!r})'

    def __str__(self):
        """
        Devuelve la representación 'bonita' del alumno. Visualiza en tres
        columnas separas por tabulador el número de identificación, el nombre
        completo y la nota media del alumno con un decimal.
        """
        return f'{self.numIden}\t{self.nombre}\t{self.media():.1f}'

def leeAlumnos(ficAlum):
    """
    Lee un fichero de texto con los datos de todos los alumnos 
    y devuelva un diccionario en el que la clave sea el nombre de 
    cada alumno y su contenido el objeto Alumno correspondiente.

    La función deberá cumplir los requisitos siguientes:
        - Sólo debe realizar lo que se indica; es decir, debe leer 
          el fichero de texto que se le pasa como único argumento y 
          devolver un diccionario con los datos de los alumnos.
        - El análisis de cada línea de texto se realizará usando 
          expresiones regulares.
        - La función leeAlumnos() debe incluir, en su cadena de documentación, 
          la prueba unitaria siguiente según el formato de la biblioteca doctest.
    """
    
    alumnos = {}

    patron = re.compile(r"^(\d+)\s+(.*?)(?=\s+\d)\s+(.+)$")

    with open(ficAlum, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue  # ignorar líneas vacías

            m = patron.match(linea)
            if not m:
                raise ValueError(f"Línea mal formada: {linea}")

            numIden = int(m.group(1))
            nombre = m.group(2).strip()
            notas = [float(x) for x in m.group(3).split()]

            alumnos[nombre] = Alumno(nombre, numIden, notas)

    return alumnos
