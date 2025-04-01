FROM python:3.9

WORKDIR /app

COPY app.py train_model.py sentiment_model.pkl requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
