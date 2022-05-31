from django.shortcuts import render

# Create your views here.

def Visualize(request):
    return render(request, 'Visualize.html')
