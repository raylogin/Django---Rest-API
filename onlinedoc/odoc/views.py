from django.shortcuts import render
from . import forms
from .models import DocPlace
from django.core.serializers import serialize
import json
from django.http import HttpResponse
from django.forms.models import model_to_dict

# Create your views here.
def editor(request, fname):
    RFilename = fname
    if request.method == 'POST':
        form = request.POST
        RFilename = form['Filename']
        try:
            RFile = form['File']
            try:
                fp = DocPlace.objects.get(Filename = RFilename)
                fp.Filename = RFilename
                fp.File = RFile
                fp.save()
            except:
                fp = DocPlace(File = RFile, Filename = RFilename)
                fp.save()
        except:
            pass
    try:
        fp = DocPlace.objects.get(Filename = RFilename)
        return render(request,'odoc/editor.html',{"filename":fp.Filename, "file":fp.File, "Untitled":"Untitled"})
    except:
        return render(request,'odoc/editor.html')

def createfile(request):
    RFilename = 'None'
    if request.method == 'POST':
        form = request.POST
        RFilename = form['Filename']
        try:
            RFile = form['File']
            try:
                fp = DocPlace.objects.get(Filename = RFilename)
                fp.Filename = RFilename
                fp.File = RFile
                fp.save()
            except:
                fp = DocPlace(File = RFile, Filename = RFilename)
                fp.save()
        except:
            pass
    try:
        fp = DocPlace.objects.get(Filename = RFilename)
        return render(request,'odoc/editor.html',{"filename":fp.Filename, "file":fp.File, "Untitled":"Untitled"})
    except:
        return render(request,'odoc/editor.html')

def index(request):
    fp = DocPlace.objects.all()
    # results = DocPlace.objects.all().values_list('Filename', flat=True) 
    alist = []
    for x in fp:
        flp = DocPlace.objects.get(Filename = x)
        adict = {'Filename':flp.Filename, 'File':flp.File}
        alist.append(adict)
    print(alist)
    return render(request,'odoc/index.html',{"content":alist})
