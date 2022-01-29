def run():
    mi_diccionario = {
        "llave1": 1, #llave: valor
        "llave2": 2,
        "llave3": 3
    }
    
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Agentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }

    # print(poblacion_paises["Agentina"]) #Imprime diccionario y entre [] la llave para que nos de el valor
    
    # for pais in poblacion_paises.keys(): # metodo .keys devuelve la llave
    #     print(pais)

    # for pais in poblacion_paises.values(): # metodo .values devuelve los valores
    #     print(pais)

    # for pais in poblacion_paises.items(): # metodo .items devuelve llave y valor en tuplas
    #     print(pais)   
    
    for pais, poblacion in poblacion_paises.items(): # metodo .items devuelve llave y valor como valores separados
        print(pais + " tiene " + str(poblacion) + " habitantes")

if __name__ == "__main__":
    run()