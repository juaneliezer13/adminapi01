FROM python:3.11-slim
# Establece el directorio de trabajo en /app
WORKDIR /app
# Copia los archivos de requirements primero para aprovechar el cache
COPY requirements.txt .
# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
# Copia el resto del código de la aplicación
COPY . .
# Expone el puerto (por defecto FastAPI usa 8000)
EXPOSE ${API_PORT}
# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${API_PORT}"]
