from django.urls import path
from products.views import get_info


urlpatterns = [
    path('', get_info),
]