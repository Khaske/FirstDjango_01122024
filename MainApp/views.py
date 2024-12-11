from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

# Create your views here.

  
def home(request): # M1.task_1
    context = {
        "name": "Исхаков Ренат Наильевич",
        "email": "khaske@ya.ru"
    }
    return render(request, "index.html", context)

def about(request): # M1.task_2, лучше сделать через словарь
    text = """
    Имя: <strong>Ренат</strong><br/>
    Отчество: <strong>Наильевич</strong><br/>
    Фамилия: <strong>Исхаков</strong><br/>
    телефон: <strong>+7-000-000-00-00</strong><br/>
    email: <strong>khaske@ya.ru</strong>
    """
    return HttpResponse(text)

def get_item(request, item_id: int): # M3.task_3
    # item = next((item for item in items if item["id"] == item_id), None) # генератор
    # if item is not None:
    #     context = {
    #         "item": item
    #     }
    #     return render(request, "item.html", context)
    # return HttpResponseNotFound(f"Товар с id = {item_id} не найден!")
    context = {
        "item": Item.objects.get(pk=item_id)
    }
    return render(request, "item.html", context)
    
def get_items_list(request): # M3.task_2
    context = {
        "items": Item.objects.all()
    }
    return render(request, "items_list.html", context)