# django imports
from django.conf import settings


def settings_media(request):

    return {'setting': settings}
