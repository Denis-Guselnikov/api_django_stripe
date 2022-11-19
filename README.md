# Тестовое задание Django + Stripe API
Проект взаимодействия фраемворка __Django__ и платёжной системы __Stripe__.

## Запуск проекта без Docker

1. ``Клонировать репозиторий https://github.com/Denis-Guselnikov/api_django_stripe``
2. ``cd api_django_stripe/``
3. ``python -m venv venv``
4. ``source venv/Scripts/activate``
5. ``pip install -r requirements.txt``
6. ``Создать и заполнить .env`` - файл должен находится в главном приложении stripe_django.

### Образец:
```
SECRET_KEY= 
DEBUG= 

STRIPE_PUBLIC_KEY= Ключи из https://stripe.com/docs
STRIPE_SECRET_KEY= После регистрации ключи будут на https://dashboard.stripe.com/test/apikeys
```

### База Данных
В репозитории уже есть db.sqlite3

7. ``cd stripe_django/``
7. ``python manage.py runserver``


## Запуск с помощью Docker

Убедитесь, что вы находитесь в той же директории, где сохранён Dockerfile
1. ``docker build -t stripe_django .``
2. ``cd stripe_django/``
3. ``docker run --name stripe_django -it -p 8000:8000 stripe_django``

Проект доступен: ``localhost:8000``
