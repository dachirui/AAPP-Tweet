#!/usr/bin/python
#-*- encoding: utf-8 -*-

import tweepy
import time
import unicodecsv as csv

consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)   
# Conexión a la API
api = tweepy.API(auth)

listIzq = ['eldiarioes','publico_es','_infoLibre']
listCentroIzq = ['el_pais','ElHuffPost','El_Plural']
listCentro = ['elmundoes','20m','elespanolcom']
listCentroDer = ['elimparcialcom','elEconomistaes','gaceta_es']
listDer = ['expansioncom','abc_es','elconfidencial']

# Procedimiento para obtener las cuentas de periodicos a las que sigue y calcular su ideología 
def GetFriendsInformation(user, api, writer, i, exampleData):
    sleeptime = 5
    pages = tweepy.Cursor(api.friends, screen_name = user, count=200).pages()
    siguePeriodico = False
    listaPeriodicos = []
    eldiario = 0
    publico = 0
    infoLibre = 0
    elPais = 0
    Elhuff = 0
    elPlural = 0
    elMundo = 0
    minutos = 0
    elespanol = 0
    elImparcial = 0
    elEconmista = 0
    laGaceta = 0
    expansion = 0
    abc = 0
    confidencial = 0
    grupoIzquierda = 0
    grupoCentroIzquierda = 0
    grupoCentro = 0
    grupoCentroDerecha = 0
    grupoDerecha = 0
    equilibrio = "no"
    balanceo = "si"
    saturacion = ""
    ponderacionExtrema = 0
    ponderacionCentral = 0
    countExtremo = 0
    countCentro = 0
    
    while True:
        try:
            print("Continuamos...")
            page = next(pages)
            time.sleep(sleeptime)
        except tweepy.TweepError as e: #excepcion por si es usuario privado
            if (e.reason) == "Not authorized.":
                print("Privado, saltamos...")                
                writer.writerow({ 
                        'nombre': user,
                        'expansion': expansion,
                        'abc': abc,
                        'el Confidencial': confidencial,
                        'el Imparcial': elImparcial,
                        'el Economista': elEconmista,
                        'la Gaceta': laGaceta,
                        'el Mundo': elMundo,
                        '20 Minutos': minutos,
                        'el Espanol': elespanol,
                        'el Pais': elPais,
                        'El Huffington Post': Elhuff,
                        'el Plural': elPlural,
                        'publico': publico,
                        'infoliblre': infoLibre,
                        'eldiario.es': eldiario,
                        'Equilibrio': '',
                        'Balanceo': '',
                        'Saturacion': ''
                })
                break
            else:        
                print("Debemos esperar...") #excepcion si es por exceso de llamadas
                time.sleep(60*15) 
                page = next(pages)    
        except StopIteration:               #excepción si se han revisado todas la cuentas que sigue || calcula dieta
                
            #determinar saturacion
            if siguePeriodico:
                countSaturacion = grupoIzquierda + grupoCentroIzquierda + grupoCentro + grupoCentroDerecha + grupoDerecha
                if countSaturacion >= 10:
                    saturacion = "polisaturada"
                elif countSaturacion >= 6 and countSaturacion <=9:
                    saturacion = "saturada"
                elif countSaturacion <= 5:
                    saturacion = "monosaturada"
            
            #determinar equilibrio
            if siguePeriodico:
                if grupoIzquierda > 0 and grupoCentroIzquierda > 0 and grupoCentro > 0 and grupoCentroDerecha > 0 and grupoDerecha > 0:
                    equilibrio = "si"
                elif grupoIzquierda + grupoCentroIzquierda > grupoCentroDerecha + grupoDerecha:
                    equilibrio = "no"
                elif grupoIzquierda + grupoCentroIzquierda < grupoCentroDerecha + grupoDerecha:
                    equilibrio = "no"
            else:
                equilibrio = ""
            #determinar balanceo
            countExtremo = grupoIzquierda + grupoDerecha
            countCentro = grupoCentroIzquierda + grupoCentroDerecha
            if siguePeriodico:
                if grupoIzquierda + grupoCentroIzquierda > grupoCentroDerecha + grupoDerecha:
                    balanceo = "Desbalance a la izquierda"
                elif grupoIzquierda + grupoCentroIzquierda < grupoCentroDerecha + grupoDerecha:
                    balanceo = "Desbalance a la derecha"
                elif grupoIzquierda == grupoDerecha:
                    if countExtremo > 0:
                        balanceo = "si"
                elif grupoCentroIzquierda == grupoCentroDerecha:
                    if countCentro > 0:
                        balanceo = "si"
            else:
                balanceo = ""
            
            for x in listaPeriodicos:       #marca periodicos leídos, para generar CSV
                if x == 'eldiarioes':
                    eldiario = 1                
                elif x == 'publico_es':
                    publico = 1
                elif x == '_infoLibre':
                    infoLibre = 1
                elif x == 'el_pais':
                    elPais = 1
                elif x == 'ElHuffPost':
                    Elhuff = 1
                elif x == 'El_Plural':
                    elPlural = 1
                elif x == 'elmundoes':
                    elMundo = 1
                elif x == '20m':
                    minutos = 1
                elif x == 'elespanolcom':
                    elespanol = 1
                elif x == 'elimparcialcom':
                    elImparcial = 1
                elif x == 'elEconomistaes':
                    elEconmista = 1
                elif x == 'gaceta_es':
                    laGaceta = 1
                elif x == 'expansioncom':
                    expansion = 1
                elif x == 'abc_es':
                    abc = 1
                elif x == 'elconfidencial':
                    confidencial = 1
            
            writer.writerow({ 
                    'nombre': user,
                    'expansion': expansion,
                    'abc': abc,
                    'el Confidencial': confidencial,
                    'el Imparcial': elImparcial,
                    'el Economista': elEconmista,
                    'la Gaceta': laGaceta,
                    'el Mundo': elMundo,
                    '20 Minutos': minutos,
                    'el Espanol': elespanol,
                    'el Pais': elPais,
                    'El Huffington Post': Elhuff,
                    'el Plural': elPlural,
                    'publico': publico,
                    'infoliblre': infoLibre,
                    'eldiario.es': eldiario,                    
                    'Equilibrio': equilibrio,
                    'Balanceo': balanceo,
                    'Saturacion': saturacion
            })
            break
        for friend in page:
             friendName = friend.screen_name             
             if friendName in listIzq:
                siguePeriodico = True
                grupoIzquierda += 1
                ponderacionExtrema -= 2
                listaPeriodicos.append(friendName)
             elif friendName in listCentroIzq:
                siguePeriodico = True
                grupoCentroIzquierda += 1
                ponderacionCentral -= 1
                listaPeriodicos.append(friendName)
             elif friendName in listCentro:
                siguePeriodico = True
                grupoCentro += 1
                listaPeriodicos.append(friendName)
             elif friendName in listCentroDer:
                siguePeriodico = True
                grupoCentroDerecha += 1
                ponderacionCentral += 1
                listaPeriodicos.append(friendName)
             elif friendName in listDer:
                siguePeriodico = True
                grupoDerecha += 1
                ponderacionExtrema += 2
                listaPeriodicos.append(friendName)
             else:
                pass            

