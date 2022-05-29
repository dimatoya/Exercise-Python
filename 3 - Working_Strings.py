#   \n = New Line
#  (Desactivate)  print ("Giraffe\nAcademy")

#   \" = Quote
#  (Desactivate)  print ("Giraffe\"Academy")

# -- Capital Letter
phrase = "Giraffe Academy"
print (phrase.lower() + " is cool")  #Lowercase
print (phrase.upper() + " is cool")  #Uppercase
print (phrase.title() + " is cool")  #Title

# -- Conditional Capital Letter
print (phrase.islower())
print (phrase.isupper())
print (phrase.istitle())

# -- Combinations Conditional Capitals Letter´s
print (phrase.upper().isupper())
print (phrase.upper().islower())
print (phrase.lower().islower())
print (phrase.lower().isupper())
print (phrase.title().islower())
print (phrase.title().isupper())
print (phrase.title().istitle())

# -- Length Variable
print (len(phrase))

# -- Extract Letter
print (phrase[14])

# -- Browse Word
print (phrase.index("a"))

# -- Replace Word
print (phrase.replace("Giraffe","Abalorioum"))