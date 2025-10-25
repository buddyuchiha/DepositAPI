FROM python:3.12.8

WORKDIR /deposit_api/

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]
