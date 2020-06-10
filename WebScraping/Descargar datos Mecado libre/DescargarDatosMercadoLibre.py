# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:32:48 2020

@author: jsvel
"""

#Script para descargar bases de mercado libre


#algunas aplicaciones útiles

from selenium import webdriver # webdriver
from selenium.webdriver.support.ui import Select # allows us to use css expresions
import time # time pauses and other utilities
from selenium.webdriver.common.by import By #allows to use by_class by_id and others 
from selenium.webdriver.support.ui import WebDriverWait # wait until something happens
from selenium.webdriver.support import expected_conditions as EC # evaluates if Expected Condition has happened


import pandas as pd
import numpy as np



# usamos tiempos aleatorios para que no sea posible identificar que es una máquina quien está haciendo el trabajo

def te():
    tcorto =  np.random.gamma(1,1) # + np.random.noncentral_f(1000,32,3) # + np.random.noncentral_chisquare(0.5,4)
    return tcorto    

# por lo tanto el algoritmo tiene un 

te()

from win32api import GetSystemMetrics

web = webdriver.Chrome(executable_path= "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")



web.get('https://www.mercadolibre.com.co/')

web.set_window_position(0, 0)
web.set_window_size(GetSystemMetrics(0),GetSystemMetrics(1))



def buscar():    
# palabra de la busqueda

    print('por favor ingrese el producto que desea scrapear')
    
    producto = input()
    
    # nombre del archivo donde se guardaran los datos descargados
    print('por favor ingrese el nombre del archivo donde quiere guardar la información')
    nombre = input()
    
    #Class
    
    print('cual es la clase html del objeto buscado')
    claseObjetoBuscado = input() #'results-item'
    
    print('por favor espere, estamos descargando la información para usted')
    #Seleccionando el buscador
    
    buscador = web.find_element_by_class_name('nav-search-input')
    buscador.send_keys(producto)
    web.find_element_by_class_name('nav-icon-search').click()
    time.sleep(te())
    #items =  web.find_elements_by_class_name(claseObjetoBuscado)
    
    # creamos una funcion para recorrer los items
    
    
    def rec_items (classname):
        time.sleep(te()) # damos algunos tiempos para esperar
        items =  web.find_elements_by_class_name(classname) # seleccionamos los elementos de la clase row item
        l = len(items) # tomamos el largo de los items para saber cuantas veces hacer las extracciones
        descrip = [None]*l 
        price = [None]*l
        envio = [None]*l
        ciudad = [None]*l
        otro1 = [None]*l
        otro2 = [None]*l
        benef = [None]*l
        stock = [None]*l
        disponibles = [None]*l
        official = [None]*l
        ventas = [None]*l
        infoVentas = [None]*l
        atencion = [None]*l
        entrega = [None]*l
        vendidos = [None]*l
        nopiniones = [None]*l
        calificacion = [None]*l
        vendedor = [None]*l
        ubicacion = [None]*l
        reviews = [None]*l
        marca = [None]*l
        modelo = [None]*l
        descripcionExt = [None]*l
        for i in range(l):
            flag =  True # una bandera para re intentar hasta un evento
            intento = 1  # una varible para saber cuantas veces se ha intentado extraer una informacion
            while(flag):
                try:
                    print(l)
                    time.sleep(te())
                    items =  web.find_elements_by_class_name(classname)
                    time.sleep(1)
                    #time.sleep(te())
                    items[i].click()        
                    try:
                        descrip[i] = web.find_element_by_class_name('item-title').text
                    except:
                        print('')
                    try:
                        price[i] = web.find_element_by_class_name('price-tag-fraction').text
                    except:
                        print('')
                    try:
                        envio[i] = web.find_element_by_class_name('shipping-method-title').text
                    except:
                        print('')
                    try:
                        ciudad[i] = web.find_element_by_class_name('gray').text
                    except:
                        print('')
                    try:
                        otro1[i] = web.find_element_by_class_name('variations-title').text
                    except:
                        print('')
                    try:
                        otro2[i] = web.find_element_by_class_name('variations-attribute').text
                    except:
                        print('')
                    try:
                        benef[i] = web.find_element_by_class_name('benefit__text').text
                    except:
                        print('')
                    try:
                        disponibles[i] = web.find_element_by_class_name('dropdown-quantity-available').text
                    except:
                        print('')
                    try:
                        stock[i] = web.find_element_by_class_name('stock-information--available--title').text
                    except:
                        print('')
                    try:
                        official[i] = web.find_element_by_class_name('disclaimer').text
                    except:
                        print('')
                    try:
                        ventas[i] = web.find_element_by_class_name('reputation-relevant').text
                    except:
                        print('')
                    try:
                        infoVentas[i] = web.find_element_by_class_name('reputation-relevant').text
                    except:
                        print('')
                    try:
                        atencion[i] = web.find_element_by_class_name('highlight-info').text
                    except:
                        print('')
                    try:
                        entrega[i] = web.find_element_by_class_name('reputation-relevant').text
                    except:
                        print('')
                    try:
                        vendidos[i] = web.find_element_by_class_name('vip-title-info').text
                    except:
                        print('')
                    try:
                        nopiniones[i] = web.find_element_by_class_name('average-legend').text
                    except:
                        print('') 
                    try:
                        calificacion[i] = web.find_element_by_id('reviewFullStar0').get_attribute("value")
                    except:
                        print('')
                    try:
                        vendedor[i] = web.find_element_by_class_name('card-subtitle').text
                    except:
                        print('')
                
                    try:
                        ubicacion[i] = web.find_element_by_class_name('card-description').text
                    except:
                        print('')
                    try:
                        reviews[i] = web.find_element_by_class_name('reviews_percent_value').text
                    except:
                        print('')
                    try:
                        marca[i] = web.find_elements_by_class_name('specs-list')[0].text
                    except:    
                        print('')
                    try:
                        modelo[i] = web.find_elements_by_class_name('specs-list')[1].text
                    except:    
                        print('') 
                    try:
                        descripcionExt[i] = web.find_element_by_class_name('item-description__text').text
                    except:
                        print('')
                    flag = False
                    print(str(i) + 'ok') 
                except:
                    intento = intento + 1
                    if intento > 2:
                        flag = False
                #print(str(i) + 'ok') 
                
                time.sleep(te())
                #time.sleep(te()) 
                web.back()
          
        d =  list(zip(descrip,price,envio,ciudad,otro1,otro2,benef,disponibles,stock,official,ventas,infoVentas,atencion,entrega,ventas,nopiniones,calificacion,vendedor,ubicacion,reviews,marca,modelo,descripcionExt))
        df = pd.DataFrame(data=d)    
        return df
    
    
    # leemos la primera paginacion de articulos       
    df = rec_items(claseObjetoBuscado)  
    # ponemos nombres a las columnas
    
    df.columns = ['descrip', 'price' , 'envio' , 'ciudad' , 'otro1' , 'otro2' , 'benef' , 'disponibles' , 'stock' , 'official' , 'ventas' , 'infoVentas' , 'atencion' , 'entrega' , 'ventas' , 'nopiniones' , 'calificacion' , 'vendedor' , 'ubicacion' , 'reviews' , 'marca' , 'modelo' , 'descripcionExt' ]
    
    
    
         
    #hacemos la primera paginacion           
    paginacion = web.find_elements_by_class_name('andes-pagination__arrow-title')
    paginacion[0].click()
    df.append
    #descargamos la paginaciones intermedias
    while web.find_element_by_class_name('andes-pagination__link'): 
        df1 = rec_items(claseObjetoBuscado)
        df1.columns = ['descrip', 'price' , 'envio' , 'ciudad' , 'otro1' , 'otro2' , 'benef' , 'disponibles' , 'stock' , 'official' , 'ventas' , 'infoVentas' , 'atencion' , 'entrega' , 'ventas' , 'nopiniones' , 'calificacion' , 'vendedor' , 'ubicacion' , 'reviews' , 'marca' , 'modelo' , 'descripcionExt' ]
        df.index = list(df.index)    
        df = pd.concat([df,df1],ignore_index =True)
        
        df.to_csv('jaime.csv')
        df.to_excel('jaime.xlsx')
        time.sleep(3)
        paginacion = web.find_elements_by_class_name('andes-pagination__arrow-title')
        time.sleep(3)
        paginacion[1].click()
        df.to_csv(nombre + '.csv')
        df.to_excel( nombre + '.xlsx')
                
    
    #descargamos la ultima paginacion
    df1 = rec_items(claseObjetoBuscado)
    df = pd.concat(df,df1)
    type(df.index)
    type(df1.index)
    ## Nombre del archivo de salida
    
    df.to_csv(nombre + '.csv')
    df.to_excel( nombre + '.xlsx')
                
    
            
        
    print(df)           



#aqui se corre el programa
    
# rowItem    
    
buscar()