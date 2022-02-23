# Dockerfile

FROM python:3.10

RUN apt update
RUN apt install -y mc vim

COPY ./main.py main.py

CMD ["python", "main.py"]
