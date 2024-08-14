#Regular Expressions    (Inspeccionar una cadena de texto)
import re               #re = para trabajar con expresiones regulares 

#match
my_string = "Esta es una cadena : de texto para 55 la explicacion de las expresiones regulares"
my_other_string = "Para que de error Esta es una Cadena de texto para la explicacion de las expresiones regulares"

"""
re.match(): Esta función es parte del módulo re y se utiliza para buscar una coincidencia al inicio de una cadena. Devuelve un objeto de coincidencia si se encuentra una, de lo contrario, devuelve None.
"""

match = re.match("Esta es una cadena", my_string, re.I)         #re.I = no importe se esa minusculas o mayusculas
print(match)
print(match.span())     #Encontrar las coincidencias en las posiciones

print(re.match("Esta es una cadena", my_other_string))          #None
print(re.match("expresiones regulares", my_string))             #None (Empieza a buscar desde el principio)


match = re.match("Para que de error", my_other_string)
#if not (match == None):        Otra forma de comparar el none 
#if match != None:        Otra forma de comparar el none 
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#print(re.match("expresiones regulares", my_other_string))  


#search
search = re.search("cadena", my_string, re.I)
print(search)
print('holi')
start, end = search.span()
print(my_string[start:end])


#findall
findall = re.findall("cadena", my_string)
print(findall)


"""
re.split() es una función en Python que pertenece al módulo re (expresiones regulares). Su principal función es dividir una cadena de texto en una lista de subcadenas basándose en una expresión regular.
"""
#split
print(re.split(":", my_string))


#sub
print(re.sub("texto", "TEXTO", my_string))
print(re.sub("cadena|Cadena", "CADENA", my_string))
print(re.sub("expresiones", "EXPLOSIONES", my_string))


#Patterns 
patterns = r'cadena|Cadena'             #sintaxis para escribir expreiones regulares 
print(re.findall(patterns, my_string))

patterns = r'cadena|expresiones'
print(re.findall(patterns, my_string))

patterns = r'[a-z]'
print(re.findall(patterns, my_string))

patterns = r'[0-9]'
print(re.findall(patterns, my_string))
print(re.match(patterns, my_string))
print(re.search(patterns, my_string))

patterns = r'\d'
print(re.findall(patterns, my_string))

patterns = r'\D'
print(re.findall(patterns, my_string))

patterns = r'[l].'
print(re.findall(patterns, my_string))

patterns = r'[l].*'
print(re.findall(patterns, my_string))


#validar email
email = "carlos.ferduardo@gmail.com"
patterns = r'[a-zA-Z0-9-_.+-]+@[a-zA-Z0-9-_.+-]+\.[a-zA-Z0-9-_.+-]+$'
print(re.match(patterns, email))
print(re.search(patterns, email))
print(re.findall(patterns, email))

#https://regex101.com