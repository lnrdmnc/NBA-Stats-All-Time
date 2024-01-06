from flask_pymongo import PyMongo
from pymongo import MongoClient


from pymongo import MongoClient

# Configura la connessione a MongoDB
client = MongoClient('mongodb://localhost:27017')  # Sostituisci con l'indirizzo del tuo database

# Seleziona il database e la collezione
database = client['NBA_Players']  # Sostituisci con il nome del tuo database
collection= database['NBA players']  # Sostituisci con il nome della tua collezione

# Recupera tutti i documenti nella collezione
documenti = collection.find()

# Stampa i documenti
for documento in documenti:
    print(documento)

# Chiudi la connessione a MongoDB
client.close()


""""
# Configurazione del database MongoDB
# Definizione dell'URI per la connessione al database MongoDB. In questo caso, il database è in esecuzione localmente sulla porta 27017.
mongo_uri = 'mongodb://localhost:27017'

# Creazione di un oggetto MongoClient utilizzando l'URI definito sopra. Questo oggetto viene utilizzato per stabilire una connessione al database MongoDB.
client = MongoClient(mongo_uri)

# Seleziona il database 'NBA_Players' dalla connessione. Questo istruisce il client a utilizzare il database specificato per le operazioni successive.
db = client['NBA_Players']

# Seleziona la collezione 'NBA players' dal database. La collezione è dove vengono memorizzati i documenti all'interno del database.
# In questo caso, la collezione contiene i dati dei giocatori NBA.
collection = db['NBA players']
print(db)
"""