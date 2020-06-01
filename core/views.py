from django.http import Http404
from core.models import Log
from core.serializers import LogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class LogList(APIView):

    """
    List all logs, or create a new log.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogDetail(APIView):
    """
    Retrive, or delete a log instance
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except Log.DoesNotExists:
            raise Http404

    def get(self, request, pk):
        log = self.get_object(pk)
        serializer = LogSerializer(log)
        return Response(serializer.data)

    def delete(self, request, pk):
        log = self.get_object(pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)