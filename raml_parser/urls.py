from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<str:raml_name>/', views.get_documentation, name='vote'),
]
