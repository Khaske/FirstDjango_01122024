# FirstDjango_01122024

## Инструкция по развертыванию проекта
1. 'python3 -m venv django_venv'
2. 'source django_venv/bin/activate'
3. 'pip install -r requirements.txt'
4. 'python manage.py runserver'

## Получение репозитория
```
git init # в папке проекта
git pull origin master
```

## Дополнительно
1. Git Graph
2. Полезное дополнение для шаблонов 'Django'
```
ext install batisteo.vscode-django
```
3. Добавить в `settings.json` (нажать значек страницы)
```
"emmet.includeLanguages": {
        "django-html": "html",
    },
"files.associations": {
    "*.html": "django-html"
}
```
4. Дополнительные инструменты:
```
pip install django-extensions
pip install ipython
```

### Работа с БД
1. https://antares-sql.app/ , скачиваем AppImage. ПКМ > Properties > Permissions > Allow this file to run as a programm
2. Установка sqlite3 через терминал:
```
sudo apt update
sudo apt install sqlite3
``` 
3. Создание модели django:
В settings.py > INSTALLED_APPS добавляем свои приложения.
```
python manage.py makemigrations
```
4. Миграция БД:
```
python manage.py migrate
```
8 PYTHON Day 2_4 . 47 min