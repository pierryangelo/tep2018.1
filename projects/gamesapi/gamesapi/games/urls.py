from django.urls import path

from .views import game_list, game_detail

urlpatterns = [
    path(r'games/', game_list),
    path(r'games/<int:pk>', game_detail)
]
