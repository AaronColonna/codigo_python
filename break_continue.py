def run():
    # for contador in range(1000): #Imprimir numeros pares
    #     if contador %2 != 0: #condición
    #         continue #si se cumple la condición no se ejecuta lo siguiente del ciclo
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break #Finaliza al cumplir la condicion

    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__":
    run()