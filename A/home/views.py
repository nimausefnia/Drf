from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def one(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({'name': f'my name is{name}'})
    else:
        return Response({'name': ' my name is nima'})

#
# @api_view()
# @permission_classes([IsAdminUser,])
# def persons(request):
#     persons = Person.objects.all()
#     ser_data = PersonSerializer(persons, many=True)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# def person(request, name):
#     try:
#         person = Person.objects.get(name=name)
#     except Person.DoesNotExist:
#         return Response({'error': 'this user does not exist'},status=status.HTTP_404_NOT_FOUND)
#     ser_data = PersonSerializer(person)
#     return Response(ser_data.data,status=status.HTTP_200_OK)
#
#
# @api_view(['POST'])
# def person_create(request):
#     info = PersonSerializer(data=request.data)
#     if info.is_valid():
#         Person(name=info.validated_data['name'], age=info.validated_data['age'],
#                email=info.validated_data['email']).save()
#         return Response({'message': 'ok'},status=status.HTTP_200_OK)
#     else:
#         return Response(info.errors,status=status.HTTP_400_BAD_REQUEST)
