from app import app, db, PontoColeta


def cadastrar_pontos():
    pontos = [
        PontoColeta(
            nome="Leroy Merlin - Raposo Tavares",
            endereco="Rod. Raposo Tavares, Km 14,5",
            bairro="Jardim Maria Luiza",
            cidade="São Paulo",
            cep="05576-100",
            tipo_material="Eletroeletrônicos;Pilhas e Baterias;Eletrodomésticos",
            latitude=-23.585955, longitude=-46.751633  # Coordenadas aproximadas
        ),
        PontoColeta(
            nome="Descomplica Butantã",
            endereco="R. Dr. Ulpiano da Costa Manso, 201",
            bairro="Peri Peri",
            cidade="São Paulo",
            cep="05538-010",
            tipo_material="Eletroeletrônicos;Pilhas e Baterias;Eletrodomésticos",
            latitude=-23.588096, longitude=-46.737987
        ),
        PontoColeta(
            nome="Makro - Butantã",
            endereco="R. Carlos Lisdegno Carlucci, 519",
            bairro="Peri Peri",
            cidade="São Paulo",
            cep="05536-000",
            tipo_material="Eletroeletrônicos;Pilhas e Baterias;Eletrodomésticos",
            latitude=-23.590733, longitude=-46.738243
        )
    ]

    with app.app_context():
        # Limpa o banco antes de inserir (opcional, para evitar duplicados no teste)
        db.drop_all()
        db.create_all()

        for p in pontos:
            db.session.add(p)

        db.session.commit()
        print("✅ Pontos de coleta cadastrados com sucesso!")


if __name__ == '__main__':
    cadastrar_pontos()