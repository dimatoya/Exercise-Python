#TRABAJO CON LISTAS
print("\n\tEJERCICIO DE LISTAS:\n")

#Variables:
list_variables = ["Dima", 2, 3.5, False]
list_text = ['Dima', 'Carlos', 'Aldana', 'Darwin', 'Miguel']

print("""Se pueden crear varios tipos de listas combinando varios tipos de variables.
Estas pueden llegar a ser texto, variables booleanas, números decimales, enteros, entre otros.
A continuación se presentan ejemplos:\n""")

print("Ejemplo 1: " + str(list_variables) + " -> En este caso una lista de variables combinada.")
print("Ejemplo 2: " + str(list_text) + " -> En este caso una lista con solamente texto.\n")

print("""Ahora bien, Las listas de izquierda a derecha se cuentan desde 0.
Un ejemplo de esto puede ser:\n
\tList_text: [\"Dima\", \"Carlos\", \"Aldana\", \"Darwin\", \"Miguel\"]
\tList_text: [   0  ,     1   ,    2    ,     3   ,     4   ] -> Izquierda a derecha\n""")

print("""En el caso de las listas con enteros negativos se leen de la siguiente manera:
\n\tList_text: [\"Dima\", \"Carlos\", \"Aldana\", \"Darwin\", \"Miguel\"]
\tList_text: [  -5  ,    -4   ,   -3    ,    -2   ,    -1   ] -> Derecha a izquierda\n\n""")

#Seleccionar variables con un SOLO NÚMERO
print("-> SELECCIONAR VARIABLES CON UN SOLO NÚMERO - Entero Positivo\n")
    # -- Enteros Positivos
print("""Para hacer un llamamiento de la variable se hará de la siguiente forma:
list_text[], siendo [] nuestra opción para seleccionar un objeto dentro de la cadena.
Se llamará a Carlos dentro de nuestra variable denominada list_text.""")
print("\n\tlist_text[1] = " + list_text[1])

    # -- Enteros Negativos
print("\n\n-> SELECCIONAR VARIABLES CON UN SOLO NÚMERO - Entero Negativo")
print("""\nDe igual forma se puede llamar a un objeto a través de una cadena de derecha a izquierda.
Como ejemplo haremos el llamado a Darwin utilizando enteros negativos.
Se hará de la siguiente forma list_text[-2]""")
print("\n\tlist_text[-2] = " + list_text[-2])

#Seleccionar variables entre un RANGO
    # -- Enteros positivos
print("\n\n-> SELECCIONAR VARIABLES CON UN RANGO - Entero Positivo\n")
print("""En la selección entre rangos con enteros positivos es necesario resaltar que no es lo mismo
buscar un rango como [1,3] y [3,1].""")
print("\n\t Para [1,3] será: list_text[1:3] = " + str(list_text[1:3]))
print("\t Para el caso de [3,1] es: list_text[3:1] = " + str(list_text[3:1]))
print("""\nEn el primer caso realiza la búsqueda, mientras en la segunda opción no es posible realizarlo.""")

    # -- Enteros negativos
print("\n\n-> SELECCIONAR VARIABLES CON UN RANGO - Entero Negativo\n")
print("Selección entre rangos con enteros negativos:")
print("\n\t Para list_text[-3:-1] = " + str(list_text[-3:-1]))
print("\t Para list_text[-1:-3] = " + str(list_text[-1:-3]))
print("""\nNOTA:
En el caso de búsquedas por rango [#,#] siempre el valor menor estará a la izquierda,
tanto para enteros positivos como enteros negativos.
\n\tEjemplo: [0,1]
\t\t[-3,-1]\n\n""")

#Cambio de un valor en la CADENA
list_text = ['Dima', 'Carlos', 'Aldana', 'Darwin', 'Miguel']
print(" -> CAMBIO DE UNA VARIABLE")
print("""\nTomando la misma cadena de list_text se realizará el cambio de una de las 
variables que se encuentran dentro. Se reemplazará el nombre de Aldana por Cinthya.""")
list_text[2] = "Cinthya"
print("\n\tlist_text[2] = Cinthya") 
print("\nObteniéndose de esta forma: " + str(list_text))
print("""\nNuevamente para llamar el rango entre Cinthya y Darwin será:\n
\tlist_text[2] = """ + str(list_text[2:4]))

#Notas de Aprendizaje
print("\n\nNOTAS:")
print("\tPrueba de comillas: \"Comillas\"")
print("\tList: [\"Dima\", \"Carlos\", \"Darwin\", \"Miguel\"]")