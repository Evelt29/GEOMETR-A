from typing import Any

#INICO CLASE POLIGONO
class Poligono:
    def __init__(self, numlado, sizelado):
        self.numlado = numlado
        self.sizelado = sizelado  

        pass
    def __str__(self):
        return f"NUMERO DE LADOS: {self.numlado} y TAMAÑO DE LADOS: {self.sizelado} "
    def nomPoly(self):
        match self.numlado:
            case 3:
                return "tu polgino es un triangulo"
            case 4:
                return "tu polgino es un cuadrado"
            case 5:
                return f"tu polgino es un pentagono ya que su NUMERO DE LADOS: {self.numlado}"
            case 6:
                return "tu polgino es un hexágono"
            case 7:
                return "tu polgino es un heptágono"
            case 8:
                return "tu polgino es un octágono"
            case 9:
                return "tu polgino es un eneágono"
            case 10:
                return "tu polgino es un decágono"
            case _:
                return "tu poligono no lo identifico"
    
    def periPoly(self):
        return (f" El perímetro es de: {self.numlado * self.sizelado}")
    
    
        
       
# FIN CLASE POLIGONOOOOO
       
       
       
       
       
# INCIO CLASE POLIGONO REGULAS
class PoligonoRegular(Poligono):
    def __init__(self,numlado,sizelado,apotema):
        super().__init__(numlado,sizelado)
        self.apotema = apotema 
        pass 
    
    
    def __str__(self):
        return f" Num lado: {self.numlado}, Size lado: {self.sizelado}, Apotema: {self.apotema}"
        
# FIN POLIGNO REGULAR