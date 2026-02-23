
class Producto:
    # Constructor
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self) -> str:
        return self.id_producto

    def obtener_nombre(self) -> str:
        return self.nombre

    def obtener_cantidad(self) -> int:
        return self.cantidad

    def obtener_precio(self) -> float:
        return self.precio

    def establecer_cantidad(self, cantidad: int):
        self.cantidad = cantidad

    def establecer_precio(self, precio: float):
        self.precio = precio

    # Representacion en cadena del producto
    def __str__(self) -> str:
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
