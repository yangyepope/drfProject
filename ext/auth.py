from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models


class QueryParamAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if not token:
            return
        user_object = models.User.objects.filter(token=token).first()
        if user_object:
            print(user_object,token)
            return user_object, token
        return

    def authenticate_header(self, request):
        return "api"


class HeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return
        user_object = models.User.objects.filter(token=token).first()
        if user_object:
            return user_object, token
        return

    def authenticate_header(self, request):
        return "api"


class NoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        raise AuthenticationFailed({"code": 10001, "message": "认证失败"})

    def authenticate_header(self, request):
        return "api"