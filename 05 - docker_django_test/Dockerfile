FROM python:3.10

RUN apt update \
    && apt install -y mc \
    && apt install -y vim

RUN mkdir -p /opt/src
WORKDIR /opt/src

COPY ./requiremants.txt requiremants.txt
RUN pip install -r requiremants.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
