"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def initcatalog():
    return {"videos": lt.newList('ARRAY_LIST')}

def addvideo (catalog, video):
    lt.addLast(catalog["videos"],video)

def addcatgories(catalog,categoria):
    lt.addLast(catalog["videos"],categoria)

def addvideolarge(catalog,videol):
    lt.addLast(catalog["videos"],videol)

def cmpVideosByViews(video1, video2): 
    if (float(video1['views'])<float(video2['views'])):
        return True
    elif (float(video1['views'])>float(video2['views'])):
        return False

def sortVideo(catalog, size, Tipo):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    if Tipo=="shell":
        A=sa.sort(sub_list,cmpVideosByViews)
    elif Tipo=="insertion":
        A=i_s.sort(sub_list,cmpVideosByViews)
    elif Tipo=="selection":
        A=ss.sort(sub_list,cmpVideosByViews)
    else:
        A=None
    return A


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento