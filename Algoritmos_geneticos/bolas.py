from random import randint, shuffle
from copy import deepcopy

vueltas = 0

def aleatorios():
    fila=[]
    numeros = [1,2,3,4,5,6,7,8,9,10]
    shuffle(numeros)
    multiplica = numeros[:5]
    suma = numeros[5:]
    fila.append(multiplica)
    fila.append(suma)
    return fila


def valoresSuma(vectorM, vectorS):
    sobra = 1
    for i in range(0,5):
        resp = sobra in vectorM
        while resp == True:
            sobra+=1
            resp = sobra in vectorM
        vectorS[i]=sobra
        sobra+=1
    return vectorS


def comprobarMutacion(vector):
    for i in  range(0,len(vector)) :
        for j in range(i+1,len(vector)):
            if vector[i] == vector[j]:
                muta = 1
                resp = muta in vector
                while resp == True:                                      
                    muta +=1 
                    resp = muta in vector                     
                vector[j]=muta

def cruce(generacion):
    posicion=[0,1,2,3,4,5,6,7,8,9,10,11]
    shuffle(posicion)    
    i=0
    while i<len(posicion):
        punto = randint(1,4)

        padreM = generacion[posicion[i]][0]        
        madreM=generacion[posicion[i+1]][0]

        generacion[posicion[i]][0] = padreM[:punto]+madreM[punto:]
        comprobarMutacion(generacion[posicion[i]][0])   

        generacion[posicion[i+1]][0] = madreM[:punto]+padreM[punto:]
        comprobarMutacion(generacion[posicion[i+1]][0])     

        i+=2

    if competencia(generacion)==True:
        return True



    

def comprobacion(multiplica,suma):        
    rSuma = sum(suma)
    rMultiplica = multiplica[0]*multiplica[1]*multiplica[2]*multiplica[3]*multiplica[4]
    if rMultiplica == 360:
        if rSuma==36:
            print ("La combinación Correcta es:")
            print("Multiplicación:",multiplica)
            print("Suma:",suma)
            print("Se obtubo el resultado en la", vueltas ,"generacion")
            return True
        else:
            return 2
    else:
        resultado=abs(360-rMultiplica)
        return resultado

def competencia(generacion):
    global vueltas
    vueltas+=1
    posicion=[0,1,2,3,4,5,6,7,8,9,10,11]
    shuffle(posicion)
    valores=[]
    for i in range(0,12):
        resultado = comprobacion(generacion[i][0],generacion[i][1])
        if resultado == True:
            return True
        elif resultado==2:
            resp = valoresSuma(generacion[i][0],generacion[i][1])
            resultado = comprobacion(generacion[i][0],resp)
            if resultado == True:
                return True
            else:
                valores.append(resultado) 
        else:
            valores.append(resultado)  
    i=0
    while i<len(valores):
        
        if valores[posicion[i]]<valores[posicion[i+1]]: 
            generacion[posicion[i+1]] = deepcopy(aleatorios())
        else:
            generacion[posicion[i]]= deepcopy(aleatorios())
        i+=2
    cruce(generacion)
            
                      


        

numeros = [1,2,3,4,5,6,7,8,9,10]    
generacion=[]
for i in range(0,12):
    shuffle(numeros)
    fila=[]
    if(sum(numeros[:5])<sum(numeros[5:])):        
        multiplica = numeros[:5]
        suma = numeros[5:]
    else:
        multiplica = numeros[5:]
        suma = numeros[:5]
    fila.append(multiplica)
    fila.append(suma)
    generacion.append(fila)
competencia(generacion)
