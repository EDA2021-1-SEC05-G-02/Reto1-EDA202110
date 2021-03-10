"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from time import process_time 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def initCatalo():
    return controller.initcatalog()
def intiCategoria():
    return controller.intiCategoria()

def loadData():
    controller.loaddata(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos por categoria y pais ")
    print("3- Video tendencia por pais")
    print("4- Video tendencia por categoria")
    print ("5- Video por mas likes")

catalog = None
Categoria=None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initcatalog()
        Categoria=controller.intiCategoria()
        controller.loaddata(catalog,Categoria)
        print("Se cargo la informacion del catalogo")
        print("se cargaron:" +str(lt.size(catalog["videos"]))+ "videos")

    elif int(inputs[0]) == 2:
         print("mejores videos por pais")
         categoria = input("Escoja una categoria: ").capitalize()
         pais = input("Escoja un pais: ")
         muestra = int(input("Cuantos videos quiere ver: "))
         for i in controller.requerimiento1(categoria,pais,muestra,catalog,Categoria):
             for k,v in i.items():
                 if k=="trending_date" or k=="title" or k=="channel_title" or k=="publish_date" or k=="views" or k=="likes" or k=="dislikes":
                     print(k+": "+v)
<<<<<<< HEAD

=======
    
    
>>>>>>> 6e8489619b613946ac345315ce5e1673631754f7
    elif int(inputs[0]) == 3:
        pais = input("Escoja un pais: ")
        for k,v in controller.requerimiento2(catalog,pais)[0].items():
            if k=="title" or k=="channel_title":
                print(k+" : "+v)
        print("Pais: "+pais+" ,Dias: "+str(controller.requerimiento2(catalog,pais)[1]))
    
<<<<<<< HEAD
=======
""" PENDIENTE
>>>>>>> 6e8489619b613946ac345315ce5e1673631754f7
    elif int(inputs[0]) == 4:
        print("Se ejecuto requerimiento 3 ")
        categoria=input("Escoja una categoria: ").capitalize()
        for k,v in controller.requerimiento3(catalog,Categoria,categoria)[0].items():
            if k=="title" or k=="channel_title":
                print(k+" : "+v)
        print("Dias: "+str(controller.requerimiento3(catalog,Categoria,categoria)[1])+" Categoría id: ",str(controller.requerimiento3(catalog,Categoria,categoria)[2]))

    elif int(inputs[0]) == 5:
        print("Se ejecuto requerimiento 4 ")
        country=input("Escoja un país o si desea ver el ranking global digite 'todos': ")
        tag=input("Digite un tag: ")
        muestra=int(input("Digite el número de videos que quiere ver: "))
        contador=0
        o=controller.requerimiento4(catalog,tag,country)
        while contador<muestra:
            print("Title: ",o[contador][0])
            print("Channel title: ",o[contador][1][0])
            print("Publish time: ",o[contador][1][1])
            print("Views: ",o[contador][1][3])
            print("Likes: ",o[contador][1][4])
            print("Dislikes: ",o[contador][1][5])
            print("Tags: ",o[contador][1][2])
            contador+=1
    
    else:
        sys.exit(0)
        
sys.exit(0)