from django.http import HttpResponse
from django.core import serializers
from rooms.models import Room
import json


def list_rooms(request):
    data = serializers.serialize("json", Room.objects.all()) # ( "format name", "query set") using components
    response = HttpResponse(content=data)
    return response