from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),

]

from django.urls import path
from . import views

urlpatterns += [
	path('', views.listar_objetos, name='paciente_listar'),
	path('novo/', views.criar_objeto, name='paciente_criar'),
	path('<int:pk>/', views.detalhar_objeto, name='paciente_detalhe'),
	path('<int:pk>/editar/', views.editar_objeto, name='paciente_editar'),
	path('<int:pk>/excluir/', views.excluir_objeto, name='paciente_excluir'),
]