#Función que va leyendo los usuarios del csv, auxiliar, no se utiliza en el proceso
def readCsv():
    usersFile = open('example.csv')
    exampleReader = csv.reader(usersFile)
    exampleData = list(exampleReader)
    i = 1
    while True:
        try:
            print(exampleData[i][0])
            i += 1
        except IndexError:
            print("Ya no hay más usuarios")
            break
            
#Funcion que accederá a cada usuario de un csv. 
#Llamará API Twitter para obtener amigos(periodicos) de usuario.
#matching amigos(periodicos) con lista
#crea csv: nombre, [periodico1,periodico2,...], ideologia 
#{nombre = string; periodicoN = nombre del periodico; ideologia = string(1 termino de los 5)}

def cuentaIdeologia():
    usersFile = open('Muestra.csv')
    exampleReader = csv.reader(usersFile)
    exampleData = list(exampleReader)
    with open('resultadosDefinitivos.csv', 'w') as outfile:
        fieldnames = ['nombre', 'expansion', 'abc','el Confidencial','el Imparcial','el Economista','la Gaceta','el Mundo','20 Minutos','el Espanol','el Pais','El Huffington Post','el Plural','publico','infoliblre','eldiario.es','Equilibrio','Balanceo','Saturacion']
        writer = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames, encoding="UTF-8")
        writer.writeheader()
        i = 1
        private = 'True'
        while True:
            try:                            
                GetFriendsInformation(exampleData[i][0], api, writer, i, exampleData)
                i += 1
            except IndexError:
                print("Ya no hay más usuarios")
                break
        outfile.close()
        
cuentaIdeologia()            
