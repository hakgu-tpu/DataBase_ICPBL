from django.urls import path
from . import views

app_name = 'park'

urlpatterns = [
    path('parking_map/<int:building_num>', views.parking_map, name="parking_map"),
    path('inquiry_list/<int:user_id>', views.inquiry, name="inquiry_list"),
]