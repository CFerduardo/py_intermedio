#Lambdas (Funciones Anonimas)
sum = lambda valor1, valor2: valor1 + valor2
print(sum(5, 26))

multiplicacion = lambda mult1, mult2: mult1 * mult2 - 3
print(multiplicacion(2, 2))

def sum_lambda(valor):
    return lambda first_value, second_value: first_value + second_value + valor

print(sum_lambda(5)(2, 4))