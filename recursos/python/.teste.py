# AINDA
# EM
# TESTES
# :)
import pymongo, json
from bson.json_util import dumps
from datetime import datetime

database = pymongo.MongoClient("mongodb://127.0.0.1:27017/")["suite"]

def getHoje():
    hoje = datetime.today().strftime('%Y-%m-%d')
    return hoje

def getMes():
    mes = datetime.today().strftime('%Y-%m')
    return mes

atendimentos = (database["atendimentos"].find())
print(atendimentos)