# Usa uma imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do seu PC para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o Flask no Cloud Run
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app