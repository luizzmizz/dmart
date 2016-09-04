from django.shortcuts import render
from datetime import datetime
# Create your views here.
from models import ov_user
from models import query
from django.http import HttpResponse
from django.template import loader

def index(request):
    users = ov_user.objects.order_by('-created')[:5]
    template = loader.get_template('contracts/index.html')
    context = { 'users':users }
    return HttpResponse(template.render(context, request))

def listqueries(request):
    return HttpResponse(loader.get_template('contracts/listqueries.html').render({ 'queries': query.objects.all() }, request))
