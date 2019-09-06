from django.urls import path
from . import views

urlpatterns = [
	path('', views.ajouter_fichier, name='ajouter_fichier'),
	path('ajouter_fichier/', views.ajouter_fichier, name='ajouter_fichier'),
    path('voir_fichiers/', views.voir_fichiers, name='voir_fichiers'),
	#path('voir_fichier/<int:id>', views.voir_fichier, name='voir_fichiers'),
]