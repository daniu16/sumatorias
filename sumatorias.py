# mostrar el resultado de una secuencia de sumatorias

from re import I


print("-------------------------------------------------------------------------------------")
print("---se determina el valor de la sumatoria hasta el numero limite que se desea sumar---")
print("-------------------------------------------------------------------------------------")

#input 

n=int(input("ingrese el numero maximo que se quiere sumar enpesando desde 1: "))

i=1
sum=0

#proseccing

while i<=n:
    sum=sum+i 
    i=i+1

#output
print("el resultado es:"+str(sum))