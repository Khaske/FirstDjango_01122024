# FirstDjango_01122024

## Инструкция по развертыванию проекта
1. 'python3 -m venv django_venv'
2. 'source django_venv/bin/activate'
3. 'pip install -r requirements.txt'
4. 'python manage.py migrate'
5. 'python manage.py runserver'

## Получение репозитория
```
git clone https://github.com/vadshi/FirstDjango_18052024.git FirstDjango_teacher
```
```
git init # в папке проекта
git pull origin master
```
Проверка подключения к репозиторию:
```
git remote -v
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
```
В settings.py > INSTALLED_APPS django_extensions
```
pip install ipython
```
Запуск:
```
python manage.py shell_plus --ipython
```

## Работа с БД
### Дополнительные инструменты
1. https://antares-sql.app/ , скачиваем AppImage. ПКМ > Properties > Permissions > Allow this file to run as a programm
2. Установка sqlite3 через терминал:
```
sudo apt update
sudo apt install sqlite3
``` 
3. Создание модели django:
В settings.py > INSTALLED_APPS добавляем свои приложения.
4. Миграция БД:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
### Изменение структуры БД
1. Вносим изменения в models.py, если в БД уже существуют элементы, то добавляем default=''.
2. Проводим миграцию БД
### Выгрузить данные из БД
```
python manage.py dumpdata MainApp --indent 4 > ./fixtures/save_all.json
```
### Загрузить данные в БД
```
python manage.py loaddata ./fixtures/save_all.json
```