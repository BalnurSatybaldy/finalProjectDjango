from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User

from chat.models import Chat


def chat_view(request, charity_pk):
    try:
        chat = Chat.objects.get(charity_id=charity_pk)
    except ObjectDoesNotExist:
        chat = Chat.objects.create(charity_id=charity_pk)

    try:
        chat.members.get(id=request.user.pk)
    except ObjectDoesNotExist:
        chat.members.add(request.user)
        chat.number_of_members += 1
        chat.save()

    return render(request, "chat.html", {"chat_pk": chat.pk, "charity_title": chat.charity.title, "number_of_members": chat.number_of_members, "user_pk": request.user.pk})


def get_messages_view(request, chat_pk):
    chat = Chat.objects.get(id=chat_pk)
    startswith = int(request.GET.get('startswith'))
    endswith = int(request.GET.get('endswith'))
    messages = list(chat.messages.all())
    messages_length = len(messages)
    messages.reverse()
    messages = messages[startswith:endswith]

    if messages_length <= endswith:
        no_more_message = True
    else:
        no_more_message = False

    messages = serialize("python", messages)
    for message in messages:
        user = User.objects.get(id=message["fields"]["user"])
        message["fields"]["username"] = user.first_name + " " + user.last_name

    return JsonResponse({"messages": messages, "no_more_message": no_more_message})


def send_message_view(request, chat_pk):
    chat = Chat.objects.get(pk=chat_pk)
    chat.messages.create(user=request.user, message=request.GET.get("message"))
    return redirect(reverse("chat", kwargs={"charity_pk": chat.charity.pk}))


def get_recent_messages_view(request, chat_pk):
    last_message_pk = int(request.GET.get("last_message_pk"))
    chat = Chat.objects.get(id=chat_pk)
    messages = list(chat.messages.all())
    messages.reverse()

    recent_messages = list()
    if messages[0].pk != last_message_pk:
        for message in messages:
            if message.pk == last_message_pk:
                break
            else:
                recent_messages.append(message)

    recent_messages = serialize("python", recent_messages)
    for message in recent_messages:
        user = User.objects.get(id=message["fields"]["user"])
        message["fields"]["username"] = user.first_name + " " + user.last_name

    return JsonResponse({"recent_messages": recent_messages})
