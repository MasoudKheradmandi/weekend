from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerialzerOutPut


class IsSuperUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.method == "GET":
            return bool(request.user and request.user.is_superuser)
        return True



class UserApiView(APIView):
    permission_classes = [IsSuperUser,]
    
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerialzerOutPut(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = UserSerialzerOutPut(data=request.data)
        return Response("ooooK")

