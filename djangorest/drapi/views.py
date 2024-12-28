from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Teacher
from .serializers import TeacherSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_all_teachers(request, pk = None):
    if request.method == 'GET':
        id = pk
    if id is not None:
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   

@api_view(['POST'])
def create_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    serializer = TeacherSerializer(teacher, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def teacher_detail_or_delete(request, pk):
    # Handle GET request: Retrieve a specific teacher
    if request.method == 'GET':
        teacher = get_object_or_404(Teacher, id=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Handle DELETE request: Delete a specific teacher
    elif request.method == 'DELETE':
        teacher = get_object_or_404(Teacher, id=pk)
        teacher.delete()
        return Response({'message': 'Teacher deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


   