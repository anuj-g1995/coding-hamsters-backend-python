from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job, JobApplyModel
from .serializers import JobSerializer, JobApplySerializer
from rest_framework import status, generics, permissions


# Create your views here.
class JobList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request):
        snippets = Job.objects.all()
        serializer = JobSerializer(snippets, many=True)
        return Response(data={"success": True, "status_code": status.HTTP_200_OK, "data": serializer.data,
                              "message": "Data Found"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"success": True, "status_code": status.HTTP_201_CREATED, "data": serializer.data,
                              "message": "Data Found"}, status=status.HTTP_201_CREATED)
        return Response(data={"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors,
                              "message": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class JobDetail(APIView):

    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = JobSerializer(snippet)
        return Response(data={"success": True, "status_code": status.HTTP_200_OK, "data": serializer.data,
                              "message": "Data Found"}, status=status.HTTP_200_OK)


class JobFilter(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        filter_val = self.kwargs['filter_val']
        return Job.objects.filter(category=filter_val)


class JobApplyCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = JobApplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"success": True, "status_code": status.HTTP_201_CREATED, "data": serializer.data,
                              "message": "Data Found"}, status=status.HTTP_201_CREATED)
        return Response(data={"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors,
                              "message": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class JobApplyDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return JobApplyModel.objects.get(pk=pk)
        except JobApplyModel.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = JobApplySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"success": True, "status_code": status.HTTP_200_OK, "data": serializer.data,
                              "message": "Data Found"}, status=status.HTTP_200_OK)
        return Response(data={"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors,
                              "message": "Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, status=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(
            data={"success": True, "status_code": status.HTTP_204_NO_CONTENT, "data": [], "message": "Record Found"},
            status=status.HTTP_204_NO_CONTENT)


class JobApplyFilterView(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        filter_val = self.kwargs['filter_val']
        if filter_val == 'is_applied':
            return JobApplyModel.objects.filter(is_applied=True)
        elif filter_val == 'is_saved':
            return JobApplyModel.objects.filter(is_saved=True)
