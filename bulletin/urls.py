from django.contrib import admin
from django.urls import include, re_path as url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^board/', include('board.urls')),
]
