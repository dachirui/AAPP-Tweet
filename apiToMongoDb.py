#!/usr/bin/python
#-*- encoding: utf-8 -*-

import pymongo
import twitter
import time
import tweepy
import json
import unicodecsv as csv

consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)   
# Conexión a la API
api = tweepy.API(auth)
    
# Procedimiento para mostrar los datos de cada follower en Twitter. 
def GetFollowersInformation(user, api):
    sleeptime = 4
    pages = tweepy.Cursor(api.followers, screen_name = user, count=200).pages()


    while True:
        try:
            page = next(pages)
            time.sleep(sleeptime)
        except tweepy.TweepError:
            print("Debemos esperar...")
            time.sleep(60*15) 
            page = next(pages)
        except StopIteration:
            break
        for user in page:
           # Generamos los documentos con los datos obtenidos.
            document = { 'screen_name': user.screen_name, 'followers_count':user.followers_count, 'friends_count': user.friends_count, 'statuses_count': user.statuses_count, 'location':user.location, 'verified':user.verified, 'lang':user.lang}
           
            # Llamada al procedimiento para insertar los documentos
            file_to_mongodb(document);
           
#funcion para poblar la base de datos
def file_to_mongodb(files):
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    db = connection.tweetsSINF
    record = db.followersYprivado
    record.insert(files)
    print("Registro insertado correctamente")
    print("Creando fichero CSV...")
    dbToCsv()
    print("Fichero creado en el directorio")
    
#funcion que crea csv a partir de la base de datos
def dbToCsv():
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    db = connection.tweetsSINF
    with open('SeguidoresConPrivado.csv', 'w') as outfile:
      fieldnames = ['nombre', 'seguidores', 'amigos', 'tweets', 'localizacion', 'verificado','idioma']
      writer = csv.DictWriter(outfile, delimiter=';', fieldnames=fieldnames, encoding="UTF-8")
      writer.writeheader()

      for data in db.followersPrueba.find():
        writer.writerow({
          'nombre': json.dumps(data['screen_name']), 
          'seguidores': data['followers_count'], 
          'amigos': data['friends_count'],
          'tweets': data['statuses_count'],
          'localizacion': json.dumps(data['location']),
          'verificado': data['verified'],
          'idioma': json.dumps(data['lang'])
        })

      outfile.close()               

GetFollowersInformation('AjuntamentVLC', api)           
