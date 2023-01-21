from django.urls import path, include
from .views import say_hello

urlpatterns = [
    path('', say_hello, name="hello"),
]