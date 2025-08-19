from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,'args.html',{'first':'it','last':'python'})


def fbv_function(request):
    return HttpResponse("fbv_view")


from django.views import View


class CBVview(View):
    def get(self,request):
        return HttpResponse("cbv_view")
