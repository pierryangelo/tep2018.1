from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.ApiRoot.as_view(),
         name=views.ApiRoot.name),

    path('users/',
         views.UserList.as_view(),
         name=views.UserList.name),

]
