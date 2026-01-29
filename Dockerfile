
#Imagen base python
FROM python:3.11-slim

#Directorio de trabajo dentro del contenedor
WORKDIR /app

#Copiamos el codigo al contenedor
COPY main.py .
COPY clientes ./clientes

#Comando para ejecutar la aplicacion 
CMD ["python", "main.py"]

