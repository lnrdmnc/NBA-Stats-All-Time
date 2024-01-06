from bson import ObjectId
from pymongo import MongoClient
import pymongo


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


#query rimuove oggetto in base ad id
def query_delete(id_oggetto):

    # Crea la query per la cancellazione dell'oggetto
    query = {
        "_id": ObjectId(id_oggetto)
    }

    # Esegui la query di cancellazione sul database MongoDB
    risultato = collection.delete_one(query)




#query  modifica degli anni di un giocatore scelta dall'utente in base al nome
def query_update_age(nome_oggetto,nuovo_age):
    # Chiedi all'utente il nome dell'oggetto e il nuovo prezzo
    # Esegui la query di aggiornamento
    risultati = collection.update_many(
        {'player_name': nome_oggetto},
        {"$set": {"age": nuovo_age}}
    )
    
    oggetti_modificati = collection.find_one({'player_name': nome_oggetto})

    return oggetti_modificati


#query modifica altezza e peso di un giocatore scelta dall'utente in base al nome
def query_update_height_weight(nome_oggetto,nuovo_height,nuovo_weight):
    # Chiedi all'utente il nome dell'oggetto e il nuovo prezzo
    # Esegui la query di aggiornamento
    risultati = collection.update_many(
        {'player_name': nome_oggetto},
        {"$set": {"player_height": nuovo_height, "player_weight": nuovo_weight}}
    )
    
    oggetti_modificati = collection.find_one({'player_name': nome_oggetto})

    return oggetti_modificati
 
#Inserisce un nuovo giocatore 
def query_insert_giocatore(nuovo_oggetto):
    collection.insert_one(nuovo_oggetto)
    oggetto_inserito = collection.find_one({"id": nuovo_oggetto["id"]})

    return oggetto_inserito


 # Rappresenta i giocatori con quella città e college
def query_by_country_college(country,college):
    # Crea la query per filtrare gli oggetti
    query = {
        "country": country,
        "college": college
    }

    # Esegui la query sul database MongoDB
    risultati = collection.find(query)

    # Restituisci i risultati come lista di oggetti
    return risultati


 # Rappresenta i giocatori con quella città e college e team
def query_by_country_college_team(country,college,team):
    # Crea la query per filtrare gli oggetti
    query = {
        "country": country,
        "college": college,
        "team_abbreviation":team
             }

    # Esegui la query sul database MongoDB
    risultati = collection.find(query)

    # Restituisci i risultati come lista di oggetti
    return risultati

 # Rappresenta i giocatori con quella assist e rimbalzo
def query_by_ast_reb(ast,reb):
    # Crea la query per filtrare gli oggetti
    query = {
        "ast": ast,
        "reb": reb
             }

    # Esegui la query sul database MongoDB
    risultati = collection.find(query)

    # Restituisci i risultati come lista di oggetti
    return risultati
    

 # Rappresenta i giocatori con quella assist, rimbalzo e punti
def query_by_ast_reb_pts(ast,reb,pts):
    # Crea la query per filtrare gli oggetti
    query = {
        "ast": ast,
        "reb": reb,
        "pts": pts
             }

    # Esegui la query sul database MongoDB
    risultati = collection.find(query)

    # Restituisci i risultati come lista di oggetti
    return risultati
    

""""


def query(name, surname):
    def simulate_draft_lottery():
        # Copia la lista delle squadre partecipanti
        remaining_teams = team_abbreviations.copy()

        # Effettua la draft lottery per assegnare le posizioni di scelta alle squadre
        for round_num in range(1, 4):  # Simuliamo tre round di scelte
            for pick_number in range(1, 31):  # Simuliamo 30 scelte in ogni round
                selected_team = random.choice(remaining_teams)
                pick_info = {"draft_year": "2023-24", "draft_round": round_num, "draft_number": pick_number}
                draft_picks[selected_team] = draft_picks.get(selected_team, []) + [pick_info]

                # Rimuovi la squadra dalla lista delle squadre partecipanti se ha terminato le scelte
                if len(draft_picks[selected_team]) == 3:
                    remaining_teams.remove(selected_team)

     
    def generate_random_player_data(name, surname):
        return {
        "name": name,
        "surname": surname,
        "college": random.choice(["Duke", "Kentucky", "North Carolina", "Kansas", "UCLA"]),
        "country": "USA",
        "gp": 0.0,
        "pts": 0.0,
        "reb": 0.0,
        "ast": 0.0,
        "net_rating": 0.0,
        "oreb_pct": 0.0,
        "dreb_pct": 0.0,
        "usg_pct": 0.0,
        "ts_pct": 0.0,
        "ast_pct": 0.0,
        "draft_info": draft_picks.get(surname, [])
    }

    # Lista delle abbreviazioni delle squadre partecipanti alla draft lottery
    team_abbreviations = ["ATL", "BOS", "BKN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL",
                          "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

    # Dizionario per salvare le scelte effettuate durante la draft lottery
    draft_picks = {}

    # Simula la draft lottery e assegna le scelte alle squadre (se non è già stata eseguita)
    if not draft_picks:
        simulate_draft_lottery()

    # Genera i dati del giocatore draftato
    player_data = generate_random_player_data(name, surname)

    # Restituisci i dati del giocatore
    return player_data
"""

