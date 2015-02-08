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

def whoshome(request):
    person_list = Person.objects.filter(is_home=True)
    jsons = {'personsAtHome':[]}
    for person in person_list:
        name = person.user.first_name + " " + person.user.last_name
        timestamp = str(person.modified)
        jsons['personsAtHome'].append({'name':name,'timestamp':timestamp})
    return HttpResponse(json.dumps(jsons))
