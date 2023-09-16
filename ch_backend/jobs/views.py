from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework import status


# Create your views here.
class JobList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Job.objects.all()
        serializer = JobSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetail(APIView):

    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = JobSerializer(snippet)
        return Response(serializer.data)


# class GetOrdersListView(generics.ListAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     queryset = OrderModel.objects.filter().order_by('id')
#
#     serializer_class = OrderModelSerializer
#
#     # filter_backends = []
#
#     filter_backends = [CustomOrderFilterBackend]
#
#     # filterset_class = CustomOrderFilterBackend
#
#     filterset_fields = ['user_role']
#
#     # ordering_fields = ['first_name']
#
#     # ordering = ['first_name']
#
#     def list(self, request, *args, **kwargs):
#
#         try:
#
#             queryset = self.filter_queryset(self.get_queryset())
#
#             limit = request.GET.get('items_per_page', 10)
#
#             page_number = request.GET.get('page', 1)
#
#             totalpages, object_list, page = paginatedResults(queryset, int(limit), int(page_number))
#
#             # print(object_list)
#
#             serializer = self.get_serializer(object_list, many=True)
#
#             # print(totalpages)
#
#             if serializer.data:
#                 # print(serializer.data)
#
#                 return Response({
#
#                     "success": True,
#
#                     "error": False,
#
#                     "message": "Orders List!!",
#
#                     "data": {
#
#                         "total_pages": totalpages,
#
#                         "current_page": page.number,
#
#                         #
#
#                         "data": serializer.data
#
#                     },
#
#                 }, status=status.HTTP_200_OK)
#
#             return Response({
#
#                 "success": True,
#
#                 "message": "Orders Not found!",
#
#                 "data": {
#
#                     "total_pages": totalpages,
#
#                     "current_page": page.number,
#
#                     #
#
#                     "data": serializer.data
#
#                 },
#
#                 # "error": serializer.errors ,
#
#             }, status=status.HTTP_200_OK)
#
#
#
#
#
#         except Exception as e:
#
#             return Response({
#
#                 "success": False,
#
#                 "error": True,
#
#                 "message": f"Internal Server Error: {str(e)}",
#
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)