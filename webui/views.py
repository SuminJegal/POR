from django.shortcuts import render

# Create your views here.
def home(request):
    search = ""
    if (request.method == 'POST'):
        search = request.POST['search']
    return render(request, 'webui/home.html', {'search':search})

