from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

from .models import Job, Spell
from .serializers import JobSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the susume index.")


class JobList(APIView):
    """
    List all jobs, or create a new job.
    """
    def get(self, request, format=None):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def spell(request, id=None):
    if id:
        try:
            spell = Spell.objects.get(id=id)
            spells = [spell]
        except ObjectDoesNotExist:
            return render(request, 'dne.html')
    else:
        spells = Spell.objects.all()
    return render(request, 'spells.html', {'spells': spells})
