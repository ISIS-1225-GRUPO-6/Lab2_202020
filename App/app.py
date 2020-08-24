"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as sh


from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar peliculas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0




def mayor(pelicula1, pelicula2, column):
    if(float(pelicula1[column])>float(pelicula2[column])):
        return True
    return False

def menor(pelicula1, pelicula2, column):
    if(float(pelicula1[column])>float(pelicula2[column])):
        return True
    return False

def order(list, maome, column):
    if(maome==0):
        sh.shellSort(list , mayor, column)
        for i in range(10):
            pelicula = lt.getElement(list, i)
            print (pelicula['title']+": "+ pelicula[column])
    else:
        sh.shellSort(list , menor, column)
        for i in range(10):
            pelicula = lt.getElement(list, i)
            print (pelicula['title']+": "+ pelicula[column])



def orderElementsByCriteria(orden, column, lstsalida, lstentrada):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    t1_start = process_time()
    print("ejecutando proceso")
    cont=0
    if(orden==0):
        for i in range(lstentrada['size']):
            actual= lt.getElement(lstentrada,i)
            cont += 1
            if(cont<2000):
                if(lstsalida['size']==0):
                    lt.addFirst(lstsalida, actual)
                else:
                    for j in range(lstsalida['size']):
                        actual1= lt.getElement(lstsalida,j)
                        actual2=lt.getElement(lstsalida,j+1)
                        if(float(actual[column])>float(actual1[column])):
                            lt.insertElement(lstsalida,actual,j)
                            break
                        elif(float(actual[column])<float(actual1[column]) or float(actual[column])>float(actual2[column])):
                            lt.insertElement(lstsalida,actual,j+1)
                            break
                        elif(float(actual[column])<float(actual1[column]) and actual2==None):
                            lt.addLast(lstsalida, actual)
                            break
            else:
                print(lstsalida['size'])
                break


    else: 
        for i in range(lstentrada['size']):
            actual = lt.getElement(lstentrada,i)
            if(lstsalida==None):
                lt.addFirst(lstsalida, actual)
            else:
                for j in range(lstsalida['size']):
                    actual1= lt.getElement(lstsalida,j)
                    actual2=lt.getElement(lstsalida,j+1)

                    if(float(actual[column])<float(actual1[column])):
                        lt.insertElement(lstsalida,actual,j)
                        break
                    elif(float(actual[column])>float(actual1[column]) or float(actual[column])<float(actual2[column])):
                            lt.insertElement(lstsalida,actual,j+1)
                            break
                    elif(actual2==None):
                        lt.addLast(lstsalida, actual)
                        break

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")                    

def menu1():
    print("\nBienvenido, te mostraremos las 10 peliculas: ")
    print("1- mas votadas")
    print("2- menos botadas")
    print("3- mejor calificadas")
    print("4- peor calificadas")
    
def selcol(resp, orden):
    resp1=''
    if resp ==1:
        resp1 = 'vote_count'
        orden=0
    elif resp ==2:
        resp1 = 'vote_count'
        orden=1
    elif resp ==3:
        resp1 = 'vote_average'
        orden=0
    elif resp ==4:
        resp1 = 'vote_average'
        orden=1
    else:
        print("no seleccionaste ninguna opcion valida")
    
    return resp1

def pel10(lista):
    resp=""
    if lista==None or lista['size']==0: #obtener la longitud de la lista
         print("La lista esta vacía")    
    else: 
        for i in range (10):
            elemento = lt.getElement(lista,i)
            resp += elemento['original_title'] + "\n"
    return resp
    
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/themoviesdb/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    menu1()
                    resp = input("seleccione que opcion buscar \n")
                    orden=0
                    lst1 = lt.newList()
                    columna = selcol(int(resp), orden)
                    order(lista,orden,columna)
                    orderElementsByCriteria(orden ,columna, lst1, lista)  #filtrar una columna por criterio  
                    resp1= pel10(lst1)
                    print( "las peliculas son: \n" + resp1)
                   
                
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()