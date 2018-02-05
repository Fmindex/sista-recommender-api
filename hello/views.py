from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Greeting


from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

class myModel(APIView):
    def get(self, request, *args, **kw):
        result = {"status" : 200, "First4196" : "get"}
        response = Response(result, status.HTTP_200_OK)
        return response
    
    def post(self, request, *args, **kw):
        result = {"status" : 200, "First4196" : "post"}
        response = Response(result, status.HTTP_200_OK)
        return response
