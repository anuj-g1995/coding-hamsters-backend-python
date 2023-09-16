from django.urls import path, include
from .views import JobList, JobDetail

urlpatterns = [
    path('listcreate/', JobList.as_view(), name='job_listcreate'),
    path('detail/<int:pk>', JobDetail.as_view(), name='job_detail'),
]
