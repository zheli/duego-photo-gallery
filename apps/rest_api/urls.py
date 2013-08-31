from apps.rest_api import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'users/$', views.UserRegisterView.as_view(), name='user-register'),
    url(r'photos/$', views.PhotoUploadListView.as_view(), name='photo-upload-list'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
