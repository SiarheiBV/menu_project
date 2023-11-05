from django.urls import path
from menu_app.views import test_view

urlpatterns = [
    path('', test_view, name='test_page')
]
