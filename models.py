from app import db

class PontoColeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    tipo_material = db.Column(db.String(100), nullable=False) # Ex: Eletroeletrônicos
    latitude = db.Column(db.Float)  # Necessário para o mapa futuro
    longitude = db.Column(db.Float) # Necessário para o mapa futuro

    def __repr__(self):
        return f'<Ponto {self.nome}>'