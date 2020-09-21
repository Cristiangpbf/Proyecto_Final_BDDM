
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "Ok7GRYYssNsfY9lXR8CIe3xeJ"
csecret = "5YrZnShw3g93HAVyASSlyrAER8ok0Sae1gU3mZXBTBxCXyDpUD"
atoken = "1288264585519288320-uSIAbWH8d7zossuXMpN87FmMeZeUS4"
asecret = "804vnKpAWdmdl150dEb7IknuPbKsjkGx7wiBqb3LJ2XqY"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('tweets_ecuador')
except:
    db = server['tweets_ecuador']
    

#twitterStream.filter(track=['Guillermo Lasso','Fabricio Correa','Gustavo Larrea', 'Lucio Gutiérrez', 'Lucio Gutierrez', 'Andrés Aráuz', 'Andres Arauz', 'Guillermo Celi', 'Yaku Pérez', 'Yaku Perez', 'César Montúfar', 'Cesar Montufar', 'Isidro Romero', 'Gerson Almeida', 'Ximena Peña', 'Paúl Carrasco', 'Paul Carrasco', 'Esteban Quirola', 'Miguel Salem Kronfle', 'Cristina Reyes', 'Xavier Hervas', 'José Freile', 'Juan Fernando Velasco', 'Washington Pesántez', 'Elecciones Ecuador','Creo', 'Justicia Social','Democracia Si', 'Partido Sociedad Patriótica','Centro Democrático','Unión por la esperanza','Union por la esperanza','SUMA','suma','Pachakutik','Concertación','avanza','Ecuatoriano Unido','Alianza país','Juntos podemos','Libertad es pueblo','Fuerza Ecuador','Social Cristiano','Izquierda Democratica','Izquierda Democrática','Construye','Unión Ecuatoriana','Union Ecuatoriana','Elecciones2020'])

'''===============LOCATIONS=============='''    
#Manta
twitterStream.filter(locations=[-92.21,-5.02,-75.19,1.95]) 
