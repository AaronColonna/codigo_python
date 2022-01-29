#FUNCION 1#
# def imprimir_mensaje():
#     print("Mensaje espcial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

#FUNCION 2#
def conversacion(mensaje):
    print("Hola")
    print("¿Cómo estás?")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opción (1,2,3): "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")
elif opcion == 3:
    conversacion("Elegiste la opción 3")
else:
    print("Escribe la opción correcta")