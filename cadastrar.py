from app import app, db, PontoColeta


def interface_cadastro():
    print("--- ♻️ Cadastro de Pontos de Coleta - EcoMapa ---")

    while True:
        with app.app_context():
            nome = input("\nNome do local: ")
            endereco = input("Endereço (Rua, nº): ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            cep = input("CEP (apenas números): ")

            print("\nCategorias disponíveis: Eletroeletrônicos, Pilhas e Baterias, Eletrodomésticos")
            print("Para múltiplos tipos, separe por ponto-e-vírgula (;)")
            tipo = input("Tipo(s) de material: ")

            lat = float(input("Latitude (ex: -23.1234): "))
            lng = float(input("Longitude (ex: -46.1234): "))

            # Criando o registro
            novo_ponto = PontoColeta(
                nome=nome,
                endereco=endereco,
                bairro=bairro,
                cidade=cidade,
                cep=cep,
                tipo_material=tipo,
                latitude=lat,
                longitude=lng
            )

            db.session.add(novo_ponto)
            db.session.commit()
            print(f"\n✅ {nome} cadastrado com sucesso!")

        continuar = input("\nDeseja inserir outro registro? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nEncerrando cadastro. Bom trabalho!")
            break


if __name__ == '__main__':
    interface_cadastro()