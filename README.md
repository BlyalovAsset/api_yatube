# API_FINAL_YATUBE

API_Final - законченная версия API для yatube.

## Стек технологий

- Python 3.7
- Django Rest Framework
- SQLite

## Как запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:
    ```sh
    git clone git@github.com:LazarevaKate/api_final_yatube.git
    cd api_final_yatube
    ```

2. Создать и активировать виртуальное окружение:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Установить зависимости из файла `requirements.txt`:
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Выполнить миграции:
    ```sh
    python3 manage.py migrate
    ```

5. Запустить проект:
    ```sh
    python3 manage.py runserver
    ```

## Описание проекта

API_Final - это API для платформы yatube, которая позволяет пользователям публиковать посты, комментировать их и подписываться на других пользователей. Этот проект предоставляет все необходимые конечные точки для работы с данными платформы.

## Примеры запросов к API

### Получение списка постов

```http
GET /api/v1/posts/
