from django.urls import path

from . import views

app_name = 'raml_loader_api'
urlpatterns = [
    path('<str:raml_folder>/', views.get_documentation, name='get_documentation'),
]
