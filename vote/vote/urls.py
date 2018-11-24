from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('qa/', include('qa.urls')),
    path('admin/', admin.site.urls),
]
