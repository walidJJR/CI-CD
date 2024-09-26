# Start with the FastAPI base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

# Copier tous les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8001
EXPOSE 8001

# Si vous avez un fichier .env, décommentez la ligne suivante
# COPY .env /app
# ENV ENV_FILE_LOCATION=/app/.env
