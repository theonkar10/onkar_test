from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cat_id>/', views.show_quiz, name='show_quiz'),
]
