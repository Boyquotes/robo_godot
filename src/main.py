# Programa principal que mostra os jogos cadastrados no banco de dados no console, numa rota API e na página inicial do site

from src.config import db # Conexão com banco de dados
from src.models.Position import Position # Modelo de tabela de jogos
from flask import Flask, render_template, request # Framework web
from flask_cors import CORS

# Cria o servidor web
app = Flask(__name__)
CORS(app)

@app.route('/') # Rota inicial
def index():
    return render_template('index.html')

@app.route('/api/position', methods=['GET']) # Rota API
def api_positions():
    # Retorna uma lista com os jogos cadastrados no banco de dados
    return {
        'positions': [position.return_json() for position in db.session.query(Position).all()]
    }

@app.route('/api/position/<int:id>') # Rota API
def api_position(id):
    # Retorna um jogo específico cadastrado no banco de dados
    return db.session.query(Position).filter(Position.id == id).first().return_json()

@app.route('/api/position/last') # Rota API
def api_position_last():
    # Retorna o último jogo cadastrado no banco de dados
    return db.session.query(Position).order_by(Position.id.desc()).first().return_json()

@app.route('/api/position', methods=['POST']) # Rota API
def api_position_post():
    # Cria um novo jogo no banco de dados
    position = Position(
        x=request.json['x'],
        y=request.json['y'],
        z=request.json['z'],
        r=request.json['r'],
        j1=request.json['j1'],
        j2=request.json['j2'],
        j3=request.json['j3'],
        j4=request.json['j4']
    )
    db.session.add(position)
    db.session.commit()
    return position.return_json()


@app.route('/api/position/<int:id>', methods=['PUT']) # Rota API
def api_position_put(id):
    # Atualiza um jogo no banco de dados
    position = db.session.query(Position).filter(Position.id == id).first()
    position.x = request.json['x']
    position.y = request.json['y']
    position.z = request.json['z']
    position.r = request.json['r']
    position.j1 = request.json['j1']
    position.j2 = request.json['j2']
    position.j3 = request.json['j3']
    position.j4 = request.json['j4']
    db.session.commit()
    return position.return_json()

@app.route('/api/position/<int:id>', methods=['DELETE']) # Rota API
def api_position_delete(id):
    # Deleta um jogo no banco de dados
    position = db.session.query(Position).filter(Position.id == id).first()
    db.session.delete(position)
    db.session.commit()
    return position.return_json()

# Inicia o servidor web
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
