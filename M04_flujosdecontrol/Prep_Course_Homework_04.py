#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

numero = 1
if numero < 0:
    print("El numero es menor a cero")
elif numero > 0:
    print("El numero es mayor a cero")
else:
    print("el numero es 0")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

variable1 = "hola"
variable2 = 5
if type(variable1) == type(variable2):
    print("los tipos de datos son los mismos")
else:
    print("los tipos de datos son diferentes")



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range (1,21):
    if i%2==0:
        print(i," es par")
    else:
        print(i, " no es par")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6):
    print(i**3)



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

var = 5
for i in range(1,var+1):
    print(i)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

numero = 5
factorial = 5
i = 1
while i <= numero:
    factorial = i*factorial
    i=i+1
    print(i)



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

num = 5
var = 8
while num < 0:
    for i in range(0,1):



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

num = 5
for x in range(1,10):
    while num > 0:



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for i in range (3,30):
    for num in range (2,i):
        if i % num == 0:
            val = False
            break
        else:
            val = True
    if val == True:
        print(i," es primo")  


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

#SI 



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:


# In[57]:

# ITERA HASTA ENCONTRAR SI ES O NO PRIMO


# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

i = 1
while i < 300:
    if i < 100:
        i=i+1
        continue
    if i % 12 == 0:
        print(i, " Es divisible entre 12")
    i=i+1



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

print("escriba un numero")
num = int(input())
print("el numero escogido es ", num)

for i in range (2,num):
    if num % i == 0:
        val = False
        break
    else:
        val = True
if val == True:
    print(num," es primo")
else:
    print(num," no es primo")

print("Quiere saber cual es el siguiente numero primo? (S/N) ")
asig = input()
if asig == "S":
    num2 = num+1
    ayuda = False
    while ayuda == False:
        for i in range (3,num2):
            if num2 % i == 0:
                val2 = False
                break
            else:
                val2 = True
        if val2 == True:
            print("el siguiente numero primo es: ", num2)
            ayuda = True
        else:
            num2=num2+1


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
i = 100
while i % 3 != 0 and i % 6 != 0:
    i=i+1
print (i, " es el numero")



