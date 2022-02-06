from argparse import Action
from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status
from .models import Student
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from .serializers import UserSerializer, GroupSerializer
from .permissions import IsOwnerOrReadOnly 
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                   IsOwnerOrReadOnly]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    
# @api_view(['GET'])
# def Get_Student(request):
#     if request.method=='GET':
#         id = request.data.get('id')
#         if id == None:
#             stu= Student.objects.all()
#             djangodata= StudentSerializer(stu)
#             return Response(djangodata.data)
#         stu = Student.objects.get(id=id)
#         djangodata = StudentSerializer(stu)
#     return Response(djangodata.data)