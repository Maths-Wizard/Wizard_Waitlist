from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User
from .validations import clean_data
from .serializers import (SuscriberSerializer,
                          RegisterSerializer)

# Create your views here.


class WelcomeView(generics.GenericAPIView):
    """ returns welcome message """
    permission_classes = [permissions.AllowAny]
    ##

    def get(self, request):
        return Response({'message': "Welcome!!"}, status=status.HTTP_200_OK)


# class UserListApiView(generics.ListCreateAPIView):
#     """ filter api for admins """
#     permission_classes = (permissions.AllowAny,)
#     queryset = User.objects.all()
#     serializer_class = SuscriberSerializer
#     name = 'email'

#     search_fields = (
#         '^email',
#     )


class UserRegister(generics.CreateAPIView):
    """ Register a new user """
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        # print(f"request.data ==> {request.data}")
        data = clean_data(request.data)
        # print(f"data ==> {data}")

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(data)
            if user:
                return Response({'message': 'User added successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'User not added'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
