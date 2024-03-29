from django.urls import path

from pages.views import (
    AboutProjectView,
    MapInfoResourcesView,
    MapMaterialResourcesView,
    ServiceServerView,
    ProfileView,
)


urlpatterns = [
    path('map_info_resources', MapInfoResourcesView.as_view(), name='map_info_resources'),
    path('map_material_resources', MapMaterialResourcesView.as_view(), name='map_material_resources'),
    path('service_server', ServiceServerView.as_view(), name='service_server'),
    path('profile', ProfileView.as_view(), name='custom_profile'),
    path('', AboutProjectView.as_view(), name='index'),
]
