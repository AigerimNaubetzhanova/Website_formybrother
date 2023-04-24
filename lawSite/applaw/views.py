from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def successful_cases(request):
    return render(request, 'successful_cases.html', {})
