# Funciones
# def name_function(params):
# code

# Sin parámetros y sin retorno
def saluda():
    print("Hola a todos!")

saluda()

# Con parámetros, sin retorno
def duplica(num):
    print(num * 2)

duplica(5)

def suma(num1, num2):
    print(f"La suma de los números es: { num1, num2 }")

suma(23, 45)

# Parámetros opcionales, sin retorno
def get_lista(al_1 = "Lalokota", al_2 = "Paquiño"):
    return [al_1, al_2]

my_list = get_lista()
print(my_list)
my_list = get_lista("Barry")
print(my_list)
my_list = get_lista("Barry Allen", "Bruce Banner")
print(my_list)
my_list = get_lista(al_2 = "Barry Allen", al_1 = "Bruce Banner")
print(my_list)