from django.http import HttpResponse
import uuid
import json

from api.models import Person
from django.contrib.auth.models import User
# Create your views here.

def process(request, tag_uuid):
    person_list = Person.objects.all()
    tagger = None
    jsons = json.loads('{"name":"","coming_home":false, "pin":"", "new":false}')
    for person in person_list:
        if person.tag_uuid == tag_uuid:
            tagger = person
    if tagger == None:
        username = uuid.uuid4().hex[:4].upper()
        password = username
        user = User.objects.create_user(username=username, email=None, password=password)
        person = Person.objects.create(user=user, tag_uuid=tag_uuid, is_home=True)
        person.save()
        tagger = person
        jsons['new'] = True
    jsons['name'] = person.user.first_name + " " + person.user.last_name
    jsons['pin'] = person.user.username
    if person.is_home == False:
        jsons['coming_home'] = True
        person.is_home = True
    else:
        person.is_home = False
    person.save()
    return HttpResponse(json.dumps(jsons))

def buildings_list(request):
    person_list = Person.objects.order_by('name')[:5]
    jsons = '{"buildings":['
    for p in building_list:
        jsons += '"'+p.__str__()+'":"'+p.address.__str__()+'",'
    jsons = jsons[:-1]+']}'
    return HttpResponse(jsons)
