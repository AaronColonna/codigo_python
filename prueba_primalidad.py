def es_primo(numero):
    contador= 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero: #Los numeros primos son divisibles entre 1 y si mismo
            continue #por eso saltamos esta división
        if numero % i == 0: #Si numero da una división exacta no es primo
            contador += 1 #Division exacta suma 1 al contador
    if contador == 0: #Sin divisiones extactas
        return True #Es primo
    else:
        return False #No es primo


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == "__main__":
    run()