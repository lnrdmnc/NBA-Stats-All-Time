from flask import Flask, render_template, request, jsonify
from query_manager import query_delete
from query_manager import query_update_age
from query_manager import query_insert_giocatore
from query_manager import query_update_height_weight
from query_manager import query_by_country_college
from query_manager import query_by_country_college_team
from query_manager import query_by_ast_reb
from query_manager import query_by_ast_reb_pts

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/query', methods=['GET'])
def query():
    return render_template('query.html')



@app.route('/query_delete', methods=['GET','POST'])
def handle_query_delete():
    if request.method == 'POST':
        id_oggetto = request.form['id_oggetto']
        
        risultato=query_delete(id_oggetto)
    return render_template('risultato_delete.html', id_oggetto=id_oggetto)



@app.route('/query_update_age', methods=['POST'])
def handle_query_update_age():
    nome_oggetto = {}
    nuovo_age={}
    nome_oggetto = request.form['nome_oggetto']
    nuovo_age= request.form['nuovo_age']
    oggetto=query_update_age(nome_oggetto,nuovo_age)
    return render_template('query_update_age.html', oggetto=oggetto)


@app.route('/query_insert', methods=['POST'])
def handle_query_insert_giocatore():
    nuovo_oggetto = {}
    

    nuovo_oggetto["id"] = request.form.get('id')
    nuovo_oggetto["player_name"] = request.form.get('player_name')
    nuovo_oggetto["team_abbreviation"] = request.form.get('team_abbreviation')
    nuovo_oggetto["age"] = request.form.get('age')
    nuovo_oggetto["player_height"] = float(request.form.get('player_height'))
    nuovo_oggetto["player_weight"] = float(request.form.get('player_weight'))
    nuovo_oggetto["college"] = request.form.get('college')
    nuovo_oggetto["country"] = request.form.get('country')
    nuovo_oggetto["draft_year"] = int(request.form.get('draft_year'))
    nuovo_oggetto["draft_round"] = int(request.form.get('draft_round'))
    nuovo_oggetto["draft_number"] = int(request.form.get('draft_number'))
    nuovo_oggetto["gp"] = int(request.form.get('gp'))
    nuovo_oggetto["pts"] = float(request.form.get('pts'))
    nuovo_oggetto["reb"] = float(request.form.get('reb'))
    nuovo_oggetto["ast"] = float(request.form.get('ast'))
    nuovo_oggetto["net_rating"] = float(request.form.get('net_rating'))
    nuovo_oggetto["oreb_pct"] = float(request.form.get('oreb_pct'))
    nuovo_oggetto["dreb_pct"] = float(request.form.get('dreb_pct'))
    nuovo_oggetto["usg_pct"] = float(request.form.get('usg_pct'))
    nuovo_oggetto["ts_pct"] = float(request.form.get('ts_pct'))
    nuovo_oggetto["ast_pct"] = float(request.form.get('ast_pct'))
    nuovo_oggetto["season"] = request.form.get('season')
    nuovo_oggetto["pst"] = request.form.get('pst')

    risultato=query_insert_giocatore(nuovo_oggetto)

    return render_template('query_insert.html', oggetto=risultato)



@app.route('/query_update_height_weight', methods=['POST'])
def handle_query_update_height_weight():
    nome_oggetto = {}
    nuovo_height={}
    nuovo_weight={}
    nome_oggetto = request.form['nome_oggetto']
    nuovo_height= request.form['nuovo_height']
    nuovo_weight= request.form['nuovo_weight']
    oggetto=query_update_height_weight(nome_oggetto,nuovo_height,nuovo_weight )
    return render_template('query_update_height_weight.html', oggetto=oggetto)



@app.route('/query_by_country_and_college', methods=['POST'])
def handle_query_by_country_and_college():
    
    country={}
    college={}
    country= request.form['country']
    college= request.form['college']
    oggetto=query_by_country_college(country, college )
    return render_template('query_by_country_and_college.html', oggetto=oggetto)


@app.route('/query_by_country_and_college_team', methods=['POST'])
def handle_query_by_country_and_college_team():
    
    country={}
    college={}
    team={}
    country= request.form['country']
    college= request.form['college']
    team= request.form['team']
    oggetto=query_by_country_college_team(country, college,team )
    return render_template('query_by_country_and_college_team.html', oggetto=oggetto)


@app.route('/query_by_ast_reb', methods=['POST'])
def handle_query_by_ast_reb():
    
    ast={}
    reb={}
    ast= float(request.form.get('ast'))
    reb= float(request.form.get('reb'))
    oggetto=query_by_ast_reb(ast,reb )
    return render_template('query_by_ast_reb.html', oggetto=oggetto)

@app.route('/query_by_ast_reb_pts', methods=['POST'])
def handle_query_by_ast_reb_pts():
    
    ast={}
    reb={}
    pts={}
    ast=float(request.form.get('pts'))
    reb = float(request.form.get('reb'))
    pts = float(request.form.get('ast'))
    oggetto=query_by_ast_reb_pts(ast,reb,pts)
    return render_template('query_by_ast_reb_pts.html', oggetto=oggetto)
    

if __name__ == '__main__':
    app.run(debug=True)
