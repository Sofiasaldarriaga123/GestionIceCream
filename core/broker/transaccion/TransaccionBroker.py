####################################

# TransaccionBroker:

####################################

from http import client
from typing import Collection
from socket import gaierror
from fastapi.datastructures import URL
import pymongo
import json

####################################

from pymongo import MongoClient
from core.domain.transaccion.transaccionModel import ModeloTransaccion

####################################

class BrokerTransaccion:
    
    async def ingresar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Sofias.135>@cluster0.4ysq7er.mongodb.net/icecream?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["icecream"]
        col = db["Transaccion"]
        data = json.dumps(transaccion)
        resultado = col.insert_one()
        transaccion.Resultado = resultado.insert_id
        

        client.close() 
        return transaccion
		
    async def modificar_transaccion(self, transaccion: ModeloTransaccion | None = None):
        URL = "mongodb+srv://dbauser:<Sofias.135>@cluster0.4ysq7er.mongodb.net/icecream?retryWrites=true&w=majority"
        client = pymongo.MongoClient(URL)
        db = client["icecream"]
        col = db["Transaccion"]
        
        for x in col.find():
            print(x)       
        return transaccion
	
    async def retirar_transaccion(self, transaccion: ModeloTransaccion | None = None):
         URL = "mongodb+srv://dbauser:<Sofias.135>@cluster0.4ysq7er.mongodb.net/icecream?retryWrites=true&w=majority"
         client = pymongo.MongoClient(URL)
         db = client["icecream"]
         col = db["Transaccion"]
        
         for x in col.find():
             print(x)   
         return transaccion

    async def consultar_transaccion(self, transaccion: ModeloTransaccion | None = None):
         URL = "mongodb+srv://dbauser:<Sofias.135>@cluster0.4ysq7er.mongodb.net/icecream?retryWrites=true&w=majority"
         client = pymongo.MongoClient(URL)
         db = client["icecream"]
         col = db["Transaccion"]


         for x in col.find():
             print(x)    
         return transaccion
    
    async def consultarid_transaccion(self, transaccion: ModeloTransaccion | None = None):
          URL = "mongodb+srv://dbauser:<Sofias.135>@cluster0.4ysq7er.mongodb.net/icecream?retryWrites=true&w=majority"
          client = pymongo.MongoClient(URL)
          db = client["icecream"]
          col = db["Transaccion"]
        
          for x in col.find():
              print(x)   
          return transaccion

##########################################