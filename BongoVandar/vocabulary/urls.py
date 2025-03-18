from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_list, name='word_list'),
    path('add/', views.add_word, name='add_word'),
    path('update/<int:word_id>/', views.update_word, name='update_word'),
    path('delete/<int:word_id>/', views.delete_word, name='delete_word'),
]