import ast

from django.shortcuts import render

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from scipy.interpolate import make_interp_spline

from . import serializers
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai.template import *

class LIST_Kings(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Kings.objects.all().order_by('-id')
    serializer_class = serializers.SER_Kings

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset = Kings.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Kings(data=queryset, many=True)
        if serializer.is_valid():
            return {'error': 'not have users'}
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Kings(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Kings.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Kings.objects.get(id=pk)
        ser = serializers.SER_Kings(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

class LIST_Num_edu(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Num_edu.objects.all().order_by('-id')
    serializer_class = serializers.SER_Num_edu

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset = Num_edu.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Num_edu(data=queryset, many=True)

        if serializer.is_valid():
            pass

        # print(serializer.data[0]["graph"])

        for x in serializer.data:
            x1=ast.literal_eval(x["graph_num"])
            y1=ast.literal_eval(x["graph"])
            X_Y_Spline = make_interp_spline(np.array(x1), np.array(y1))

        # Returns evenly spaced numbers
        # over a specified interval.
            X_ = np.linspace(np.array(x1).min(),np.array(x1).max(), 100)
            Y_ = X_Y_Spline(X_)
            x["graph"]=str(Y_.tolist())
            x["graph_num"] = str(X_.tolist())


        return Response(serializer.data)
    # id = models.BigAutoField(primary_key=True)
    # desc= models.TextField(blank=True, null=False,default="")
    # card_num=models.IntegerField(blank=True, null=False,default=0)
    # error=models.FloatField(blank=True, null=False,default=0)
    # graph=models.TextField(blank=True, null=False,default="")
    # dif_money=models.IntegerField(blank=True, null=False,default=0)
    # dif_popularity = models.IntegerField(blank=True, null=False, default=0)
    # dif_army = models.IntegerField(blank=True, null=False, default=0)
    # dif_land = models.IntegerField(blank=True, null=False, default=0)
    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Num_edu(data=request.data)
        if ser.is_valid():
            dt = ser.validated_data
            try:
                last_object = Num_edu.objects.latest('id')
                res = create_model(dt["epo"], dt["dif_money"], dt["dif_popularity"], dt["dif_army"], dt["dif_land"],
                               (last_object.id+1))
            except:
                res = create_model(dt["epo"], dt["dif_money"], dt["dif_popularity"], dt["dif_army"], dt["dif_land"],
                               1)
            # print(res)
            ser.validated_data["error"]=res[0]*100
            ser.validated_data["graph"]=res[3]
            ser.validated_data["graph_num"]=res[4]
            ser.validated_data["desc"] = res[2]
            ser.validated_data["card_num"]=len(CARDS_LEARN())

            ser.save()

            # print(res)
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Num_edu.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Cards.objects.get(id=pk)
        ser = serializers.SER_Cards(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

class LIST_Trys(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Trys.objects.all()
    serializer_class = serializers.SER_Trys

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset = Trys.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Trys(data=queryset, many=True)
        if serializer.is_valid():
            return {'error': 'not have users'}
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Trys(data=request.data)
        if ser.is_valid():
            dt = ser.validated_data
            res = set_model(dt["epo"], dt["dif_money"], dt["dif_popularity"], dt["dif_army"], dt["dif_land"],dt["num"])
            print(res)
            ser.validated_data["card_num"]=len(CARDS_TEST())
            ser.validated_data["graph"]=res[3]
            ser.validated_data["graph_num"]=res[4]
            print(str(res[2]))
            ser.validated_data["desc"] = str(res[2])
            ser.save()

            # print(res)
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Trys.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Trys.objects.get(id=pk)
        ser = serializers.SER_Trys(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
