from django.shortcuts import render, redirect
from charity.models import Charity


def profile_page_view(request):
    return render(request, "admin.html")


def add_charity_view(request):
    typee = request.POST.get("type")
    title = request.POST.get("title")
    description = request.POST.get("description")
    poster = request.FILES.get("poster")
    needed_price = request.POST.get("needed_price")

    if not needed_price:
        needed_price = 0
    else:
        needed_price = int(needed_price)

    Charity.objects.create(type=typee, title=title, description=description, needed_price=needed_price, poster=poster, trustfund=request.user.trustfund)
    return redirect("/trustfund_profile/")


def edit_charity_view(request, charity_pk):
    charity = Charity.objects.get(id=charity_pk)
    charity.type = request.POST.get("type")
    charity.title = request.POST.get("title")
    charity.description = request.POST.get("description")

    needed_price = request.POST.get("needed_price")
    if not needed_price:
        needed_price = 0
    else:
        needed_price = int(needed_price)
    charity.needed_price = needed_price

    poster = request.FILES.get("poster")
    if poster:
        charity.poster = poster

    charity.save()
    return redirect("/trustfund_profile/")


def remove_charity_view(request, charity_pk):
    Charity.objects.get(id=charity_pk).delete()
    return redirect("/trustfund_profile/")
