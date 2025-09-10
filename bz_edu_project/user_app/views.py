from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from user_app.serializers import RegisterSerializer, UserDetailSerializer
from user_app.models import User
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework import generics
from django.shortcuts import redirect

# Create your views here.
class LoginView(APIView):
    def get(self,request):
        return render(request,'login.html')

    def post(self, request):
        # 1.获取参数
        phone = request.data.get('phone')
        password = request.data.get('password')
        remember = request.data.get('remember')
        # print(phone)
        # print(password)
        # 2.从数据库里找数据
        try:
            user = User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            return Response({'code': status.HTTP_404_NOT_FOUND, 'msg': '用户不存在'})

        if user.check_password(password):
            if remember == 'remember':
                HttpResponse.set_cookie('phone',phone,max_age=60*60*24*3)
            # return redirect('index')
            return Response({
                'code': status.HTTP_200_OK,
                'msg': '登录成功',
                'nickname': user.nickname,
                'user_id': user.id
            })
        else:
            # return redirect('login')
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': '密码错误'})


class RegisterView(APIView):
    def get(self,request):
        return render(request,'register.html')
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
            # return Response({
            #     'code': status.HTTP_201_CREATED,
            #     'msg': '注册成功'
            # })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'msg': f'注册失败:{serializer.errors}'
            })


class UserDetail(generics.RetrieveAPIView):  # 实现用id查询数据
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
