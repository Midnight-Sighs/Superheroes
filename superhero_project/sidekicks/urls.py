from django.urls import path

from . import views

app_name="sidekicks"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sidekick_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('edit<int:sidekick_id>/', views.edit, name='edit'),
    path('delete<int:sidekick_id>/', views.delete, name='delete'),
]
