from lib import *


#hw()
"""obj_rect = Rectangulo(10,5)
print(obj_rect)
print("ANCHO: "+str(obj_rect.ancho))
print("LARGO: "+str(obj_rect.largo))

print("------------------------------------------------")
obj_rect_2= Rectangulo(25,15)
print(obj_rect_2)
print("ANCHO: "+str(obj_rect_2.ancho))
print("LARGO: "+str(obj_rect_2.largo))

print("------------------------------------------------")
obj_rect_3= Rectangulo(0,0)
obj_rect_3.ancho = 75
obj_rect_3.largo =55
print(obj_rect_3)
print("ANCHO: "+str(obj_rect_3.ancho))
print("LARGO: "+str(obj_rect_3.largo))
# perimetro = 2*(obj_rect_3.ancho + obj_rect_3.largo)
#  print("PERIMETRO:" +perimetro)
print("PERIMETRO: " +str(obj_rect_3.perimetro()) + "[cm]")
print("PERIMETRO- REC 1: " +str(obj_rect.perimetro()) +"[cm]")
print("ÁREA: "+str(obj_rect.area())+  "[cm^2]" )

# nombre de variable . (punto) + nombre de lo que queremos mandar a llamar
print("------------------------------------------------")
obj_poly_1 = Poligono(5,18) 
print(obj_poly_1)
print(f" Num lados: {obj_poly_1.numlado}")
print("------------------------------------------------")
print(obj_poly_1.nomPoly())
print("------------------------------------------------")
obj_poly_2 = PoligonoRegular(5,15,10)
print(obj_poly_2)
print(obj_poly_2.nomPoly())
print(f"El área es de: {obj_poly_2.periPoly()}")
print("------------------------------------------------")
print(f" El área es de: {obj_poly_2.getArea()}")
print(f" ¿El área es mayor a 200? {obj_poly_2.chkArea()}")
#print(obj_poly_2.setColor("Verde vejiga"))
obj_poly_2.setColor("Verde vejiga")
print(obj_poly_2.color)

num1 = "10" # / 10 
num2 = 0


try :
    div = num1 / num2
except ZeroDivisionError:
    print("No se puede dividir entre cero :( ")
    
except TypeError:
    print("No se puede dividir str entre números :( ")
    
except Exception as e:
    print(f"Error desconocido: {e}")

print("holi") 
print(" bye ")"""

art1 = Articulo(10256,"Coca-Cola","Canada Dry")
art1.setDescuento(10)
art1.setPeso(10)
art1.setInventario(10)
art1.setPrecio(25.00)
print(art1)

cart1 = Cart("ABC123")
#print(cart1)

cart2 = Cart("DEF456")
#print(cart2)

cart3 = Cart("GHI789")
#print(cart3)

art2 = Articulo(10165,"Sabritas","Rancheritos 500gr")
art2.setDescuento(25)
art2.setPeso(500)
art2.setInventario(5)
art2.setPrecio(22.00)
#print(art2)

art3 = Articulo(11608,"Bimbo","Mantacadas 150gr")
art3.setPeso(150)
#art3.setInventario(5)
art3.setPrecio(22.00)
#print(art3)

cart1.addarticulo(art1)
cart1.addarticulo(art2)
cart1.addarticulo(art3)
print(cart1)
print("---------------------------------")
print(cart1.objArticulos[0])
print(cart1.objArticulos[0].nombre)#en aso de solo querer un dato en específico se agrega "." y lo que quieres q imprima
print(cart1.objArticulos[1].nombre)
print(art1.inventario)
print(art2.inventario)
print(art3.inventario)
print("--------------------------------------")
print(f"Carrito: {cart1.IdCart}\nTotal: { cart1.geTotal1()}")