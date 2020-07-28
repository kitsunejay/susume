from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core import serializers
import json

from .models import Job, Spell, Server, Slot, Ability, Equipment
#
import pathlib
import sys
sys.path.append(pathlib.Path(__file__).parent.name + '/libs/')

import helpers

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the susume index.")

@csrf_exempt
def dne(request):
    return render(request, 'dne.html')

@csrf_exempt
def job(request, id=None):
    if request.method == "POST":
        if request.content_type == 'application/json':
            this_json = json.loads(request.body)
            to_deserialize = []
            for item in this_json:
                new_item = {"model":"susume.job","fields":{}}
                try:
                    for k,v in item.items():
                        new_item["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(new_item)
                # Validate fields and attempt to create/update
            for deserialized_item in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_item.object.full_clean(validate_unique=False)
                deserialized_item.object.save()
            return render(request, 'jobs.html', {'jobs': Job.objects.all()})
        else:
            return HttpResponse("JSON ONLY")
    if id:
        try:
            job = Job.objects.get(id=id)
            jobs = [job]
        except ObjectDoesNotExist:
            return render(request, 'dne.html')
    else:
        # QuerySet filled with Models
        jobs = Job.objects.all()
    if request.headers['Content-Type'] == 'application/json':
        # QuerySet filled with dicts
        json_jobs = jobs.values()
        return JsonResponse(list(json_jobs),safe=False)
    else:
        return render(request, 'jobs.html', {'jobs': jobs})

@csrf_exempt
def spell(request, id=None):
    if request.method == "POST":
        if request.content_type == 'application/json':
            spell_json = json.loads(request.body)
            to_deserialize = []
            for item in this_json:
                new_item = {"model":"susume.spell","fields":{}}
                try:
                    for k,v in item.items():
                        new_item["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(new_item)
                # Validate fields and attempt to create/update
            for deserialized_item in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_item.object.full_clean(validate_unique=False)
                deserialized_item.object.save()
            return render(request, 'spells.html', {'spells': Spell.objects.all()})
        else:
            return HttpResponse("JSON ONLY")
    if id:
        try:
            spell = Spell.objects.get(id=id)
            spells = [spell]
        except ObjectDoesNotExist:
            return render(request, 'dne.html')
    else:
        spells = Spell.objects.all()
    return render(request, 'spells.html', {'spells': spells})

@csrf_exempt
def ability(request, id=None):
    if request.method == "POST":
        if request.content_type == 'application/json':
            this_json = json.loads(request.body)
            to_deserialize = []
            for item in this_json:
                new_item = {"model":"susume.ability","fields":{}}
                try:
                    for k,v in item.items():
                        new_item["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(new_item)
                # Validate fields and attempt to create/update
            for deserialized_item in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_item.object.full_clean(validate_unique=False)
                deserialized_item.object.save()
            return render(request, 'abilities.html', {'abilities': Ability.objects.all()})
        else:
            return HttpResponse("JSON ONLY")
    if id:
        try:
            ability = Ability.objects.get(id=id)
            abilities = [ability]
        except ObjectDoesNotExist:
            return render(request, 'dne.html')
    else:
        abilities = Ability.objects.all()
    return render(request, 'abilities.html', {'abilities': abilities})

@csrf_exempt
def server(request, id=None):
    if request.method == "POST":
        if request.content_type == 'application/json':
            server_json = json.loads(request.body)
            to_deserialize = []
            for s in server_json:
                ns = {"model":"susume.server","fields":{}}
                try:
                    for k,v in s.items():
                        ns["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(ns)
                # Validate fields and attempt to create/update
            for deserialized_item in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_item.object.full_clean(validate_unique=False)
                deserialized_item.object.save()
            return render(request, 'servers.html', {'servers': Server.objects.all()})
        else:
            return HttpResponse("JSON ONLY")
    if id:
        try:
            server = Server.objects.get(id=id)
            servers = [server]
        except ObjectDoesNotExist:
            return render(request, 'dne.html')
    else:
        servers = Server.objects.all()
    return render(request, 'servers.html', {'servers': servers})

@csrf_exempt
def slot(request, id=None):
    if request.method == "POST":
        if request.content_type == 'application/json':
            slot_json = json.loads(request.body)
            to_deserialize = []
            for s in slot_json:
                ns = {"model":"susume.slot","fields":{}}
                try:
                    for k,v in s.items():
                        ns["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(ns)
                # Validate fields and attempt to create/update
            for deserialized_item in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_item.object.full_clean(validate_unique=False)
                deserialized_item.object.save()
            return render(request, 'slots.html', {'slots': Slot.objects.all()})
        else:
            return HttpResponse("JSON ONLY")
    if id:
        try:
            slot = Slot.objects.get(id=id)
            slots = [slot]
        except ObjectDoesNotExist:
            return render(request, 'dne.html')
    else:
        slots = Slot.objects.all()
    return render(request, 'slots.html', {'slots': slots})

@csrf_exempt
def equipment(request, id=None):
    if request.method == "POST":
        if request.content_type == 'application/json':
            equipment_json = json.loads(request.body)
            to_deserialize = []
            for s in equipment_json:
                ns = {"model":"susume.equipment","fields":{}}
                try:
                    for k,v in s.items():
                        ns["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(ns)
                # Validate fields and attempt to create/update
            for deserialized_item in serializers.deserialize("json",json.dumps(to_deserialize)):
                try:
                    deserialized_item.object.full_clean(validate_unique=False)
                    deserialized_item.object.save()
                except Exception as e:
                    print(e,deserialized_item.object.id,deserialized_item.object.en)
            return render(request, 'equipment.html', {'equipment': Equipment.objects.all()})
        else:
            return HttpResponse("JSON ONLY")
    if id:
        try:
            item = Equipment.objects.get(id=id)
            items = [item]
        except ObjectDoesNotExist:
            return render(request, 'dne.html')
    else:
        items = Equipment.objects.all()
    return render(request, 'Equipment.html', {'equipment': items})

def dynamic_template(request, req_page="jobs"):
    data = Slot.objects.values()
    fields = []
    for f in data:
        fields = fields + list(f.keys())
    fields = set(fields)
    print(fields)
        
    page = {}
    
    if req_page:
        page['name'] = req_page
        page['title'] = page['name']
    else:
        page['name'] = "Jobs"
        page['title'] = page['name']
    page['menu_dropdown'] = [
        {'name':'Jobs','endpoint':'/susume/jobs'},
        {'name':'Servers','endpoint':'/susume/servers'},
        {'name':'Slots','endpoint':'/susume/slots'},
        {'name':'Spells','endpoint':'/susume/spells'},
        {'name':'Abilities','endpoint':'/susume/abilities'},
    ],
    page['fields'] = fields

    data = Slot.objects.all()
    return render(request, 'dynamic.html',
        {'app_name': 'Susume',
         'page': page,
         'data': data})
