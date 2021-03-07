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
from DISClib.Algorithms.Sorting import insertionsort as i_s
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import quicksort as q
from DISClib.Algorithms.Sorting import mergesort as m
assert cf
from collections import defaultdict

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def initcatalog():
        return {"videos": lt.newList('ARRAY_LIST')}
    
def intiCategoria():
    return {"categorias":lt.newList("ARRAY_LIST")}

def addvideo (catalog, video):
    lt.addLast(catalog["videos"],video)
    

def addcatgories(Categoria,categoria):
    lt.addLast(Categoria["categorias"],categoria)

def addvideolarge(catalog,videol):
    lt.addLast(catalog["videos"],videol)

def cmpVideosByViews(video1, video2): 
    if (float(video1['views'])<float(video2['views'])):
        return True
    elif (float(video1['views'])>float(video2['views'])):
        return False

def addviews(catalog):
    lt.addLast(catalog["videos"]["dislikes"], catalog["videos"]["likes"], catalog["videos"]["views"], catalog["videos"]["publish_time"], 
    catalog["videos"]["cannel_title"], catalog["videos"]["title"], catalog["videos"]["trending_date"] )

"""def sortVideo(catalog, size, Tipo):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    if Tipo=="shell":
        A=sa.sort(sub_list,cmpVideosByViews)
    elif Tipo=="insertion":
        A=i_s.sort(sub_list,cmpVideosByViews)
    elif Tipo=="selection":
        A=ss.sort(sub_list,cmpVideosByViews)
    elif Tipo=="quick":
        A=q.sort(sub_list,cmpVideosByViews)
    elif Tipo=="merge":
        A=m.sort(sub_list,cmpVideosByViews)
    else:
        A=None
    return A"""


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def requerimiento1(category_name,country,n,catalog,Categoria):
    valor_a_busar=[]
    for i in Categoria["categorias"]["elements"]:
        for k,v in i.items():
            if category_name in v:
                valor_a_busar.append(v)
    valor=valor_a_busar[0][0:2]
    videos_1=[]
    for i in catalog["videos"]["elements"]:
            for k,v in i.items():
                if k=="category_id" and valor in v:
                    videos_1.append(i)
    pais=[]
    for z in videos_1:
            for k,v in z.items():
                if k=="country" and country in v:
                    pais.append(z)
    organizada=sorted(pais, key = lambda i: (i['views']),reverse=True)
    cortar=organizada[:n]
    return cortar

def requerimiento2(catalog,country):
    paises=[]
    for i in catalog["videos"]["elements"]:
        for k,v in i.items():
            if k=="country" and v==country:
                paises.append(i)
    nombres=[]
    dates=[]
    for i in paises:
        for k,v in i.items():
            if k=="title":
                nombres.append(v)
            if k=="trending_date":
                dates.append(v)
    unicos=[]
    for i in nombres:
        if i not in unicos:
            unicos.append(i)
    d = defaultdict(list)
    for key, value in zip(nombres,dates):
         d[key].append(value)
    unicas_fechas=[]
    for key,value in d.items():
        unicas_fechas.append(set(value))
    duracion=[]
    for i in unicas_fechas:
        duracion.append(len(i))
    maximo=max(duracion)
    indice_mayor=duracion.index(maximo)
    return (paises[indice_mayor], maximo)


