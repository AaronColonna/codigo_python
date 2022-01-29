def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos" + tipo_pesos + "tienes?: ") #Entrada por teclado
    pesos = float(pesos) #Entrada convertido a punto flotante
    dolares = pesos / valor_dolar #Dólar del día #Operación para convertir los COP a USD
    dolares = round(dolares, 2) #Acortar cantidad de decimales
    dolares = str(dolares) #Números a string
    print("Tienes $" + dolares + " dólares") #Impresión 

menu = """
Bienvenido al conversor de monedas 🤑

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """ #Windows + punto permite colocar emojis. Triple comilla permite escribir string en varias lineas

opcion = input(menu)

if opcion == "1":
    conversor("colombianos", 3875)
elif opcion == "2":
    conversor("argentinos", 65)
elif opcion == "3":
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción correcta, por favor")
