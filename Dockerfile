# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos da sua aplicação para o diretório de trabalho
COPY . /app

# Instale as dependências
RUN pip install -r requirements.txt

# Comando para executar a aplicação
CMD ["python", "app.py"]
