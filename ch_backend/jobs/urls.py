from django.urls import path, include, re_path
from .views import JobList, JobDetail, JobFilter, JobApplyCreateApiView, JobApplyDetailView, JobApplyFilterView

urlpatterns = [
    path('listcreate/', JobList.as_view(), name='job_listcreate'),
    path('detail/<int:pk>', JobDetail.as_view(), name='job_detail'),
    re_path('^filter/(?P<filter_val>.+)/$', JobFilter.as_view(), name="job_filter"),

    path('apply/', JobApplyCreateApiView.as_view(), name='job_apply'),
    path('applied/edit/<int:id>', JobApplyDetailView.as_view(), name='job_appled_edit'),
    re_path('^applied/filter/(?P<filter_val>.+)/$', JobApplyFilterView.as_view(), name="job_applied_filter"),
]
