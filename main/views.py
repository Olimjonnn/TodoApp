from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view, action
from rest_framework.generics import ListAPIView, ListCreateAPIView
from main.models import *
from main.serializer import *

class WorksView(ListCreateAPIView):
    queryset = Works.objects.all()
    serializer_class = WorkSerializer


class WorkTrue(ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorkSerializer

    def list(self, request):
        work = Works.objects.all()
        a = []
        for i in work:
            if i.finished == True:
                dat = {
                    'Name': i.name,
                    'Day': i.day,
                    'Finished or Not': i.finished,
                }
                a.append(dat)
                data = {
                    "These works finished ":
                    a
                }
        return Response(data)


class WorkFalse(ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorkSerializer

    def list(self, request):
        work = Works.objects.all()
        a = []
        for i in work:
            if i.finished == False:
                dat = {
                    'Name': i.name,
                    'Day': i.day,
                    'Finished or Not': i.finished,
                }
                a.append(dat)
                data = {
                    "These works not finished yet":
                    a
                }
        return Response(data)
        