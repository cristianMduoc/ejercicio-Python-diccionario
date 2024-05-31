
diccionario = {}
try:
    while(True):
        opcion=0
        print("*******************************")
        print("**   Bienvenido al programa  **")
        print("**   -----------IA---------  **")
        print("**   -DICCIONARIO EN PYTHON- **")
        print("*******************************")
        print('1) Ingresar datos al diccionario')
        print('2) Borrar datos de diccionario')
        print('3) Listar datos del diccionario')
        print('4) Probar la operación')
        print('5) Salir\n')
        opcion = int(input('Ingrese la opcion a elegir:--> '))

        def funcion1 ():
            cantidad = int(input('¿Cuantos valores ingresará?\n'))
            for contador in range(cantidad):
                operacion = input(f'Ingrese la operación número {contador+1}\n')
                descripcion = input(f'Ingrese el valor de la operación número {contador+1}\n')
                diccionario[operacion] = descripcion
                
        def funcion2 ():
            print('El diccionario contiene los siguientes valores:\n')
            print(f'{diccionario}\n')            
            diccionario.pop(input('Ingrese el nombre de la llave que eliminará\n'))
            print('El diccionario quedó con los siguientes valores:\n')
            print(f'{diccionario}\n')
            
        def funcion3():
            print(diccionario)
            
        def funcion4():
            print('El diccionario contiene los siguientes valores:\n')
            print(f'{diccionario}\n')            
            llave = input('Ingrese el valor de la llave que desea obtener\n')
            print(diccionario[llave])
            
        def funcion5():
            print("\nUd eligio salir\n")
        
        match(opcion):
            case 1:
                funcion1()  
            case 2:
                funcion2()      
            case 3:
                funcion3()      
            case 4:
                funcion4()
            case 5:
                funcion5()
                break
            case _:
                print("\ningrese opcion valida!\n")
except:
    print("Se ha producido un Error!") 