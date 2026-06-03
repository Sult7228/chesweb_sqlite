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
git clone <ссылка на репозиторий>
cd web_chess

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| POST | /api/auth/register/ | Регистрация |
| POST | /api/auth/login/ | Получить JWT |
| POST | /api/auth/refresh/ | Обновить токен |
| GET | /api/profile/{id}/ | Профиль игрока |
| PATCH | /api/profile/me/ | Редактировать профиль |
| POST | /api/games/ | Создать партию |
| GET | /api/games/ | Список партий |
| GET | /api/games/{id}/ | Детали партии |
| POST | /api/games/{id}/move/ | Сделать ход |
| POST | /api/games/{id}/resign/ | Сдаться |
| POST | /api/tournaments/ | Создать турнир |
| GET | /api/tournaments/ | Список турниров |
| POST | /api/tournaments/{id}/join/ | Вступить в турнир |

## Документация
После запуска сервера: http://127.0.0.1:8000/api/docs/

## Admin
http://127.0.0.1:8000/admin/
