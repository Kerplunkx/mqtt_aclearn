from pymongo import MongoClient
from datetime import datetime

client = MongoClient('URL')
db = client.admin
collection = db.comfort_votacion


def get_total_votes():
    '''
    Returns how many votes are registered on the current date
    '''
    current_date = datetime.utcnow()

    results = collection.find({
        "fecha": {
            "$gte": current_date.replace(hour=0, minute=0, second=0, microsecond=0),
            "$lte": current_date.replace(hour=23, minute=59, second=59, microsecond=999)
        }
    })
    return len(list(results))
