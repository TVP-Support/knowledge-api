from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/note/', include('note.urls_api')),
    path('api/v1/faci/', include('faci.urls_api')),
    path('note/', include('note.urls')),
    path('faci/', include('faci.urls')),
    path('auth/', include('custom_auth.urls')),
    path('', include('pages.urls')),
]
