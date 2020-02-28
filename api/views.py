from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/readAllEmp',
        'Read' : 'readEmp/<str:pk>/',
        'Create' : '/createEmp/',
        'Update' : 'updateEmp/<str:pk>/',
        'Delete' : '/deleteEmp/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['POST'])
def newEmployee(request):
    print(request.data)
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def readAllEmp(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def readEmployee(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def updateEmp(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task ,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEmp(request, pk):
    task = Task.objects.get(id=pk)
    print(task.delete())

    return Response(True);