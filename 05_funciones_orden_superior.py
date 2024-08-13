#Higher Order Functions 

from functools import reduce                                    #Necesario para operar con reduce()

def sum_one(values):
    return values + 1

def sum_five(values):
    return values + 5

def sum_two_values(first_value, second_value, f_sum):            #f_sum se está pasando como parámetro y guarda la función
    return f_sum(first_value + second_value)

print(sum_two_values(5, 2, sum_one))
print(sum_two_values(5, 2, sum_five))


#Closures                                                       #Retorna una funcion
def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(5)
print(add_closure(5))
print(sum_ten(5)(5))


#Built-in Higher Order Functions 

numbers = [2, 36, 5, 69]

#Map        Con un listado iterable genera otro listado iterable en funcion a la funcion que se le ha pasado  
def multpl2(number):
    return number * 2

print(list(map(multpl2, numbers)))
print(list(map(lambda number: number * 2, numbers)))


#Filter      Ejecuta una funcion que retorna true o false para saber como filtrar los valores del iterado
def filter_mayor_diez(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_mayor_diez, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


#Reduce     Operar entre los valores que va recorriendo 
def reduce_two_values(value1, value2):
    print(value1)
    print(value2)
    return value1 + value2

print(reduce(reduce_two_values, numbers))