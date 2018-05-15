from django.shortcuts import render
from. models import Result

def home(request):
    search = ""
    results = Result.dummy

    if (request.method == 'POST'):
        search = request.POST['search']

    return render(request, 'webui/home.html', {'search':search, 'results':results})
