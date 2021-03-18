"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *

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

def requerimiento3(catalog, Categoria,categoria):
    valor_a_busar=[]
    for i in Categoria["categorias"]["elements"]:
        for k,v in i.items():
            if categoria in v:
                valor_a_busar.append(v)
    valor=valor_a_busar[0][0:2]
    videos_1=[]
    for i in catalog["videos"]["elements"]:
            for k,v in i.items():
                if k=="category_id" and valor in v:
                    videos_1.append(i)
    nombres=[]
    dates=[]
    for i in videos_1:
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
    return (videos_1[indice_mayor], maximo,valor)

def requerimiento4(catalog,tag,country):
    if country=="todos":
        tags=[]
        for i in catalog["videos"]["elements"]:
            for k,v in i.items():
                if k=="tags" and tag in v:
                    tags.append(i)
        titulo=[]
        otros=[]
        for i in tags:
            for k,v in i.items():
                if k=="title":
                    titulo.append(v)
                if k=="channel_title":
                    otros.append(v)
                if k=="publish_time":
                    otros.append(v)
                if k=="views":
                    otros.append(v)
                if k=="likes":
                    v=int(v)
                    otros.append(v)
                if k=="dislikes":
                    otros.append(v)
                if k=="tags":
                    otros.append(v)
        chunks=[otros[x: x+6] for x in range(0,len(otros), 6)]
        dic=dict(zip(titulo,chunks))
        o=sorted(dic.items(), key=lambda e: e[1][4], reverse=True)
    else:
        paises=[]
        for i in catalog["videos"]["elements"]:
            for k,v in i.items():
                if k=="country" and v==country:
                    paises.append(i)
        tags=[]
        for i in paises:
            for k,v in i.items():
                if k=="tags" and tag in v:
                    tags.append(i)
        titulo=[]
        otros=[]
        for i in tags:
            for k,v in i.items():
                if k=="title":
                    titulo.append(v)
                if k=="channel_title":
                    otros.append(v)
                if k=="publish_time":
                    otros.append(v)
                if k=="views":
                    otros.append(v)
                if k=="likes":
                    v=int(v)
                    otros.append(v)
                if k=="dislikes":
                    otros.append(v)
                if k=="tags":
                    otros.append(v)
    chunks=[otros[x: x+6] for x in range(0,len(otros), 6)]
    dic=dict(zip(titulo,chunks))
    o=sorted(dic.items(), key=lambda e: e[1][4], reverse=True)
    return o


