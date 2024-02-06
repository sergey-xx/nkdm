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


Генерация 10 тестовых пользователей и 10 постов у каждого.
```
docker compose exec backend python manage.py generatedata 10
```

Запуск задачи ежедневной рассылки.
```
docker compose exec backend python manage.py sendmails
```

Документация API лежит в "backend\docs\schema.yaml"

'/api/v1/posts/' анонимам выдает все 500 постов. Авторизованным пользователям
только из тех блогов, на которые они подписаны

1000 анонимных запросов обрабатываются < 8 секунд 