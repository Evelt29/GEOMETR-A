from lib import *


#hw()
obj_rect = Rectangulo(10,5)
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
