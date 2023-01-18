from django. urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:unique_id>', views.req),
    path('dashboard/<str:username>', views.dashboard, name = 'dashboard'),
    path('dashboard/<str:username>/urls/<str:unique_id>', views.url_stats, name = 'url_stats'),
]

