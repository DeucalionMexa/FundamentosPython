# function input -> retorna string
name = input('Cómo te llamas? \n')
age = int(input('Cuántos años tienes? \n'))
future=int(input('Cuántos años más? \n'))

print("Hola " + name)
print("En " + str(future) + "años tendrás " + str(age + future))

#Format Strings

text_complete = "Hola {}, en {} años tendrás {} años"
print(text_complete.format(name, future, age + future))

print(f"Hola {name}, en {future} años tendrás {age + future} años")