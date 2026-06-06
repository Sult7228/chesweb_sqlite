# чесс на - Django 

## стек
- Django 6.0
- Django REST Framework
- Simple JWT
- drf-spectacular (Swagger)
- SQLite / PostgreSQL
- python-chess

## Установка

```bash
git clone <ссылка на ваш репозиторий>
cd chessweb_django

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Документация
После запуска сервера: http://127.0.0.1:8000/api/docs/

## Admin
http://127.0.0.1:8000/admin/auth/user/
