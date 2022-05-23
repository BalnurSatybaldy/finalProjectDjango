from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from charity.models import Charity
from volunteer.models import Volunteer


def home_page_view(request):
    return render(request, "main.html")


def charity_list_view(request):
    charity_type = request.GET.get("type")
    charity_list = Charity.objects.filter(type=charity_type)
    return render(request, "charity_list.html", {"charity_list": charity_list, "type": charity_type})


def profile_page_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user, "trustfund"):  # request.user.trustfund
            return redirect('/trustfund_profile/')
        return redirect('/volunteer_profile/')
    return redirect('/authorization/login/')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        if not first_name:
            return JsonResponse({"success": False, "errors": {"first_name": "Введите Имя"}})
        elif not last_name:
            return JsonResponse({"success": False, "errors": {"last_name": "Введите Фамилия"}})
        elif not phone_number:
            return JsonResponse({"success": False, "errors": {"phone_number": "Введите Номер телефона"}})
        if form.is_valid():
            user = form.save()
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            Volunteer.objects.create(user=user, phone_number=phone_number)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
