from django.shortcuts import render, HttpResponse


# Create your views here.
def login_form(request):
    return render(request, 'user/login.html')


def get_user(request, id):
    return HttpResponse(f"user:{id}")


def page_not_found(request, exception):
    print("enter")
    return render(request, 'user/a404.html', status=404)


# 添加首页视图
def index(request):
    return render(request, 'home/index.html')
