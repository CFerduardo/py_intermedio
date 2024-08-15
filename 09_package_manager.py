#Package Manager (gestor de paquetes para python 

#pip                
"""
NumPy es una biblioteca fundamental en Python para realizar cálculos numéricos y trabajar con matrices
"""

import numpy

import intermediate.arithmetics            #pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([26, 69, 89, 6, 37, 48, 24])
print(type(numpy_array))

print(numpy_array * 2)


"""
pandas diseñada para la manipulación y el análisis de datos. Proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento y fáciles de usar
"""

import pandas           #pip install pandas 


#pip list                   obtener una lista completa de todos los paquetes que tienes instalados en tu entorno de Python
#pip uninstall pandas       desinstalar paquetes que ya no necesitas o que están causando problemas
#pip show numpy             obtener información detallada sobre un paquete específico que tienes instalado


import requests           #pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


#Arithmetics Package 
from intermediate import arithmetics

print(arithmetics.sum_values(5, 4))


#Arithmetics2 Package
from intermediate import arithmetics2

print(arithmetics2.sum_two_values(120, 26))