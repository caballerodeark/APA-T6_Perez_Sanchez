"""
horas.py

Guillem Perez Sanchez QP 2025
Funcion normalizaHoras
"""
import re

def normalizaHoras(ficText, ficNorm):
    """
    Lee el fichero de texto ficText, lo analiza en busca de expresiones horarias 
    y escribe el fichero ficNorm en el que éstas se expresan según el formato normalizado, 
    con las horas y los minutos indicados por dos dígitos y separados por dos puntos (08:27).

    Cada línea del fichero puede contener, o no, una o más expresiones horarias, pero éstas 
    nunca aparecerán partidas en más de una línea.

    Las horas con expresión incorrecta, por ejemplo, '17:5' (en la expresión normalizada 
    deben usarse dos dígitos para expresar los minutos) u '11 de la tarde' (la tarde nunca llega hasta esa hora), 
    deben dejarse tal cual.
    """

    