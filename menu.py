import helpers
import ejercicio3 as e3

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
            nombre = e3.ordenar(lista, 'name')
            largo = e3.ordenar(lista, 'length')
            
            print('Lista ordenada de nombres')
            print(nombre)
            print('Lista ordenada de largo')
            print(largo)
            if 'Stat of death' in nombre:
                print('Si')
            if 'Millenium Falcon' in nombre:
                print('Si')
            
           
        
        if opcion == '4':
            print("...\n")
           
                
        if opcion == '5':
            print("...\n")
            
            
        if opcion == '6':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")