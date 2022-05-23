"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from charity import views as charity_views
from project import settings
from trustfund import views as trustfund_views
from volunteer import views as volunteer_views
from chat import views as chat_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', charity_views.home_page_view, name="home"),
    path('charity_list/', charity_views.charity_list_view),

    path('charity_list/to_be_volunteer/<int:charity_pk>/', volunteer_views.to_be_volunteer_view),
    path('charity_list/donate/<int:charity_pk>/', volunteer_views.donate_view),
    path('after_donation/<int:order_id>/', volunteer_views.after_donation_view),

    path('authorization/', include('django.contrib.auth.urls')),
    path('authorization/sign-up/', charity_views.SignUpView.as_view(), name="sign-up"),
    path('profile/', charity_views.profile_page_view, name="profile"),

    path('trustfund_profile/', trustfund_views.profile_page_view),
    path('trustfund_profile/add_charity/', trustfund_views.add_charity_view, name="add_charity"),
    path('trustfund_profile/charity/<int:charity_pk>/remove_charity/', trustfund_views.remove_charity_view, name="remove_charity"),
    path('trustfund_profile/charity/<int:charity_pk>/edit_charity/', trustfund_views.edit_charity_view, name="edit_charity"),

    path('volunteer_profile/', volunteer_views.profile_page_view),

    path('chat/<int:charity_pk>/', chat_views.chat_view, name="chat"),
    path('chat/<int:chat_pk>/get_messages/', chat_views.get_messages_view, name="get_messages"),
    path('chat/<int:chat_pk>/get_recent_messages/', chat_views.get_recent_messages_view, name="get_recent_messages"),
    path('chat/<int:chat_pk>/send_message/', chat_views.send_message_view, name="send_message")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
