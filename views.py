from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm

from .models import RescueSpecialist, PatientRecord



def index(request):
    rescuespecialist = RescueSpecialist.objects.get(id=1)
    template = loader.get_template('PCR/index.html')
    context = {
        'rescuespecialist': rescuespecialist,
    }
    return HttpResponse(template.render(context, request))

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/PCR/patientaccesscenter/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'PCR/login.html', {'form': form})

def patient_access_center(request):
    template = loader.get_template('PCR/PatientAccessCenter.html')
    return HttpResponse(template.render(request))

def search(request):
    template = loader.get_template('PCR/search.html')
    return HttpResponse(template.render(request))


def search_history(request):
    results=""
    if request.GET.get('sar_no'):
        search = request.GET.get('sar_no')
        results = PatientRecord.objects.get(pk=search)

    return render(request, 'PCR/past_history.html',{
        'results': results,
    })


def logout(request):
    template = loader.get_template('PCR/logout.html')
    return HttpResponse(template.render(request))


def add(request):
    template = loader.get_template('PCR/add.html')
    return HttpResponse(template.render(request))