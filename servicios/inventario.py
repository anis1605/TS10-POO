import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo: str = "inventario.txt"):
        self.archivo = archivo
        self.productos = []
        # Carga automatica al iniciar
        self.cargar_inventario()

    def cargar_inventario(self):
        self.productos.clear()
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        id_producto, nombre, cantidad, precio = datos
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
            print("Notificacion: Inventario cargado exitosamente desde el archivo.")
        
        except FileNotFoundError:
            print(f"Notificacion: El archivo '{self.archivo}' no existe. Se creara uno nuevo.")
            # Crear el archivo vacio si no existe
            try:
                with open(self.archivo, 'w') as f:
                    pass
            except PermissionError:
                print(f"Error: Permiso denegado para crear el archivo '{self.archivo}'.")
        
        except PermissionError:
            print(f"Error: Permiso denegado para leer el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as f:
                for p in self.productos:
                    # Guardar formato separado por comas
                    f.write(f"{p.obtener_id()},{p.obtener_nombre()},{p.obtener_cantidad()},{p.obtener_precio()}\n")
            print("Notificacion: Cambios guardados exitosamente en el archivo.")
        except PermissionError:
            print(f"Error: Permiso denegado para escribir en el archivo '{self.archivo}'. Asegurese de tener los permisos.")
        except Exception as e:
            print(f"Error inesperado al guardar en el archivo: {e}")

    def añadir_producto(self, producto: Producto):
        # Validacion simple de ID duplicado
        for p in self.productos:
            if p.obtener_id() == producto.obtener_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        
        self.productos.append(producto)
        print("Producto añadido a la lista.")
        self.guardar_inventario()

    def actualizar_producto(self, id_producto: str, nueva_cantidad: int, nuevo_precio: float):
        encontrado = False
        for p in self.productos:
            if p.obtener_id() == id_producto:
                if nueva_cantidad is not None:
                    p.establecer_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.establecer_precio(nuevo_precio)
                encontrado = True
                break
        
        if encontrado:
            print("Producto actualizado.")
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado en el inventario.")

    def eliminar_producto(self, id_producto: str):
        longitud_inicial = len(self.productos)
        # Filtrar la lista excluyendo el producto a eliminar
        self.productos = [p for p in self.productos if p.obtener_id() != id_producto]
        
        if len(self.productos) < longitud_inicial:
            print("Producto eliminado.")
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario actual esta vacio.")
        else:
            print("\n--- PRODUCTOS EN INVENTARIO ---")
            for p in self.productos:
                print(p)
          
