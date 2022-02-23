# quiz_1_web

## Docker commands
- сборка и запуск стэка контейнеров
```shell
docker-compose -f dev_docker-compose.yml up --build
```
- остановка и удаление стэка
```shell
docker-compose -f dev_docker-compose.yml down
```
- выполнение Django команд в контейнере `web`
```shell
docker-compose -f dev_docker-compose.yml exec web python manage.py migrate
docker-compose -f dev_docker-compose.yml exec web python manage.py collectstatic
docker-compose -f dev_docker-compose.yml exec web python manage.py loaddata dump_dat
a.json
docker-compose -f dev_docker-compose.yml exec web python manage.py createsuperuser
```