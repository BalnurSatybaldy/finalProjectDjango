from datetime import datetime, timedelta

import requests
from django.http import JsonResponse
from django.shortcuts import redirect, render

from project import settings
from volunteer.models import Volunteering, Donation


def profile_page_view(request):
    return render(request, "userProfile.html")


def _create_order(order_data):
    response = requests.post(settings.IOKA_CREATE_ORDER_URL, headers=settings.IOKA_REQUEST_HEADER, json=order_data)
    return response.json()["order"]["checkout_url"]


def donate_view(request, charity_pk):
    if request.user.is_authenticated:
        last_name = request.user.last_name
        first_name = request.user.first_name
        if hasattr(request.user, 'volunteer'):
            phone_number = request.user.volunteer.phone_number
        else:
            phone_number = request.user.trustfund.phone_number
    else:
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")
    amount = int(request.POST.get("amount", 0))
    order_object = Donation.objects.create(charity_id=charity_pk, price=amount, first_name=first_name, last_name=last_name, phone_number=phone_number)

    if request.user.is_authenticated:
        order_object.user = request.user
        order_object.save()

    order_data = {
        "amount": amount*100,
        "currency": "KZT",
        "capture_method": "AUTO",
        "due_date": (datetime.now() + timedelta(days=1)).isoformat(),
        "back_url": f"http://127.0.0.1:8000/after_donation/{order_object.id}/"
    }

    url = _create_order(order_data)
    return JsonResponse({"success": True, "url": url})


def after_donation_view(request, order_id):
    donation = Donation.objects.get(id=order_id)
    if not donation.is_paid:
        donation.charity.earned_price += donation.price
        donation.charity.save()
        donation.is_paid = True
        donation.save()
    return redirect("/")


def to_be_volunteer_view(request, charity_pk):
    if request.user.is_authenticated:
        last_name = request.user.last_name
        first_name = request.user.first_name
        phone_number = request.user.volunteer.phone_number
    else:
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")

    volunteering = Volunteering.objects.create(charity_id=charity_pk, last_name=last_name, first_name=first_name, phone_number=phone_number)
    if request.user.is_authenticated:
        volunteering.user = request.user
        volunteering.save()

    return JsonResponse({"success": True})
