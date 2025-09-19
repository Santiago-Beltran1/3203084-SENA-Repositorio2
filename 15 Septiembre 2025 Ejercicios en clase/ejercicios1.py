#Imprime el espacio donde se guarda la variable
var1 = 10
print(id(var1))

#Imprime el mismo espacio ya que es como un clon de la primera variable (uno esta dentro de otro)
var2 = "jose"
var3 = var2

print(id(var2))
print(id(var3))


#Imprime la cantidad de bytes que ocupa esas variables en el sistema
import sys
var4 = 1
print(sys.getsizeof(var4))

var5 = "josé"
print(sys.getsizeof(var5))