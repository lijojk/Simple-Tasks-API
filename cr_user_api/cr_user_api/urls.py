from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cr-user/', include('crUserApp.urls')),
    path('cr-task/', include('crTaskApp.urls')),
]

