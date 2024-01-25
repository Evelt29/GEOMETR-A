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
print(" bye ")
