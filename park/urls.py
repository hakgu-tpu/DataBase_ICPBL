from django.urls import path
from . import views

app_name = 'park'

urlpatterns = [
    path('parking_map/<int:user_id>', views.parking_map, name="parking_map")
]