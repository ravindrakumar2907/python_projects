from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
# Create your views here.
# function that takes request and return response
# Request handler
# actions

#https://stackoverflow.com/questions/45720065/django-missing-1-required-positional-argument-request

def hellow(request):
    return HttpResponse('hellow word')

def myView(request):
    return render(request, 'index.html', {'name': 'ravi'})

def index1(request):
  template = loader.get_template('data.html')
  HttpResponse(template.render())
  
def data(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)