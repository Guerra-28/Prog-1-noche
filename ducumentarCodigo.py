print("ingrese 3 numeros enteros diferenetes") #imprime mensaje al usuario
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor")) #solicita al usuario la opcion a ordenar y lo captura en una variable
a = int(input("ingrese el numero a"))#Solicita el primer número y lo guarda en a
b = int(input("ingrese el numero b"))#Solicita el segundo número y lo guarda en b
c = int(input("ingrese el numero c"))#Solicita el tercer número y lo guarda en c

if (e == 1):    #si e es igual a 1 entra al proceso, en el lado falso no se hace nada
    if (a > b): #si a es mayor que b entra al proceso, no se hace nada en el lado falso
        if (a > c): #evalua si a es mayor que c y no hace nada en el lado falso
            if(b > c): #evalua si b es mayor que c, entra el proceso por el lado verdadero y por el lado falso se define otro proceso
               print(a, b, c) #imprime los números en el orden descendente
            else: #lado falso de evaular si b es mayor que c
               print(a, c, b)#imprime los números en el orden descendente
    if (c > a):#si c es mayor que a entra en proceso, por el lado falso no se hace nada 
        if (c > b): #si c es mayor que b entra al lado verdadero, en el lado falso no se hace nada
            if(b > a): #si b es mayor que a entra al lado verdadero, sino entra al proceso del lado falso
               print(c, b, a)#imprime los números en el orden descendente
            else: #lado falso de evaluar si b es mayor que a
               print(c, a, b)#imprime los números en el orden descendente
    if (b > a):#si b es mayor que a entra al lado verdadero, en el lado falso no se hace nada
        if (b > c): #si b es mayor que c entra al lado verdadero, en el lado falso no se hace nada
            if(a > c):#si a es mayor que c entra al lado verdadero sino entra a lado falso
               print(b, a, c) ##imprime los números en el orden descendente
            else: #lado falso de evaluar si a es mayor que c
               print(b, c, a)#imprime los números en el orden descendente


if (e == 2): #si es es igual a 2 entra al lado verdadero, por el lado falso no se hace nada
    if (a < b):#si a es menor que b entra al lado verdadero en el lado falso no se hace nada
        if (a < c):#si a es menor que c entra al lado verdadero en lado falso no se hace nada
            if(b < c):# si b es menor que c entra al lado verdadero
               print(a, b, c)#imprime los números en el orden ascendente
            else: #lado falso de evaluar si b es menor que c
               print(a, c, b)#imprime los números en el orden ascendente
    if (c < a):#si c es menor que a entra al lado verdadero en el lado falso no se hace nada
        if (c < b):#si c es menor que b entra al lado verdadero en el lado falso no se hace nada
            if(b < a):#si b es menor que a entra al lado verdadero en el lado falso no se hace nada
               print(c, b, a)#imprime los números en el orden ascendente
            else:#lado falso de evaluar si b es menor que a
               print(c, a, b)#imprime los números en el orden ascendente
    if (b < a):#si b es menor que a entra al lado verdadero en el lado falso no se hace nada
        if (b < c):#si b es menor que c entra al lado verdadero en el lado falso no se hace nada
            if(a < c):#si a es menor que c entra al lado verdadero en el lado falso no se hace nada
               print(b, a, c)#imprime los números en el orden ascendente
            else:#lado falso de evaluar si a es menor que c
               print(b, c, a)#imprime los números en el orden ascendente

if (a == b): #si a y b son iguales entra al lado verdadero y no hace nada por el lado falso
    print("b y a son iguales") #imprime que a y b son iguales
    if (a == c): #si a tambien es igual a c entra al lado verdadero
        print("a y c son iguales") #imprime que a y c son iguales
        if(b == c): #si b es igual que c entra al lado verdadero
           print(" b y c con iguales")#imprime que b y c son igules
           if(a == b == c):#si a, b y c son iguales entra al lado verdadero
              print("todos son iguales") #imprime que todos son iguales