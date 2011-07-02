# Create your views here.
import random, string
from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from game_site.models import Login

def index(request, result = {}):
    return render_to_response('index.html', result)