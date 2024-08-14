#File Handling
import os       #trabajar con archivos, directorios, rutas, y otras características del sistema operativo

txt_fle = open("./07_fichero.txt", "r+") #Leer y escribir
txt_fle.write("carlos silva\n25 años\nProgramador\nProgramo en python\nvenezolano ")   #Escribir en el fichero

#print(txt_fle.read())
#print(txt_fle.read(10))        Contar numero de caracteres
#print(txt_fle.readline())       Contar por línea
#print(txt_fle.readlines())       lee todas las líneas del archivo y las devuelve como una lista
txt_fle.write('\nTambien uso lentes')

"""
with open(): Esta construcción se utiliza para abrir archivos de manera segura. Cuando se sale del bloque with, el archivo se cierra automáticamente, incluso en caso de excepciones
"""

for line in txt_fle.readlines():
    print(line)

txt_fle.close()                 #cerrar un archivo que previamente se ha abierto utilizando la función open()
#os.remove("./07_fichero.txt")  #Eliminar fichero


#_JSON FILE
import json                     #Trabajar con json

json_file = open("./07_fichero_json.json", "w+")

json_text = {
    "nombre":"camila",
    "apellido":"silva",
    "edad":25,
    "lenguaje de programcion":"python",
    "lenguajes": ["swift", "php", "c"]
}

"""
json.dump() es una función en Python que se utiliza para serializar un objeto de Python (como un diccionario, una lista o cualquier otro objeto que pueda ser convertido en un diccionario) y escribirlo en un archivo JSON.

(indent = )Cambiar los espacios del json
"""

json.dump(json_text, json_file, indent = 3)     

json_file.close()

with open("./07_fichero_json.json") as my_other_json:
    for line_json in my_other_json.readlines():
        print(line_json)

#Leer el fichero json
json_dict = json.load(open("./07_fichero_json.json"))
print(type(json_dict))
print(json_dict)
print(json_dict["nombre"])


#.csv file
import csv

csv_file = open("./07_fichero_csv.csv", "w+")

csv_write = csv.writer(csv_file)
csv_write.writerow(["nombre", "apellido", "edad", "nacionalidad"])
csv_write.writerow(["carlos", "silva", 25, "venezolano"])
csv_write.writerow(["RoussRell", "", 25, "brasilero"])

csv_file.close()

with open("./07_fichero_csv.csv") as my_other_csv:
    for line_csv in my_other_csv.readlines():
        print(line_csv)

#.xlsx file
#import xlrd Debe instalarse el modulo


#.xml file
import xml

xml_file = open("./07_fichero_xml.xml", "w+") 