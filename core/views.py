# from django.shortcuts import render
from django.http import HttpResponse
from core.models import Log
from core.serializers import LogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse("Hello World!")


class LogList(APIView):
    """
    List all logs, or create a new log.
    """
    def get(self, request, format=None):
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
