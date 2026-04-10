import os
from flask import Flask, render_template, request  # Adicionado 'request' aqui
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)

# Configuração inteligente do caminho do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'projeto.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class PontoColeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=True)
    bairro = db.Column(db.String(100), nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    cep = db.Column(db.String(20), nullable=True)
    tipo_material = db.Column(db.String(200), nullable=False)

    telefone1 = db.Column(db.String(20))
    telefone2 = db.Column(db.String(20))
    observacoes = db.Column(db.Text)  # Text permite textos mais longos que String

    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f'<Ponto {self.nome}>'


# Rota inicial de teste
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/busca', methods=['GET', 'POST'])
def busca():
    resultados = []
    # Pega o tipo de material via URL (ícones da index)
    tipo_filtro = request.args.get('tipo')

    # Pega o texto digitado no campo de busca (pode ser CEP, Bairro ou Cidade)
    busca_texto = request.form.get('cep')

    query = PontoColeta.query

    # 1. Filtro por Tipo de Material (se houver)
    if tipo_filtro:
        query = query.filter(PontoColeta.tipo_material.ilike(f"%{tipo_filtro}%"))

    # 2. Filtro por Localização (CEP, Bairro ou Cidade)
    if busca_texto:
        # 1. Remove qualquer caractere que não seja número (hífens, pontos, espaços)
        apenas_numeros = "".join(filter(str.isdigit, busca_texto))

        # 2. Pega apenas os 3 primeiros dígitos para a busca regional
        # Se o usuário digitou menos de 5, o Python pega o que tiver
        prefixo_cep = apenas_numeros[:3]

        query = query.filter(
            or_(
                PontoColeta.cep.like(f"{prefixo_cep}%"),  # Busca regional por CEP
                PontoColeta.bairro.ilike(f"%{busca_texto}%"),
                PontoColeta.cidade.ilike(f"%{busca_texto}%")
            )
        )
    resultados = query.all()
    return render_template('busca.html', resultados=resultados)

@app.route('/importancia')
def importancia():
    return render_template('importancia.html')

if __name__ == '__main__':
    app.run(debug=True)