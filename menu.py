import helpers
import ejercicio3 as e3
import ejercicio1 as e1


def iniciar():
     while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] ")
        print("[2] ")
        print("[3] Naves Star Wars ")
        print("[4]  ")
        print("[5]  ")
        print("[6]  ")
        print("========================")
        
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("...\n")
            
                            
        if opcion == '2':
            print("...\n")
            
        
        if opcion == '3':
            print("Naves de Star Wars...\n")
            vehiculos = helpers.leer('vehicles.csv')
            helpers.limpiar(vehiculos)
            lista = e3.filtrar(vehiculos)
            nombre = e3.ordenar(lista, 'nombre')
            largo = e3.ordenar(lista, 'largo')
            
            print('Lista ordenada de nombres')
            print(nombre)
            print('Lista ordenada de largo')
            print(largo)
            pasajeros = e3.ordenar(lista, 'pasajeros')
            naves = e3.naves(lista, pasajeros, 'pasajeros', 'nombre')
            print('Naves con mayor número de pasajeros:')
            print(naves[0], naves[1], naves[2], naves[3], naves[4])
            tripulacion = e3.ordenar(lista, 'tripulacion')
            naves1 = e3.naves(lista, tripulacion, 'tripulacion', 'nombre')
            print('La nave con mayot tripulación es:')
            print(naves1[0])
            
            
            
           
        
        if opcion == '4':
            print("...\n")
           
                
        if opcion == '5':
            print("...\n")
            
            
        if opcion == '6':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")