miLista = [10, 8, 6, 4, 2]
del miLista[:]
print(miLista)


sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0
for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1
print(aciertos)


miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]
for i in range(1, len(miLista)):
    if miLista [i]> mayor:
        mayor = miLista[i]
print(mayor)


miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevalista=[0]
for lista in miLista:
    if lista in nuevalista:
        continue
    else:
        nuevalista.append(lista)
print("La lista solo con elementos únicos:")
print(miLista)
print(nuevalista)


miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]
for i in miLista:
    if i > mayor:
        mayor = i
print(mayor)


cuadrados = [x ** 2 for x in range(10)]
dos = [2 ** i for i in range(8)]
print(cuadrados)
print(dos)
probabilidades = [x for x in cuadrados if x % 2 != 0]
print(probabilidades)


miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]
for i in miLista [1:]:
   if i > mayor:
        mayor = i
print(mayor)


miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False
for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break
if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")


EMPTY = "-"
TORRE = "TORRE"
CABALLO="CABALLO"
PEON="PEON"
tablero = []
for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)
tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE
tablero[4][2] = CABALLO
tablero[3][4] = PEON
print(tablero)


temps = [[0.0 for h in range(24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#
suma = 0.0
for day in temps:
    suma += day[11]
promedio= suma / 31
print("Temperatura promedio al mediodía:", promedio)


temps = [[0.0 for h in range (24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#
mas_alta = -100.0
for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp
print("La temperatura más alta fue:", mas_alta)


habitaciones =[[[False for r in range(20)] for f in range(15)] for t in range(3)]
habitaciones[2][14][5]=True
habitaciones[2][14][3]=True
habitaciones[2][14][12]=True
habitaciones[2][14][17]=True
habitaciones[2][14][1]=True
vacante=0
for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1
print(vacante)


i=2
while i >=0:
    print("*")
    i-=2

for i in range(-1,1): 
    print("#")

lst=[3,1,-1]
lst[-1]=lst[-2]
print(lst)


