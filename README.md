# api_final
api final

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/personage-hub/api_final_yatube
```

```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
cd venv/Scripts/
```

```
activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Создать администратора проекта (superuser):
```
python manage.py createsuperuser
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

###Примеры запросов
Получение JWT-токена

`POST`:```http://127.0.0.1:8000/api/v1/jwt/create/```

_payload (application/json)_:
```
{
  "username": "string",
  "password": "string"
}
```
Пример ответа (`200`):
```
{
  "refresh": "string",
  "access": "string"
}
```

###Документация
После запуска проекта документация доступна по ссылке [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)