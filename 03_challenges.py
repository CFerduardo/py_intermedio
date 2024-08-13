#fizzBuzz 
def fizzBuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzBuzz()


#Anagrama
def anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

resultado = anagrama('amor', 'amor')
print(resultado)


#Fibonacci
def fibonacci(n):
    my_list = [0,1]
    while len(my_list) < n:
        my_new_list = my_list[-1] + my_list[-2]
        my_list.append(my_new_list)
    return my_list

resultado_fibonacci = fibonacci(50)
print(resultado_fibonacci)


#Numero primo
"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo():
    for number in range(1, 101):

        if number >= 2 :
            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)

es_primo()


#Cadena invertida
"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def reverse(text):
    text_len = len(text)
    reverse_text = ""
    for index_text in range(0, text_len):
        reverse_text += text[text_len - index_text - 1]
    return reverse_text

print(reverse('hola mundo'))