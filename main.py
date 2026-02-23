"""
ALUMNA: CLARA ANAHI GONZALEZ APOLO
MATERIA: PROG ORIENTADA A OBJETOS
TAREA: SEMANA 10
"""

from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    print("\n--- SISTEMA DE GESTION DE INVENTARIOS ---")
    print("1. Añadir nuevo producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Salir")
   

def main():
    # Al instanciar, carga los datos automaticamente o crea el archivo
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)
            except ValueError:
                print("Error de entrada: Cantidad y precio deben ser valores numericos.")

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            try:
                cant_input = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
                cantidad = int(cant_input) if cant_input else None
                
                prec_input = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
                precio = float(prec_input) if prec_input else None
                
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error de entrada: Los valores ingresados no son numericos.")

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '4':
            inventario.mostrar_inventario()

        elif opcion == '5':
            print("Saliendo del sistema...")
            break
            
        else:
            print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    main()
