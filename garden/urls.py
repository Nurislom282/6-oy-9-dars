from django.urls import path
from .views import index,gul_by_tur,gul_detail,add_post,update_post

urlpatterns = [
    path('', index, name='home'),
    path('Turlar/<int:turi_id>/', gul_by_tur, name='gul_by_tur'),
    path('posts/<int:pk>/', gul_detail, name='detail'),
    path('add-post/', add_post, name='add_post'),
    path('posts/<int:pk>/update/', update_post, name='update_post'),

]