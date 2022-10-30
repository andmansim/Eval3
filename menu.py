import helpers
import ejercicio3 as e3
import ejercicio4 as e4
import ejercicio2 as e2
import ejercicio1 as e1
import ejercicio5 as e5


def iniciar():
     while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Torres de Hanoi")
        print("[2] Determinante 3x3")
        print("[3] Naves Star Wars ")
        print("[4]  ")
        print("[5]  ")
        print("[6]  ")
        print("========================")
        
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Torres de Hanoi...\n")
            aguja1 = e1.Pila()
            aguja2 = e1.Pila()
            aguja3 = e1.Pila()

            #El disco más pequeño esel 74 y el más grande el 1
            for i in range(1, 75):
                aguja1.apilar(i)


            e1.cambiar_disco(aguja1.tamaño(), aguja1, aguja3, aguja2)
                            
        if opcion == '2':
            print("Determinante 3x3...\n")
            print('Forma iterativa')
            matriz = [[1, 2, 3], 
                    [2, 3, 4], 
                  [5, 6, 7]]
            #FORMA ITERATIVA
            '''i = 0
            j = 1
            h = 2
            suma = 0
            resta = 0
            contador = 0
            while contador != 6:
    
                if contador < 3:
        
                    uno = e2.det_iterativa(matriz, i, j, h)
                    suma = suma + uno
                    i, j, h = e2.parametros(i, j, h, contador)
        
                else:
                    if contador == 3:
                        h, j, i = i, j, h
            
                    dos = e2.det_iterativa(matriz, i, j, h)
                    resta = resta + dos
                    i, j, h = e2.parametros(i, j, h, contador)
                contador = contador + 1
    '''
            total = e2.iterar(0, 1, 2, 0, 0, 0, matriz)

            print('El determinante da ' + str(total))
            
        
        if opcion == '3':
            print("Naves de Star Wars...\n")
            vehiculos = helpers.leer('vehicles.csv')
            helpers.limpiar(vehiculos)
            lista = e3.filtrar(vehiculos)
            halcon = e3.añadir_datos('Halcón Milenario', 34.37, 4,4)
            estrella = e3.añadir_datos('Estrella de la Muerte', 80000, 1200000 , 825984)
            lista.append(halcon)
            lista.append(estrella)
            nombre = e3.ordenar(lista, 'nombre')
            largo = e3.ordenar(lista, 'largo')

            print('Lista ordenada de nombres ' + str(nombre) + '\n')
            print('Lista ordenada de largo ' + str(largo) + '\n')


            print(lista[-1]) 
            print(lista[-2]) 

            pasajeros = e3.ordenar(lista, 'pasajeros')
            pasajeros1 = pasajeros[0:5]
            nave = e3.naves(lista, pasajeros1, 'pasajeros', 'nombre')
            print('Naves con mayor número de pasajeros: ' + str(nave) + '\n') 
            tripulacion = e3.ordenar(lista, 'tripulacion')
            naves1 = e3.naves(lista, [tripulacion[0]], 'tripulacion', 'nombre')
            print('La nave con mayor tripulación es: ' + str(naves1) + '\n') 
            print('Naves que empiezan por AT')
            for i in nombre:
                if i.startswith('AT'):
                    print(i)

            pa = []
            for i in pasajeros:
                if i >= 6.0:
                    pa.append(i)

            naves2 = e3.naves(lista, pa, 'pasajeros', 'nombre')
            print('Naves que pueden llevar 6 o más pasajeros: ' + str(naves2) + '\n')

            nave_p = e3.sacar_info(lista, largo[-1], 'largo')
            print('Nave más pequeña: '+ str(nave_p)  + '\n') 

            nave_g = e3.sacar_info(lista, largo[0], 'largo')
            print('La nave más grande: ' + str(nave_g)  + '\n') 
            
            
            
           
        
        if opcion == '4':
            print("Polinomio...\n")
            pol = e4.Polinomio()
           
                
        if opcion == '5':
            print("...\n")
            
            
        if opcion == '6':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")