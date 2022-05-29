# -- str = Convert Number to object
print("\nString (Convert number to object):")
my_num = 2
test = "is my favorite number"
print(str(my_num) + " is my favorite number")
    #En este caso es necesario convertir la variable número para una cadena.


# -- test con f-strings
print("\ntest2 f-strings:")
complete = f"{my_num} {test}"
print(complete)


# -- abs with negativa numbers
print("\nValues Absolutes:")
num1 = -5
print(abs(num1))


# -- pow elevar base y exponente
print("\nPower of n:")
num2 = 2
print(pow(2, num2))
print(pow(num2, 2))


# -- Max_Number
print("\nTest Max_Number:")
print(max(num2,5))
print(max(9,num2))
print(max(num1,num2))
print(max(num2,num1))


# -- Min_Number
print("\nTest Min_Number:")
print(min(num2,5))
print(min(5,num2))
print(min(num2,num1))
print(min(num1,num2))


# -- Round Number
print("\nRound Number:")
print(round(num2,4))
print(round(7,num2))
print(round(num2,num1))
print(round(num1,num2))
    #Redondea los números

from math import *
    #Accede a las librerías matemáticas para poder traer las variables.

# -- Floor Number
print("\nFloor Number:")
print(floor(7.2))
print(floor(8.7))
    #Redondea hacia el menor <


# -- Ceil Number
print("\nCeil Number:")
print(ceil(7.4))
print(ceil(8.7))
    #Redondea hacia el mayor >


# -- Sqrt Number
print("\nSqrt Number:")
print(sqrt(18))
print(sqrt(9))
    #Propiedad radicación