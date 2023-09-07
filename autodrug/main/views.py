from django.shortcuts import render

# Create your views here.

def index(requiest):
    return render(requiest,'main/index.html')

def index1(requiest):
    return render(requiest, 'main/second.html')