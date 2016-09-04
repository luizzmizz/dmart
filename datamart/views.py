from django.shortcuts import render
# Create your views here.
from .models import dmSection
from django.http import HttpResponse
from django.template import loader

def dmSections(request):
    return HttpResponse(loader.get_template('datamart/dmSections.html').render({ 'dmSections': dmSection.objects.order_by('name') }, request))
