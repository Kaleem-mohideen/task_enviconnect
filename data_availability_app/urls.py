from django.urls import path
from .views import get_data_points, post_data_point

urlpatterns = [
    path('get_data_points/', get_data_points, name='get_data_points'),
    path('post_data_point/', post_data_point, name='post_data_point'),
]
