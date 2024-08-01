# Basis-Image des Containers erstellen
FROM python:3.12.9

# Set up directory
RUN mkdir /application 
WORKDIR /application

# Copy python dependencies and install these dep
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the rest of the application
COPY . .

# Expose port 8001 to allow communication to/from server
EXPOSE 8001
STOPSIGNAL SIGINT 

ENTRYPOINT ["python"]
CMD ["notfallapp_main.py"]
