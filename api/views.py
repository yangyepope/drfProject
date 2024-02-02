from django.shortcuts import render

# Create your views here.
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response

import ext.auth
from ext.auth import BaseAuthentication
from ext import code

from api import models


# Create your views here.

class HomeView(APIView):
    authentication_classes = [ext.auth.QueryParamAuthentication]

    def get(self, request):
        return Response("...")


class LoginView(APIView):
    authentication_classes = []

    def post(self, request):
        print(request.data)
        print(request.query_params)
        user = request.data.get("username")
        pwd = request.data.get("password")

        # 验证数据
        user_object = models.User.objects.filter(username=user, password=pwd).first()

        if not user_object:
            return Response({"status": code.ERROR_CODE, "message": "用户或密码不正确"}, status=400)

        # 正确
        token = str(uuid.uuid4())
        user_object.token = token
        user_object.save()

        return Response({"status": 200, 'data': token})


class UserView(APIView):
    # authentication_classes = [ext.auth.HeaderAuthentication]

    def get(self, request):
        print(request.user, request.auth)
        return Response("UserView")
