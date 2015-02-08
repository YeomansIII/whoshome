from django.http import HttpResponse
import uuid
import json

from api.models import Person
from django.contrib.auth.models import User
# Create your views here.

def process(request, tag_uuid):
    person_list = Person.objects.filter(tag_uuid=tag_uuid)
    jsons = json.loads('{"name":"","coming_home":false, "pin":"", "new":false}')
    if person_list:
        persona = person_list[0]
    else:
        username = uuid.uuid4().hex[:6].upper()
        password = username
        user = User.objects.create_user(username=username, email=None, password=password)
        persona = Person.objects.create(user=user, tag_uuid=tag_uuid, is_home=True)
        persona.save()
        jsons['new'] = True
    jsons['name'] = persona.user.first_name + " " + persona.user.last_name
    jsons['pin'] = persona.user.username
    if persona.is_home == False:
        jsons['coming_home'] = True
        persona.is_home = True
    else:
        persona.is_home = False
    persona.save()
    return HttpResponse(json.dumps(jsons))

def whoshome(request):
    person_list = Person.objects.filter(is_home=True)
    jsons = {'personsAtHome':[]}
    for persona in person_list:
        name = persona.user.first_name + " " + persona.user.last_name
        timestamp = str(persona.modified)
        jsons['personsAtHome'].append({'name':name,'timestamp':timestamp})
    return HttpResponse(json.dumps(jsons))
