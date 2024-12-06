from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]

        
def home(request): # M1.task_1
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Исхаков Р.Н.</i>
    """
    return HttpResponse(text)

def about(request): # M1.task_2
    text = """
    Имя: <strong>Ренат</strong><br/>
    Отчество: <strong>Наильевич</strong><br/>
    Фамилия: <strong>Исхаков</strong><br/>
    телефон: <strong>+7-000-000-00-00</strong><br/>
    email: <strong>khaske@ya.ru</strong>
    """
    return HttpResponse(text)

def get_item(request, item_id): # M1.task_3&4&6
    for item in items:
        if item["id"] == item_id:
            return HttpResponse(f'<p>Товар с id={item["id"]}: {item["name"]}, {item["quantity"]} шт.</p>\n<a href="http://127.0.0.1:8000/items/">Назад к списку товаров</a>')
    else:
        return HttpResponse(f'<p>Товар с id={item_id}: не найден</p>\n<a href="http://127.0.0.1:8000/items/">Назад к списку товаров</a>')
    
def get_items_list(request): # M1.task_5&6
    list = """
    <strong>Список всех товаров:</strong>
    <ol>\n
    """
    for item in items:
        list += f'    <li><a href="http://127.0.0.1:8000/items/{item["id"]}">{item["name"]}, {item["quantity"]} шт.</a></li>\n'
    list += "</ol>"
    return HttpResponse(list)