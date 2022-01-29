from types import prepare_class


def palindromo(palabra): #Palindromo: palabra que es igual derecha a izquierda y viceversa
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
# |2 espacios entre funciones es una buena practica
# 
def run(): #Funcion que inicia el código, es una buena practica. Tambien se puede llamar def main
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")
# |2 espacios entre funciones es una buena practica
# 
if __name__ == "__main__": #Entry point de Python, buena practica
    run()