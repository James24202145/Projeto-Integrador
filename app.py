import os
from flask import Flask, render_template, request  # Adicionado 'request' aqui
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração inteligente do caminho do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'projeto.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class PontoColeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    tipo_material = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f'<Ponto {self.nome}>'


# Rota inicial de teste
@app.route('/')
def index():
    return render_template('index.html')


# --- NOVA ROTA DE BUSCA ---
@app.route('/busca', methods=['GET', 'POST'])
def busca():
    resultados = []
    tipo_filtro = request.args.get('tipo')
    busca_texto = request.form.get('cep')  # O usuário pode digitar CEP ou Bairro aqui

    query = PontoColeta.query

    if tipo_filtro:
        query = query.filter(PontoColeta.tipo_material.contains(tipo_filtro))

    if busca_texto:
        # A mágica acontece aqui: ele procura o texto tanto no CEP quanto no Bairro
        query = query.filter(
            (PontoColeta.cep.contains(busca_texto)) |
            (PontoColeta.bairro.contains(busca_texto))
        )

    resultados = query.all()
    return render_template('busca.html', resultados=resultados)

@app.route('/importancia')
def importancia():
    return render_template('importancia.html')

if __name__ == '__main__':
    app.run(debug=True)