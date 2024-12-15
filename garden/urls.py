from django.urls import path
from .views import index,gul_by_tur,gul_detail

urlpatterns = [
    path('', index, name='home'),
    path('Turlar/<int:turi_id>/', gul_by_tur, name='gul_by_tur'),
    path('posts/<int:pk>/', gul_detail, name='detail'),
]