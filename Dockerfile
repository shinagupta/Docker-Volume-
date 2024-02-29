FROM python:3.8-slim
WORKDIR /projecta
COPY . /projecta
EXPOSE 5000
CMD ["python", "main.py"]
