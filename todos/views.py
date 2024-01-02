from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework import status

def index(request):
    return HttpResponse("Hello, world. You're at the todos index.")

def detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    
    return HttpResponse(f"You're looking at todo {id} -> {todo.title} -> {todo.completed}")

def todo_lists(request):
    todos = Todo.objects.all()
    template = loader.get_template("todo_lists.html")

    return HttpResponse(template.render({'todos': todos}, request))

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/todo-list/',
        'Detail View': '/todo-detail/<int:pk>/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<str:pk>/',
        'Delete': '/todo-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all().order_by('title')
    serializer = TodoSerializer(todos, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def todoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def todoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return JsonResponse("Todo successfully deleted!", safe=False)