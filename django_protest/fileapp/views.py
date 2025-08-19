from django.http import Http404
from django.shortcuts import render
from .models import UploadImg
# Create your views here.
from rest_framework.views import APIView
class upload_file(APIView):
    def get(self,request):
        return render(request,'upload_file.html')
    def post(self,request):
        u = UploadImg()
        u.file = request.FILES.get('file')
        u.img = request.FILES.get('img')
        u.desc = request.POST.get('desc')
        u.save()
        return render(request,'show.html',{'upload':u})


class GetFileView(APIView):
    def get(self, request, pk, format=None):
        try:
            upload = UploadImg.objects.get(pk=pk)
        except UploadImg.DoesNotExist:
            raise Http404("图片不存在")

        return render(request, 'show.html', {'upload': upload})