# AINDA
# EM
# TESTES
# :)
import pymongo, json
from bson.json_util import dumps

database = pymongo.MongoClient("mongodb://127.0.0.1:27017/")["suite"]

data = {}

## usuarios ativos (nome e online)
def getUsuarios():
    cursor = (database['usuarios'].find({'status': 'A'},{'nome','online'}))
    list_cur = list(cursor)
    data_string = dumps(list_cur)
    data['usuarios'] = json.loads(data_string);
    # end

## departamentos ativos (status)
def getDepartamentos():
    cursor = (database["departamentos"].find({'status': "A"},{'status','nome'}))
    list_cur = list(cursor)
    data_string = dumps(list_cur)
    data['departamentos'] = json.loads(data_string);
    # end

## atendimentos 'aguardando' ou 'em atendimento'
def getAtendimentos():
    cursor = (database['atendimentos'].find({'$or':[{'status':'AG'},{'status':'EA'}]},{'status','setor','id_atendente','canal_id','canal'}))
    list_cur = list(cursor)
    data_string = dumps(list_cur)
    data['atendimentos'] = json.loads(data_string);
    # end

## canai de atendimetos
def getCanais():
    cursor = (database['canal_comunicacaos'].find({'status':'A'},{'nome'}))
    list_cur = list(cursor)
    data_string = dumps(list_cur)
    data['canais'] = json.loads(data_string);
    # end

getUsuarios()
getDepartamentos()
getAtendimentos()
getCanais()

print(data['atendimentos'])