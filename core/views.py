from django.http import Http404
from core.models import Log
from core.serializers import LogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated


class LogSearch(generics.ListAPIView):
    """
    Search for logs.
    """

    permission_classes = [IsAuthenticated]

    search_fields = ["log"]
    filter_backends = (filters.SearchFilter,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class LogList(generics.ListCreateAPIView):
    """
    List all logs, or create a new log.
    """

    permission_classes = [IsAuthenticated]

    queryset = Log.objects.all()
    serializer_class = LogSerializer


class LogDetail(APIView):
    """
    Retrive, or delete a log instance
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except Log.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        log = self.get_object(pk)
        serializer = LogSerializer(log)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        log = self.get_object(pk)
        serializer = LogSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        log = self.get_object(pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
