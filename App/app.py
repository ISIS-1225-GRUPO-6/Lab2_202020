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
from Sorting import shellsort as sh
from Sorting import mergesort as ms
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
    print("4- Consultar peliculas buenas de un director")
    print("5- Consultar peliculas")
    print("6- Conocer a un director")
    print("7- Conocer a un actor")
    print("8- Conocer genero")
    print("9- ordenar genero")
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

def countElementsByCriteria(criteria, column, lst, lst1):
    "requerimiento 1"
    if lst['size']==0 or lst1['size']==0:
        print("lista vacia")
        return 0
    else:
        t1_start=process_time()
        cont=0
        suma=0.0
        prom = 0.0
        for i in range(lst1['size']):
            elemento= lt.getElement(lst1,i)
            if elemento[column]==criteria:
                id=int(elemento['id'])
                for j in range(lst['size']):
                    elemento1 = lt.getElement(lst,j)
                    if int(elemento1['id'])==id and float(elemento1['vote_average']) >= 6.0:
                        cont+=1
                        suma += float(elemento1['vote_average'])
                        break
        t1_stop = process_time() #tiempo final
        print("\nTiempo de ejecución ",t1_stop-t1_start," segundos\n")
        if(cont==0):
            return "0"
        else: 
            prom=(suma/cont)
    return("El director tiene "+str(cont)+" peliculas buenas y su calificación media es "+str(prom))

def mayor(pelicula1, pelicula2, column):
    if(float(pelicula1[column])>float(pelicula2[column])):
        return True
    return False

def menor(pelicula1, pelicula2, column):
    if(float(pelicula1[column])<float(pelicula2[column])):
        return True
    return False

def order(list, maome, column):
    "requerimiento 2"
    if(maome==0):
        ms.mergesort(list , mayor, column)
        for i in range(10):
            pelicula = lt.getElement(list, i)
            print (str(i+1)+". "+pelicula['title']+": "+ pelicula[column])
    else:
        ms.mergesort(list , menor, column)
        for i in range(10):
            pelicula = lt.getElement(list, i)
            print (str(i+1)+". "+pelicula['title']+": "+ pelicula[column])

def orderGender(list, maome, criteria, column):
    "requerimiento 6"
    if(maome==0):
        ms.mergesort(list,mayor, column)
        rep=0
        promedio=0
        calificacion=0.0
        for i in range(list['size']):
            pelicula = lt.getElement(list, i)
            if rep>=10:
                break
            generos = pelicula['genres'].split("|")
            for genero in generos:
                if genero.strip() == criteria:
                    rep+=1
                    promedio= int(pelicula['vote_count'])
                    calificacion += float(pelicula['vote_average'])
                    print (str(rep)+". "+pelicula['title']+", tiene : "+ pelicula['vote_count']+" votos y su calificacion es: "+ pelicula['vote_average'])
                    break
        print("el promedio de votos es : "+ str((promedio/10))+ " y su calificacion promedio es: "+ str((calificacion/10.0)))
            
    else:
        ms.mergesort(list,menor, column)
        rep=0
        promedio=0
        calificacion=0.0
        for i in range(list['size']):
            pelicula = lt.getElement(list, i)
            if rep>=10:
                break
            generos = pelicula['genres'].split("|")
            for genero in generos:
                if genero.strip() == criteria:
                    rep+=1
                    promedio= int(pelicula['vote_count'])
                    calificacion += float(pelicula['vote_average'])
                    print (str(rep)+". "+pelicula['title']+", tiene : "+ pelicula['vote_count']+" votos y su calificacion es: "+ pelicula['vote_average'])
                    break
        print("el promedio de votos es : "+ str((promedio/10))+ " y su calificacion promedio es: "+ str((calificacion/10.0)))

def conocerAUnDir(lst, lst1, criteria):
    "requerimiento 3"
    if lst['size']==0 or lst1['size']==0:
        print("lista vacia")
    else:
        t1_start=process_time()
        cont=0
        suma=0.0
        prom = 0.0
        for i in range(lst1['size']):
            elemento= lt.getElement(lst1,i)
            if elemento['director_name']==criteria:
                id=int(elemento['id'])
                for j in range(lst['size']):
                    elemento1 = lt.getElement(lst,j)
                    if int(elemento1['id'])==id:
                        cont+=1
                        suma += float(elemento1['vote_average'])
                        print(str(cont)+": "+elemento1['original_title'])
                        break
        t1_stop = process_time() #tiempo final
        print("\nTiempo de ejecución ",t1_stop-t1_start," segundos")
        if(cont==0):
            prom = 0
            print("el director no existe en el catalogo")
        else: 
            prom=(suma/cont)
            print("\nEl director tiene "+str(cont)+" peliculas buenas y su calificación media es "+str(prom))

def existe(lst, column, criteria ):
    for i in  range(lst['size']):
        element = lt.getElement(lst, i)
        if(element[column] == criteria):
            return True
            break
        else:
            return False

