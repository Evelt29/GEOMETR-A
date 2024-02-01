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
    
    def setPeso(self,peso):
        self.peso  = peso
        return 0
    def setDescuento(self,descuento):
        self.descuento = descuento
        return 0
    def setInventario(self,inventario):
        self.inventario = inventario
        return 0
    def getPreciodto(self):
        if self.descuento != None:
            precioDescuento = self.precio - (self.precio * (self.descuento/100))
        else:
            precioDescuento = self.precio    
        return precioDescuento    
        
    
        
# FIN ARTICULO        
class Cart():
    def __init__(self,IdCart):
        self.IdCart = IdCart
        self.articulos =[ ]
        pass
        
    def __str__(self):
        printCart = f"Carrito número: {self.IdCart} \n"
        if len(self.articulos) >= 1:
            for i in range (0, len(self.articulos),1):
                printCart += f"Articulo: {self.articulos[i]}\n"
        else: 
                printCart += f"Carrito vacio"    
        return printCart    
    def addarticulo(self,IdArt):
        self.articulos.append(IdArt)
        return 0 
    
