# Тестовое задание Django + Stripe API
Проект взаимодействия фраемворка __Django__ и платёжной системы __Stripe__.

## Запуск проекта без Docker

1. ``Клонировать репозиторий https://github.com/Denis-Guselnikov/api_django_stripe``
2. ``cd stripe_django``
3. ``pip install -r requirements.txt``
4.  ``Создать и заполнить .env``


### Образец:
```
SECRET_KEY= 
DEBUG= 

STRIPE_PUBLIC_KEY= Ключи из https://stripe.com/docs
STRIPE_SECRET_KEY=

```

### База Данных
В репозитории уже есть db.sqlite3

6. ``python manage.py migrate``
7. ``python manage.py runserver``

## Запуск с помощью Docker

Убедитесь, что вы находитесь в той же директории, где сохранён Dockerfile
1. ``docker build -t stripe_django .``
2. ``cd stripe_django``
3. ``docker run --name stripe_django -it -p 8000:8000 stripe_django``

Проект доступен: ``localhost:8000``
