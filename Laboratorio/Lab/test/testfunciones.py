from Lab.funciones.funcionesentrega import primo,combinatorio, S, diferencia_lista, mas_larga
from math import comb
    
#Ejercicio 1
numero:int=4
    
    
if primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} es complejo y por tanto no es primo")
        
#Ej 2
n:int=0
k:int=0
    
print(f"Combinatorio({n},{k}) =", combinatorio(n,k))
print ('Prueba del combinatorio:',comb(n,k))
    
#Ej 3 (mismas variables que ej 2)
print(f'S({n},{k})=', S(n,k))
    
#Ej 4
lista=[2,8,3,34,7]
print(f'El resultado de restar el número anterior en {lista} es',diferencia_lista(lista))

 #Ej 5
lista_cadenas = ["Ferrari", "Fiat", "Audi", "Seat", "Peugeot","Volvo"]
print("Cadena de caracteres más larga:",(mas_larga(lista_cadenas)))