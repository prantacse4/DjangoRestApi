from django.shortcuts import render
from .models import MyApi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyApiSerializer
from django.http import JsonResponse

# Create your views here.

def home(request):
    data = MyApi.objects.all().order_by('-id')
    diction = { 'data':data, }
    return render(request, 'appapi/home.html', context=diction)


@api_view(['GET', 'POST'])
def details(request):
    if request.method=="GET":
        data = MyApi.objects.all()
        serializer = MyApiSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer = MyApiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'PUT'])
def UniqueView(request,id):
    try:
        gettingdata = MyApi.objects.get(pk=id)
    except MyApi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = MyApiSerializer(gettingdata)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MyApiSerializer(gettingdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == "DELETE":
    #     gettingdata.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view([ 'DELETE'])
def deletedata(request,id):
    if request.method == "DELETE":
        mydata = MyApi.objects.get(pk=id)
        mydata.delete()
        return JsonResponse({'status':0})