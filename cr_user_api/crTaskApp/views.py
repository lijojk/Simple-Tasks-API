from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# create Task ----------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Add TokenAuthentication
@permission_classes([IsAuthenticated])  # Add IsAuthenticated and IsAdminUser permissions
def taskCreate(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# read --all list -------------------------------------------------------------------------------------------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Add TokenAuthentication
@permission_classes([IsAuthenticated])  # Add IsAuthenticated and IsAdminUser permissions
def TaskListView(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# read -- using task_id --------------------------------------------------------------------------------------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Add TokenAuthentication
@permission_classes([IsAuthenticated])  # Add IsAuthenticated and IsAdminUser permissions
def TaskDetail(request, task_id):
    try:
        task = Task.objects.get(custom_id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)


# update ----------------------------------------------------------------------------------------------------------
@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])  # Add TokenAuthentication
@permission_classes([IsAuthenticated])  # Add IsAuthenticated and IsAdminUser permissions
def TaskUpdate(request, task_id):
    try:
        task = Task.objects.get(custom_id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete ----------------------------------------------------------------------------------------------------------
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])  # Add TokenAuthentication
@permission_classes([IsAuthenticated])  # Add IsAuthenticated and IsAdminUser permissions
def TaskDestroy(request, task_id):
    try:
        task = Task.objects.get(custom_id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------- The End ----------------------------------------------------------------