def conocerAUnActor(lst, lst1, criteria):
    "requerimiento 4"
    if lst['size']==0 or lst1['size']==0:
        print("lista vacia")
    else:
        director = lt.newList()
        t1_start=process_time()
        cont=0
        suma=0.0
        prom = 0.0
        directorname=""
        for i in range(lst1['size']):
            elemento= lt.getElement(lst1,i)
            if elemento['actor1_name']==criteria or elemento['actor2_name']==criteria or elemento['actor3_name']==criteria or elemento['actor4_name']==criteria or elemento['actor5_name']==criteria:
                namedic = elemento['director_name']
                if director['size']==0 or director== None:
                    lt.addFirst(director,{'name':namedic, 'veces':1})
                else:
                    if existe(director,'name', namedic):
                        for dir in director:
                            if dir['name']==namedic:
                                dir['veces']+=1
                                break
                    else:
                        lt.addLast(director,{'name':namedic, 'veces':1})


                id=int(elemento['id'])
                for j in range(lst['size']):
                    elemento1 = lt.getElement(lst,j)
                    if int(elemento1['id'])==id:
                        cont+=1
                        suma += float(elemento1['vote_average'])
                        print(str(cont)+": "+elemento1['original_title'])
                        break

        mas=0           
        for i in range(director['size']):
            element = lt.getElement(director, i)
            if int(element['veces'])> mas:
                mas=int(element['veces'])
                directorname= element['name']

        t1_stop = process_time() #tiempo final
        print("\nTiempo de ejecución ",t1_stop-t1_start," segundos")
        if(cont==0):
            prom = 0
        else: 
            prom=(suma/cont)
    print("\nEl actor tiene "+str(cont)+" peliculas y su calificación media es "+str(prom)+ "\n el director con quien mas ha grabado es: "+ directorname)

def conocerGenero(lst, criteria):
    "requerimiento 5"
    if lst['size']==0 :
        
        print("lista vacia")
    else:
        t1_start=process_time()
        cont=0
        suma=0.0
        prom = 0.0
        for i in range(lst['size']):
            elemento= lt.getElement(lst,i)
            generos = elemento['genres'].split("|")
            for genero in generos:
                if genero.strip() == criteria:
                    cont+=1
                    suma += float(elemento['vote_average'])
                    print(str(cont)+": "+elemento['original_title'])
                    break
                
        t1_stop = process_time() #tiempo final
        print("\nTiempo de ejecución ",t1_stop-t1_start," segundos")
        if(cont==0):
            prom = 0
        else: 
            prom=(suma/cont)
    print("\nEl genero tiene "+str(cont)+" peliculas y su calificación media es "+str(prom))
                      
def menu1():
    print("\nBienvenido")
    print("1- id")
    print("2- genero")
    print("3- id imdb")
    print("4- titulo original")
    print("5- popularidad")
    
def menu2():
    print("\nBienvenido, te mostraremos las 10 peliculas: ")
    print("1- mas votadas")
    print("2- menos votadas")
    print("3- mejor calificadas")
    print("4- peor calificadas")
    
def selcol(resp):
    resp1=''
    if resp ==1:
        resp1 = '\ufeffid'
    elif resp ==2:
        resp1 = 'genres'
    elif resp ==3:
        resp1 = 'imdb_id'
    elif resp ==4:
        resp1 = 'original_title'
    elif resp ==5:
        resp1 = 'vote_average'
    else:
        print("no seleccionaste ninguna opcion valida")
    
    return resp1

def selorden(resp):
    resp1=0
    if resp ==1:
        resp1 = 0
    elif resp ==2:
        resp1 = 1
    elif resp ==3:
        resp1 = 0
    elif resp ==4:
        resp1 = 1
    else:
        print("no seleccionaste ninguna opcion valida")
    
    return resp1

def selcol1(resp):
    resp1=''
    if resp ==1:
        resp1 = 'vote_count'
       
    elif resp ==2:
        resp1 = 'vote_count'
        
    elif resp ==3:
        resp1 = 'vote_average'
        
    elif resp ==4:
        resp1 = 'vote_average'
       
    else:
        print("no seleccionaste ninguna opcion valida")
    
    return resp1
      
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    lista1 = lt.newList() 
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/themoviesdb/SmallMoviesDetailsCleaned.csv")
                lista1 = loadCSVFile("Data/themoviesdb/MoviesCastingRaw-small.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            
            
            
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            
            
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    menu1()
                    resp = input("seleccione que columna buscar \n")
                    columna = selcol(int(resp))
                    criteria =str(input('Ingrese el criterio de búsqueda\n'))
                    counter=countElementsFilteredByColumn(criteria, columna, lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria   )

             
                   
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("en esta opcion te mostraremos la cantidad de peliculas \n  bien calificadas de un autor")
                    criteria =input('Ingrese el criterio de búsqueda , el nombre del autor\n')
                    counter=countElementsByCriteria(criteria,'director_name',lista,lista1)
                    print(counter," , mostrando resultados, para el director: '", criteria ,"' (\n estas, que tienen una calificacion mayor a 6.0)")



            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    menu2()
                    resp = input("seleccione que opcion buscar \n")
                    orden=selorden(int(resp))
                    columna = selcol1(int(resp))
                    order(lista,orden,columna)

            elif int(inputs[0])==6: #opcion 6
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("en esta opcion te mostraremos las peliculas de un director")
                    criteria =input('Ingrese el criterio de búsqueda , el nombre del director\n')
                    conocerAUnDir(lista,lista1, criteria)

            elif int(inputs[0])==7: #opcion 7
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("en esta opcion te mostraremos las peliculas de un actorr")
                    criteria =input('Ingrese el criterio de búsqueda , el nombre del actor\n')
                    conocerAUnActor(lista,lista1, criteria)

            elif int(inputs[0])==8: #opcion 8
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("en esta opcion te mostraremos las peliculas de un genero")
                    criteria =input('Ingrese el criterio de búsqueda , el genero\n')
                    conocerGenero(lista,criteria)

            elif int(inputs[0])==9: #opcion 9
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    menu2()
                    resp = input("seleccione que opcion buscar \n")
                    criteria =input('Ingrese el criterio de búsqueda , el genero\n')
                    orden=selorden(int(resp))
                    columna = selcol1(int(resp))
                    orderGender(lista, orden, criteria, columna )
                   
                
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()