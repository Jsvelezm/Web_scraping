# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:23:23 2020

@author: jsvel
"""

#cargando las librerias que necesito

import pandas as pd # esta libreria es para manejar bases de datos
import numpy as np # esta libreria es para hacer cuentas
import re  # esta libreria para trabajar expersiones regulares


# leer la base

base =  pd.read_csv("C:/Users/jsvel/Google Drive/Desarrollos/WebScraping/Descargar datos Mecado libre/botines.csv")
base.columns

# Empezar a arreglar los datos

dispo = base['disponibles'] # esta es la variable que tiene la descripcion del productod


dispo[0] # trae el valor de lo que este en la primera columna de dispo

nobs = len(dispo)

#for i in range(nobs):
#    c = re.sub("\(","",dispo[i])
#    c = re.sub("\)","",c)
#    c = re.sub(" disponibles","",c)
#    c = float(c)
#    dispo[i] = c

var = [] # creando una nueva variable para guardar los nuevos datos

# ten mucho cuidado con las tabulaciones y los espacios
for i in range(nobs):
    try: # intenta hacer lo que este acontinuación si no se puede hacer hace lo que esté en except
        c = re.sub("[^0-9]","",dispo[i])
        c = float(c)
        var.append(c)
    except: # si no lo logra pasa a 
        var.append(0)
   

#def jaimito(x):
#    for i in range(nobs):
#        try:
#            c = re.sub("[^0-9]","",x[i])
#            c = float(c)
#            var.append(c)
#        except:
#            var.append(0)
#    return var        

#jaimito(base['nopiniones'])

len(var) == nobs


base['disponibles'] = var

base.to_excel("diana.xlsx")


# una forma elegante de hacerlo

#aqui extraemos todo lo que es texto
str = "h3110 23 cat 444.4 rabbit 11 2 dog"
[int(s) for s in str.split() if s.isdigit()]
