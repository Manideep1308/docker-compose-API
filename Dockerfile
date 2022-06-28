FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .


EXPOSE 1564

CMD ["python", "app.py"]
