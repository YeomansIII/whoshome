from django.http import HttpResponse, HttpResponseRedirect
import uuid
import json
from django.shortcuts import render
from api.models import Person
from django.contrib.auth.models import User
from api.forms import RegisterForm
# Create your views here.

def process(request, tag_uuid):
    person_list = Person.objects.filter(tag_uuid=tag_uuid)
    jsons = json.loads('{"name":"","coming_home":false, "pin":"", "new":false}')
    if person_list:
        persona = person_list[0]
    else:
        username = uuid.uuid4().hex[:4].upper()
        password = username
        user = User.objects.create_user(username=username, email=None, password=password)
        persona = Person.objects.create(user=user, tag_uuid=tag_uuid)
        persona.save()
    jsons['name'] = persona.user.first_name + " " + persona.user.last_name
    jsons['pin'] = persona.user.username
    jsons['new'] = persona.new
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

def register(request, pin):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            persona = Person.objects.filter(user__username=pin)[0]
            print(form.cleaned_data['first_name'])
            persona.user.first_name = form.cleaned_data['first_name']
            persona.user.last_name = form.cleaned_data['last_name']
            persona.new = False
            persona.user.save()
            persona.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        person_list = Person.objects.filter(user__username=pin)
        if not person_list:
            return render(request, 'nopin.html')
        elif person_list[0].new == True:
            form = RegisterForm()
            return render(request, 'register.html', {'form': form, 'pin':pin})
    return HttpResponseRedirect('/')
