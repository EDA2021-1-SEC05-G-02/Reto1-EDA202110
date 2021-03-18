import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def initcatalog():
    catalog = model.initcatalog()
    return catalog

def intiCategoria():
    Categoria= model.intiCategoria()
    return Categoria

def loaddata(catalog,Categoria):
    cargardatoscat(Categoria)
    cargardatosvideoslarge(catalog)


def cargardatos(catalog):
    vfile = cf.data_dir + 'videos/videos-small.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for video in input_file:
        model.addvideo(catalog, video)

def cargardatoscat(Categoria):
    vfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for categoria in input_file:
        model.addcatgories(Categoria, categoria)

def cargardatosvideoslarge(catalog):
    vfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for videol in input_file:
        model.addvideolarge(catalog, videol)

def requerimiento1(category_name,country,n,catalog,Categoria):
    return model.requerimiento1(category_name,country,n,catalog,Categoria)

def requerimiento2(catalog,country):
    return model.requerimiento2(catalog,country)

def requerimiento3(catalog,Categoria,categoria):
    return model.requerimiento3(catalog,Categoria,categoria)