from django.urls import path

from core import views

urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view(),
         name=views.UsuarioList.name),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view(),
         name=views.UsuarioDetail.name),
    path('planos/', views.PlanosDeEstudoList.as_view(),
         name=views.PlanosDeEstudoList.name),
    path('plano/<int:pk>/', views.PlanosDeEstudoDetail.as_view(),
         name=views.PlanosDeEstudoDetail.name),
    path('disciplinas/', views.DisciplinaList.as_view(),
         name=views.DisciplinaList.name),
    path('disciplina/<int:pk>/', views.DisciplinaDetail.as_view(),
         name=views.DisciplinaDetail.name),
    path('assuntos/', views.AssuntoList.as_view(),
         name=views.AssuntoList.name),
    path('assunto/<int:pk>/', views.AssuntoDetail.as_view(),
         name=views.AssuntoDetail.name),
    path('atividades/', views.AtividadeList.as_view(),
         name=views.AtividadeList.name),
    path('atividade/<int:pk>/', views.AtividadeDetail.as_view(),
         name=views.AtividadeDetail.name),
]