from django.urls import path
from orders.views import get_info


urlpatterns = [
    path('', get_info),
]