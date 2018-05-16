from django.shortcuts import render
from data_processing import Searching
from django import forms
from django.conf import settings

class SelectLocationForm(forms.Form):
    LOCATION_CHOICES = ((loc, loc) for loc in settings.LOCATIONS)
    locations = forms.ChoiceField(choices=LOCATION_CHOICES, widget=forms.Select(attrs={'onchange': 'actionform.submit();'}))

def home(request):
    search = ""
    results = []

    if (request.method == 'POST'):
        location = request.POST['search']
        results = Searching.main_flow(location)

    return render(request, 'webui/home.html', {'search':search, 'results':results})

def home_v2(request):
    search = ""
    results = {}
    if (request.method == 'POST'):
        location = request.POST['locations']
    else:
        location = "도곡동"

    df = Searching.ranked_restaurant[location]
    results = dict(zip(df.name, df.counter))

    return render(request, 'webui/home_v2.html', {'search': search, 'results': results, 'form':SelectLocationForm(request.POST or None)})