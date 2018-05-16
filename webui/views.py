from django.shortcuts import render
from data_processing import Searching

def home(request):
    search = ""
    results = []

    if (request.method == 'POST'):
        location = request.POST['search']
        results = Searching.main_flow(location)

    return render(request, 'webui/home.html', {'search':search, 'results':results})
