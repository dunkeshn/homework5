from django.shortcuts import render
from django.http import HttpResponse
from core.models import User, UserChats
import datetime

def show_info(request):
    all_users = User.objects.all()
    all_messages = 0
    all_chats = UserChats.objects.all()
    for i in all_chats:
        all_messages += i.message_value
    time = str(datetime.datetime.now().time())[:5]
    date = datetime.datetime.now().date()
    print(time)

    return HttpResponse(f'Всего пользоваталей зарегистрировано: {all_users.count()} '
                        f'Всего сообщений отправлено на сайте: {all_messages} '
                        f'Текущее время: {time} '
                        f'Текущая дата: {date}')
