from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='listar_pub'),
    path('pub/<int:pk>', views.detalle_pub, name='detalle_pub'),
    path('pub/nueva/', views.nueva_pub, name='nueva_pub'),
    path('pub/<int:pk>/editar/', views.editar_pub, name='editar_pub'),
    path('borrador/', views.post_draft_list, name='post_draft_list'),
    path('pub/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]
