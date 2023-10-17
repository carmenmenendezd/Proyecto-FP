from tools.Preconditions import check_argument

#Ejercicio 1:Dado un número entero, determinar si es un número primo o no.
def primo(numero:int)->bool:
    check_argument(numero>=1,'El numero es menor que 1')

    for i in range(2, int(numero)):
        if numero % i == 0:
            return False  

    return True  


    

#Ejercicio 2:Dados los números enteros 𝑛, 𝑘 con 𝑛 ≥ 𝑘 diseñar una función que calcule el número combinatorio

def combinatorio(n,k)->int:
    check_argument(n>=k, 'n tiene que ser mayor o igual que k')  
    n_menos_k=n-k
    if n==0:
        n=1
    else:
        for i in range (1,n):
            n*=i
    if k==0:
        k=1
    else:
        for i in range (1,k):
            k*=i
    if n_menos_k==0:
        n_menos_k=1
    else:
        for i in range (1,n_menos_k):
            n_menos_k*=i    
    combinatorio=n/(k*n_menos_k)
    return combinatorio


#Ejercicio 3:Dados los números enteros 𝑛, 𝑘 con 𝑛 ≥ 𝑘 diseñar una función que calcule el número 𝑆(𝑛, 𝑘)
def S(n, k)->float: 
    check_argument(n>=k, 'n tiene que ser mayor o igual que k')  
    sumatorio:int = 0
    for i in range(k + 1):
        sumatorio += ((-1)**i)*combinatorio(k, i)*((k - i)** n)
    if k==0:
        k=1
    else:
        for i in range (1,k):
            k*=i
    S:float = 1 /k * sumatorio
    return S



#Ejercicio 4: Dada una lista con números enteros, diseñar una función que devuelva otra lista con las diferencias\entre cada valor y el anterior.
def diferencia_lista (lista)->list:
    lista2=[]
    for i in range(1, len(lista)):
        diferencia = lista[i] - lista[i - 1]
        lista2.append(diferencia)
    return lista2


#Ejercicio 5:Dada una lista de cadenas de caracteres, diseñar una función que devuelva la cadena más larga.
def mas_larga(lista_cadenas)->str:
    mas_larga =""  
    longitud_mayor=0 #variable necesaria en caso de empate
    for cadena in lista_cadenas:
        if len(cadena)>longitud_mayor:
            mas_larga=cadena
            longitud_mayor=len(cadena)
        elif len(cadena)==longitud_mayor:
            mas_larga += f" y {cadena}" 
    
    return mas_larga




 