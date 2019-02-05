from django.urls import path
from django.conf import settings
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
