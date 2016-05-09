from django.shortcuts import render

from chemposer.forms import *

from django.http import *
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from subprocess import call


def home(request):
	context = {}
	return render(request, 'home.html', context)


def upload_xyz(request, uid=None):

    context = {}
    if request.method == 'GET':
        print "Get request to upload_xyz"
        #context['name'] = '/static/xyz/tmp/C20.sdf'
        return render(request, 'renderMolecule.html', context)
    print request.FILES

    filename = request.FILES['xyzfile'].name
    data = request.FILES['xyzfile']
    path = default_storage.save('tmp/'+filename, ContentFile(data.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)

    ex = './chemposer/chemposer'
    fname = './chemposer/static/xyz/tmp/'+filename
    call([ex,fname])
    arr = filename.split('.')

    context['name'] = '/static/xyz/tmp/'+ arr[0] + '.sdf' 
    return render(request, 'renderMolecule.html', context)


