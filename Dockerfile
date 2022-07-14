FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get -y install openssh-server

RUN apt-get install -y sshpass

COPY . . 

EXPOSE 1564

CMD ["python", "app.py"]
