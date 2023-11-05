from django.urls import path
from menu_app.views import menu_view

urlpatterns = [
    path('', menu_view, {'menu_name': 'menu1.1'}, name='menu_view'),
    path('menu/<str:menu_name>/', menu_view, name='menu_view'),
]