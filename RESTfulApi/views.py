from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from RESTfulApi import serializers
from RESTfulApi.serializers import DishSerializer
from dcxt.models import Dish


class DishList(APIView):
    """
    List all dishes, or create a new dish.
    """
    def get(self,request,format=None):
        dishs = Dish.objects.all()
        serializer = DishSerializer(dishs,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DishDetail(APIView):
    """
    Retrieve, update or delete a dish instance.
    """
    def get_object(self,id):
        try:
            return Dish.objects.get(id=id)
        except Dish.DoesNotExist:
            raise Http404

    def get(self,request,id,formate=None):
        dish = self.get_object(id)
        serializer = DishSerializer(dish)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        dish = self.get_object(id)
        serializer = DishSerializer(dish,data=request.query_params,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        dish = self.get_object(id)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)