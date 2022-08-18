from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *


@login_required
def add_default_flat_data(request):
    try:
        buildings = {
            'A1': 14,
            'A2': 14,
            'A3': 14,
            'A4': 14,
            'B1': 16,
            'B2': 16
        }

        for wing, flats in buildings.items():
            for i in range(1, flats+1):
                name = "{}-{}".format(wing, i)
                MoneyCollection.objects.create(building=wing, flat_no=i, name=name,
                                               added_by=request.user, modified_by=request.user)

        return HttpResponse("Data Added Successfully!")
    except Exception as e:
        print(e)
        return HttpResponse("Data Loading Failed! ")


