### Технологии
Python 3.7, Django 2.2, DRF, JWT + Djoser
### Запуск проекта в dev-режиме
- Клонировать репозиторий и перейти в него в командной строке.
```bash
git clone https://github.com/WispHes/api_final_yatube.git
```
- Установите виртуальное окружение c версии Python 3.7 :
```bash
py -3.7 -m venv venv
```
- Активируйте виртуальное окружение :
```bash
venv/Scripts/activate
```
- Далее установите зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
- Перейдите в дерикторию yatube_api и выполните миграции:
```bash
python manage.py migrate
```
- После требуется создать суперпользователя:
```bash
python manage.py createsuperuser
```
- Чтобы запустить проект используйте команду:
```bash
python manage.py runserver
```