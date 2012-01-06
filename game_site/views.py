# Create your views here.
import random, string
from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from game_site.models import Login
#from django.template.loader import Context

def index(request, result = {}):
    result = { ' head_title' : 'Gamesite', 'page_title' : 'Welcome to Game Site', 'page_body' : 'This is Gamesite' }
    return render_to_response('index.html', result)
