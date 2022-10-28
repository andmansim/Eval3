import helpers
import ejercicio3 as e3
import ejercicio4 as e1


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
            print('Naves que empiezan por AT')
            for i in nombre:
                if i.startswith('AT'):
                    print(i)
            print('Naves que pueden llevar 6 o más pasajeros:')
            pa = []
            for i in pasajeros:
                if i >= '6':
                    pa.append(i)
            
            naves2 = e3.naves(lista, pa, 'pasajeros', 'nombre')
            print(naves2)
            print('Nave más pequeña:')
            nave_p = e3.sacar_info(lista, largo[-1], 'largo')
            print(nave_p)
            print('La nave más grande:')
            nave_g =e3.sacar_info(lista, largo[0], 'largo')
            print(nave_g)
            
            
            
           
        
        if opcion == '4':
            print("...\n")
           
                
        if opcion == '5':
            print("...\n")
            
            
        if opcion == '6':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")