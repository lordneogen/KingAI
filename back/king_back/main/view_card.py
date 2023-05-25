from django.shortcuts import render

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from . import serializers
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


def CARDS_LEARN():
    count = Cards.objects.filter(is_learn=True)
    res=[]
    for x in count:
        serializer_new =serializers.SER_Cards(x)
        res.append(serializer_new.data)
    return res

def CARDS_TEST():
    count = Cards.objects.all()
    res=[]
    for x in count:
        serializer_new =serializers.SER_Cards(x)
        res.append(serializer_new.data)
    return res


class LIST_Cards(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Cards.objects.all().order_by('-id')
    serializer_class = serializers.SER_Cards

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset = Cards.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Cards(data=queryset, many=True)
        if serializer.is_valid():
            return {'error': 'not have users'}
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Cards(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Cards.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Cards.objects.get(id=pk)
        ser = serializers.SER_Cards(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
