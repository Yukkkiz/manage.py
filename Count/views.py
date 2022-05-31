from django.shortcuts import render

# Create your views here.

def Count(request):
    return render(request, 'Count.html')
