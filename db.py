from pymongo import MongoClient
from pymongo.collection import Collection
from mongo_db_config import mongodb_config

MONGO_URI = f"mongodb://{mongodb_config['HOST']}:{mongodb_config['PORT']}/"
DB_NAME = mongodb_config["DB_NAME"]
COLLECTION_NAME = mongodb_config['COLLECTION_NAME']

def get_collection() -> Collection | None:
    
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        return collection
    
    except Exception as er:
        print("\n--- ERRO CRÍTICO ---")
        print(f"Não foi possível conectar ao MongoDB. Erro: {er}")
        print("Certifique-se de que o MongoDB Server (ou o Compass) está rodando.")
        return None