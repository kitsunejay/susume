from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core import serializers
import json

from .models import Job, Spell, Server

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the susume index.")

@csrf_exempt
def job(request, id=None):
    if request.method == "POST":
        if request.content_type == 'application/json':
            job_json = json.loads(request.body)
            to_deserialize = []
            for j in job_json:
                nj = {"model":"susume.job","fields":{}}
                try:
                    for k,v in j.items():
                        nj["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(nj)
                # Validate fields and attempt to create/update
            for deserialized_job in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_job.object.full_clean(validate_unique=False)
                deserialized_job.object.save()
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
            for s in spell_json:
                ns = {"model":"susume.spell","fields":{}}
                try:
                    for k,v in s.items():
                        ns["fields"][k] = v
                except KeyError as e:
                    return HttpResponse(e,status=400)
                # Add new job to list of dict to be deserialized
                to_deserialize.append(ns)
                # Validate fields and attempt to create/update
            for deserialized_spell in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_spell.object.full_clean(validate_unique=False)
                deserialized_spell.object.save()
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
            for deserialized_spell in serializers.deserialize("json",json.dumps(to_deserialize)):
                deserialized_spell.object.full_clean(validate_unique=False)
                deserialized_spell.object.save()
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