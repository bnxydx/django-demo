from django.shortcuts import render

def index(request):
    """首页视图"""
    return render(request, 'index.html')