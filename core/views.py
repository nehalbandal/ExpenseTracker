from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect("/admin/")


def view_only(request):
    user = authenticate(username="kamal", password="Krs@2022")
    if user is not None:
        login(request, user)
    return HttpResponseRedirect("/admin/")
