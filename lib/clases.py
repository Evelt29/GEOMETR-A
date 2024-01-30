"""class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho
        pass
    
    def __str__(self):
        return f"Rectángulo de largo {self.largo} y ancho {self.ancho}"
    
    def area (self):
        return (self.ancho * self.largo)
    def perimetro(self):
        return 2*(self.ancho + self.largo)"""
# INICIO ARTICULO        
class Articulo():
    def __init__(self,marca,nombre,Id,precio=None,peso=None,descuento=None,inventario=None):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.descuento = descuento
        self.Id = Id
        self.inventario = inventario
        pass
    def __str__(self):
        return f"nombre: {self.Id} - Id: {self.marca} - marca: {self.nombre} - Precio: {self.precio} - Peso: {self.peso} - descuento: {self.descuento} - inventario: {self.inventario}"
        
    def setPrecio(self,precio):
        self.precio = precio
        return 0
        
        
# FIN ARTICULO        
class Cart():
    def __init__(self,marca,nombre,precio,peso,descuento,Id,piezas,articulo,total,iva,descTotales):
        super().__init__(marca,nombre,precio,peso,descuento,Id,piezas)
        self.articulo = articulo
        self.total = total
        self.iva = iva
        self.descTotales = descTotales
        
        
        
        

   