#!/usr/bin/python
#-*- encoding: utf-8 -*-
import unicodecsv as csv

#funcion que extrae muestra de usuarios
def cuenta():
    usersFile = open('SeguidoresAjuntamentLimpio.csv')
    exampleReader = csv.reader(usersFile)
    exampleData = list(exampleReader)
    count = 0
    i = 1
    with open('Muestra.csv', 'w') as outfile:
        fieldnames = ['nombre', 'seguidores', 'amigos', 'tweets', 'localizacion', 'verificado','idioma']
        writer = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames, encoding="UTF-8")
        writer.writeheader()
        while True:
                try:
                    #print(exampleData[i][0])
                    if int(exampleData[i][2]) > 254 and int(exampleData[i][2]) < 1016 and int(exampleData[i][3]) > 228 and int(exampleData[i][3]) < 912:
                        count += 1
                        writer.writerow({ 
                            'nombre': exampleData[i][0],
                            'seguidores': exampleData[i][1],
                            'amigos': exampleData[i][2],
                            'tweets': exampleData[i][3],
                            'localizacion': exampleData[i][4],
                            'verificado': exampleData[i][5],
                            'idioma': exampleData[i][6]                      
                        })
                        
                    i += 1
             
                except IndexError:
                    print("Ya no hay mas usuarios")
                    print(count)
                    break
                
cuenta()                
