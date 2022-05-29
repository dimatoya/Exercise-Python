#Building a Basic Calculator

#First Model Calculator
print("\nPRIMER CALCULADORA CON INTEGER\n")
num1 = input("\tEnter your first number: ")
num2 = input("\tEnter your second number: ")
result_plus12 = int(num1) + int(num2)
result_subt12 = int(num1) - int(num2)
result_mult12 = int(num1) * int(num2)
result_div12 = int(num1) / int(num2)
result_res12 = int(num1) % int(num2)

print(f"\tEl resultado de tu sumatoria(+) es: {result_plus12}")
print(f"\tEl resultado de tu sustracción(-) es: {result_subt12}")
print(f"\tEl resultado de tu multiplicación(*) es: {result_mult12}")
print(f"\tEl resultado de tu división(/) es: {result_div12}")
print(f"\tEl resultado de tu residual(%) es: {result_res12}\n")

'''SOLUCIÓN:
   En este caso se utiliza la variable -> "int", 
   esto se debe a que Python por defecto 
   toma los datos obtenidos como strings.
   
   Por tanto es necesario utilizar la variable -> "int".
   Esta devuelve un número entero equivalente a la expresión.
   
   PROBLEMA:
   Solamente sirve para números enteros,
   no funciona en el caso de los decimales.'''


#Second Model Calculator
print("SEGUNDA CALCULADORA CON FLOAT")
num3 = input("\tEnter your first number: ")
num4 = input("\tEnter your second number: ")
result_plus34 = float(num3) + float(num4)
result_subt34 = float(num3) - float(num4)
result_mult34 = float(num3) * float(num4)
result_div34 = float(num3) / float(num4)
result_res34 = float(num3) % float(num4)

print(f"\tEl resultado de tu sumatoria(+) es: {result_plus34}")
print(f"\tEl resultado de tu sustracción(-) es: {result_subt34}")
print(f"\tEl resultado de tu multiplicación(*) es: {result_mult34}")
print(f"\tEl resultado de tu división(/) es: {result_div34}")
print(f"\tEl resultado de tu residual(%) es: {result_res34}")

'''SOLUCIÓN:
   En este caso se utiliza la variable -> "float"
   
   Para ambos casos la única forma de poder escribir texto en el resultado es con -> f"".
   '''