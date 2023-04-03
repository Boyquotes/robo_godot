# Servidor 

from config import db # Conexão com banco de dados
from models.Position import Position # Modelo de posições
from flask import Flask, render_template, request # Framework web
from flask_cors import CORS # Permite acesso de outros domínios

# Cria o servidor web
app = Flask(__name__)
CORS(app) 

@app.route('/') # Rota inicial do servidor, retorna a página index.html
def index():
    return render_template('index.html')

# Retorna todas as posições cadastradas no banco de dados em uma lista de objetos json
@app.route('/api/position', methods=['GET'])
def api_positions():
    return {
        'positions': [position.return_json() for position in db.session.query(Position).all()]
    }

# Retorna uma posição específica cadastrada no banco de dados em um objeto json
@app.route('/api/position/<int:id>') 
def api_position(id):
    return db.session.query(Position).filter(Position.id == id).first().return_json()

# Retorna a última posição cadastrada no banco de dados em um objeto json
@app.route('/api/position/last') 
def api_position_last():
    return db.session.query(Position).order_by(Position.id.desc()).first().return_json()

# Adciona uma nova posição no banco de dados
@app.route('/api/position', methods=['POST']) 
def api_position_post():
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

# Atualiza uma posição no banco de dados
@app.route('/api/position/<int:id>', methods=['PUT']) # Rota API
def api_position_put(id):
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

# Deleta uma posição no banco de dados
@app.route('/api/position/<int:id>', methods=['DELETE']) # Rota API
def api_position_delete(id):
    position = db.session.query(Position).filter(Position.id == id).first()
    db.session.delete(position)
    db.session.commit()
    return position.return_json()

# Inicia o servidor web
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) # Roda também na rede local
