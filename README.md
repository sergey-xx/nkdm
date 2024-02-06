# nkdm

Локальный запуск проекта


```
docker compose up
```

При первом запуске нужно выполнить миграции и перезапустить compose.
```
docker compose exec backend python manage.py migrate
docker compose down
docker compose up
```


Генерация 10 тестовых пользователей и постов.
```
docker compose exec backend python manage.py generatedata 10
```

Запуск задачи ежедневной рассылки.
```
docker compose exec backend python manage.py sendmails
```

Документация API лежит в "backend\docs\schema.yaml"