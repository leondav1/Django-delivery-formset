# Delivery Form

## Setup local

Первое, что нужно сделать, это клонироать репозиторий:
```angular2html
$ https://github.com/leondav1/Django-delivery-formset.git
$ cd Django-delivery-formset
```
Создайте виртуальную среду для установки зависимостей и активируйте ее:
```angular2html
$ python -m venv env
$ source env/bin/activate
```
Затем установите зависимости:
```angular2html
(env)$ pip install -r requirements.txt
```
Создайте файл .env, добавьте одну настройку DEBUG=True:
```angular2html
echo DEBUG=True > .env
```
Cоздать и применить миграции:
```angular2html
python manage.py makemigrations
python manage.py migrate
```
Создать суперпользователя:
```angular2html
python manage.py createsuperuser
```
Запускаем сервер:
```angular2html
python manage.py runserver
```
Страница доступна по адресу: http://127.0.0.1:8000/delivery/create/
