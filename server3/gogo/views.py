from django.shortcuts import render

# Create your views here.
def gogo(request):
    return render(request, 'gogo.html')
